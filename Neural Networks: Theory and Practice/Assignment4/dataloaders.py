import os
import torch

import torch.nn as nn
import torch.optim as optim 
import torch.nn.functional as F

from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader, random_split

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class Connect4Dataset(Dataset):
    def __init__(self, file_path, channels, label_num, last_moves=13, feature_vector=False):
        self.data = []
        self.channels = channels
        with open(file_path, 'r') as file:
                num_lines = sum(1 for _ in file)
                file.seek(0)
                for line in tqdm(file, total=num_lines, desc="Loading Data"):
                    self.data.extend(self.convert_game_to_samples(line[:-1], last_moves, channels, label_num, feature_vector))
                    # tutaj uzyje tworzenie featerow
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        X, Y = self.data[idx]
        return X, Y

    @classmethod
    def convert_game_to_samples(cls, game, last_moves, channels, label_num, feature_vector):
        if not (feature_vector and label_num == 3 and channels == 1):
            raise Exception("Feature vector invalid use")

        if label_num == 3: label = Connect4Dataset.create_label_winner(game)
        elif label_num == 7: pass
        else: raise Exception("Wrong label number")

        game = game[1:-1]
        begin = len(game) - last_moves + 1

        if channels == 1: converter = Connect4Dataset.convert_state_to_1_channel_input
        elif channels == 3: converter = Connect4Dataset.convert_state_to_3_channel_input
        else: raise Exception("Wrong channel number")

        res = []
        for i in range(begin if begin > 0 else 1, len(game) + 1 if label_num == 3 else len(game)):
            board = converter(game[:i])
            if feature_vector: board = Connect4Dataset.create_feature_vector(board[0])
            if label_num == 7: label = Connect4Dataset.create_label_next_move(i, game)
            res.append((board, label))

        return res

    @classmethod
    def convert_state_to_3_channel_input(cls, state):
        board = torch.zeros(3, 7, 6) # shifted 90 degree right
        board[2] = torch.ones(7, 6)
        counter = torch.zeros(7, dtype=torch.int)
        player = 0
        try:
            for move in state:
                board[player][int(move)][counter[int(move)]] = 1
                board[2][int(move)][counter[int(move)]] = 0
                counter[int(move)] += 1
                player = 1 - player
        except Exception as e:
            pass
        return board

    @classmethod
    def convert_state_to_1_channel_input(cls, state):
        board = torch.zeros(1, 7, 6) # shifted 90 degree right
        counter = torch.zeros(7, dtype=torch.int)
        player = 1
        for move in state:
            board[0][int(move)][counter[int(move)]] = player
            counter[int(move)] += 1
            player *= -1
        return board

    @classmethod
    def create_label_winner(cls, game):
        label = torch.zeros(3)
        if game[-1] == 'A': label[0] = 1
        elif game[-1] == 'B': label[1] = 1
        else: label[2] = 1
        return label

    @classmethod
    def create_label_next_move(cls, i, game):
        label = torch.zeros(7)
        label[int(game[i])] = 1
        return label

    @classmethod
    def create_feature_vector(cls, state):
        # analyzes based on 1-channel input
        # remember that A is 1 and B is -1 in state

        features = []

        # whose turn (1 - A, 0 - B) (A is first)
        temp = torch.sum(state) % 2
        features.append(int(temp))

        # quantity of all moves
        temp = torch.sum(state != 0).item()
        features.append(temp)

        # quantity on odd rows (A)
        temp = torch.sum(state[1::2] == 1).item()
        features.append(temp)

        # quantity on odd rows (B)
        temp = torch.sum(state[1::2] == -1).item()
        features.append(temp)

        # quantity on even rows (A)
        temp = torch.sum(state[::2] == 1).item()
        features.append(temp)

        # quantity on even rows (B)
        temp = torch.sum(state[::2] == -1).item()
        features.append(temp)

        # number of fours (A)
        temp = Connect4Dataset.count_fours(state, 1)
        features.append(temp)

        # number of fours (B)
        temp = Connect4Dataset.count_fours(state, -1)
        features.append(temp)


        # number of not blocked threes (A)
        temp = Connect4Dataset.count_triplets_in_rows(state, 1)
        temp += Connect4Dataset.count_triplets_in_rows(state.t(), 1)
        temp += Connect4Dataset.count_triplets_in_diagonals(state, 1)
        temp += Connect4Dataset.count_triplets_in_diagonals(torch.flip(state, dims=[1]), 1)
        features.append(temp)

        # number of not blocked threes (B)
        temp = Connect4Dataset.count_triplets_in_rows(state, -1)
        temp += Connect4Dataset.count_triplets_in_rows(state.t(), -1)
        temp += Connect4Dataset.count_triplets_in_diagonals(state, -1)
        temp += Connect4Dataset.count_triplets_in_diagonals(torch.flip(state, dims=[1]), -1)
        features.append(temp)

        # number of twos (A)
        mask = state == 1
        filter_neighbors = torch.tensor([[1, 1, 1],
                                        [1, 0, 1],
                                        [1, 1, 1]]).unsqueeze(0).unsqueeze(0).int()
        neighbors_sum = torch.conv2d(mask.unsqueeze(0).unsqueeze(0).int(), filter_neighbors, padding=1)
        isolated_mask = (neighbors_sum == 1) & mask
        isolated_count = isolated_mask.sum().item()
        features.append(isolated_count // 2)

        # number of twos (B)
        mask = state == -1
        neighbors_sum = torch.conv2d(mask.unsqueeze(0).unsqueeze(0).int(), filter_neighbors, padding=1)
        isolated_mask = (neighbors_sum == 1) & mask
        isolated_count = isolated_mask.sum().item()
        features.append(isolated_count // 2)
        

        # number of isolated ones (A)
        mask = state == 1
        filter_neighbors = torch.tensor([[1, 1, 1],
                                        [1, 0, 1],
                                        [1, 1, 1]]).unsqueeze(0).unsqueeze(0).int()
        neighbors_sum = torch.conv2d(mask.unsqueeze(0).unsqueeze(0).int(), filter_neighbors, padding=1)
        isolated_mask = (neighbors_sum == 0) & mask
        isolated_count = isolated_mask.sum().item()
        features.append(isolated_count)

        # number of isolated ones (B)
        mask = state == -1
        neighbors_sum = torch.conv2d(mask.unsqueeze(0).unsqueeze(0).int(), filter_neighbors, padding=1)
        isolated_mask = (neighbors_sum == 0) & mask
        isolated_count = isolated_mask.sum().item()
        features.append(isolated_count)

        # number of fours with unit hole (A)
        # number of fours with unit hole (B)
        # use filters

        return torch.tensor([features]).squeeze(0)

    @classmethod
    def count_triplets_in_rows(cls, state, target):
        triplets_count = 0
        for row in state:
            row_with_padding = torch.cat([torch.tensor([2137]), row, torch.tensor([2137])])
            for i in range(1, len(row_with_padding) - 4):
                if row_with_padding[i] == row_with_padding[i+1] == row_with_padding[i+2] == target:
                    if row_with_padding[i-1] == 0 or row_with_padding[i+3] == 0:
                        triplets_count += 1
        return triplets_count

    @classmethod
    def count_triplets_in_diagonals(cls, state, target):
        # adjust for 6x7 board
        padded_board = torch.nn.functional.pad(state, (1, 1, 1, 1), value=2137)
        triplets_count = 0
        for i in range(2, 5):
            for j in range(1, 5 - (i - 2)):
                if (padded_board[i, j] == padded_board[i+1, j+1] == padded_board[i+2, j+2] == target):
                    if (padded_board[i-1, j-1] == 0 or padded_board[i+3][j+3] == 0):
                        triplets_count += 1
        for i in range(1, 4):
            for j in range(1, 5 - (i - 1)):
                if (padded_board[j, i+j-1] == padded_board[j+1, i+j] == padded_board[j+2, i+j+2] == target):
                    if (padded_board[j-1, i+j-2] == 0 or padded_board[j+3][i+j+3] == 0):
                        triplets_count += 1
        return triplets_count

    @classmethod
    def count_fours(cls, state, target):
        res = 0
        mask = state == target
        # vertical and horizontal
        filter = torch.tensor([[1, 1, 1, 1]])
        temp = filter.unsqueeze(0).unsqueeze(0).int()
        neighbors_sum = torch.conv2d(mask.unsqueeze(0).unsqueeze(0).int(), temp)
        fours = (neighbors_sum == 4)
        res += fours.sum().item()
        temp = filter.t().unsqueeze(0).unsqueeze(0).int()
        neighbors_sum = torch.conv2d(mask.unsqueeze(0).unsqueeze(0).int(), temp)
        fours = (neighbors_sum == 4)
        res += fours.sum().item()
        # diagonal
        for i in range(1, 4):
            for j in range(0, 3 - (i - 1)):
                if (state[i, j] == state[i+1, j+1] == state[i+2, j+2] == state[i+3][j+3] == target):
                        res += 1
        for i in range(0, 3):
            for j in range(0, 3 - i):
                if (state[j, i+j-1] == state[j+1, i+j] == state[j+2, i+j+2] == state[j+3][i+j+3] == target):
                        res += 1
        return res

