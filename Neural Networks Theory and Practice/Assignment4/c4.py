from colorama import Fore, Style
from copy import deepcopy
import random
import sys
from utils import *
import torch.nn.functional as F

DX = 7
DY = 6
STRENGTH = 10
LEVEL = 3
GAMMA = 0.999

    
coins = [Fore.BLUE + '⬤', Fore.RED + '⬤']

directions = [ (1,0), (0,1), (1,-1), (1,1) ]

EMPTY = 0

class MyAgent:
    def __init__(self, model_class, model_path, device):
        self.name = 'MyAgent'
        self.model = model_class(device=device)
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()
        print('ok')

    def best_move(self, b):
        move_hostory = ''.join(map(str, b.last_moves))
        ms = b.moves()
        for m in ms:
            if b.is_winning(m): return m
        # inputs = torch.stack([Connect4Dataset.create_feature_vector(Connect4Dataset.convert_state_to_1_channel_input(move_hostory + str(m))[0]) for m in ms])
        # outputs = self.model(inputs.float())
        inputs = torch.stack([Connect4Dataset.convert_state_to_3_channel_input(move_hostory + str(m)) for m in ms])
        outputs = self.model(inputs)
        outputs = F.softmax(outputs)
        # print(outputs)
        # exit()
        return ms[outputs[:,(len(move_hostory) + 1) % 2].argmax().item()]

class AgentMC:
    def __init__(self, n_of_rollouts):
        self.n_of_rollouts = n_of_rollouts
        self.name = f'MC({self.n_of_rollouts})'
    
    def best_move(self, b):
        ms = b.moves()
        return b.best_move_rollouts(ms, self.n_of_rollouts)
    
class AgentRandom:
    def __init__(self):
        self.name = 'RND'
        
    def best_move(self, b):
        return b.random_move()
    
class AgentMinMaxMC:
    def __init__(self, level, n_of_rollouts):
        self.level = level
        self.n_of_rollouts = n_of_rollouts
        self.name = f'MM_MC({self.level}, {self.n_of_rollouts})'
    
    def best_move(self, b):
        return b.best_move(self.level, self.n_of_rollouts)
        

class Board:
    def __init__(self):
        self.board = [DX * [0] for y in range(DY)]
        self.hs = DX * [0]
        self.who = +1
        self.last_moves = []
        self.move_number = 0
        self.result = '?'
        
    def moves(self):
        return [n for n in range(DX) if self.hs[n] < DY]
        
    def apply_move(self, m):
        h = self.hs[m]
        self.board[h][m] = self.who
        self.hs[m] += 1
        self.who = -self.who
        self.last_moves.append(m)
        self.move_number += 1
        
    def undo_move(self, m):
        h = self.hs[m]
        self.board[h-1][m] = EMPTY
        
        self.hs[m] -= 1
        self.who = -self.who
        self.last_moves.pop()
        self.move_number -=1
                
    def print(self):
        for raw in self.board[::-1]:
            for x in range(DX):
                if raw[x] == EMPTY:
                    print ('  ', end='')
                else:
                    r = (raw[x] + 1) // 2
                    print (coins[r] + ' ', end='')
            print ()
        print (Fore.LIGHTYELLOW_EX + 2 * DX*'‒')
        for i in range(DX):
            if self.last_moves and i == self.last_moves[-1]:
                style = Style.BRIGHT
            else:
                style = Style.NORMAL
            print (style + str(i+1), end=' ')
                
        print ()   
        print ()   
        
    def random_move(self):
        ms = self.moves()
        for m in ms:
            if self.is_winning(m):
                return m
        return random.choice(ms)  
        
    def rollout(self, m):
        while True:
            if self.is_winning(m):
                return self.who
            self.apply_move(m)
            ms = self.moves()
            if ms == []:
                return 99
            m = self.random_move()               
            
    
    def move_value(self, m, n_of_rollouts):       
        value = 0
        who_is_playing = self.who 
        for i in range(n_of_rollouts):
            state = (self.who, self.last_moves[:], self.hs[:], deepcopy(self.board))
            
            r = self.rollout(m)
            if r == who_is_playing:
                value += 1
            if r == -who_is_playing:
                value -= 1
            
            self.who, self.last_moves, self.hs, self.board = state
                           
        return value
        
    def best_move_rollouts(self, ms,  n_of_rollouts):
        #return random.choice(ms)
        return max(ms, key=lambda x:self.move_value(x,  n_of_rollouts))
                
    def best_moves(self, level):
        #minimax
        ms = self.moves()
        
        vms = []
        for m in ms:
            if self.is_winning(m):
                return [m]
            self.apply_move(m)    
            vms.append( (self.mini_max(level), m))
            self.undo_move(m)
            
        if self.who == 1:
            min_max = max
        else:
            min_max = min
                        
        v_max,m = min_max(vms)
        
        good_moves = [m for (v,m) in vms if v == v_max]
        return good_moves
        
    def best_move(self, level, n_of_rollouts):
        ms = self.best_moves(level)   
        return self.best_move_rollouts(ms, n_of_rollouts)
                
    def mini_max(self, level):
        if level == 0:
            return 0
        ms = self.moves()
        if not ms:
            return 0
        
        vals = []
        for m in ms:
            if self.is_winning(m):
               return self.who * (GAMMA ** self.move_number)
            self.apply_move(m)
            
            vals.append(self.mini_max(level-1))
            self.undo_move(m)
        if self.who == +1:
            return max(vals)
        return min(vals)    
    
    def last_move_was_winning(self):
        return self.was_winning(self.last_moves[-1])
    
    def end(self):
        if not self.last_moves:
            return False
        if self.last_move_was_winning():
            if len(self.last_moves) % 2 == 0:
                self.result = -1
            else:
                self.result = +1
            return True    
        if len(self.last_moves) == DX*DY:
                self.result = 0
                return True 
        return False 
        
    def vertical_winning(self):
        return self.was_vertical_winning(self.last_moves[-1])
        
    def was_winning(self, m):    
        for dx, dy in directions:
            x,y = m, self.hs[m]-1  # after applying move        
            score = 0
            
            while self.board[y][x] == -self.who:
                score += 1
                x += dx
                y += dy
                if not (0<=x<DX and 0<=y<DY):
                    break
            
            x,y = m, self.hs[m]-1      
            dx = -dx
            dy = -dy
            
            while self.board[y][x] == -self.who:
                score += 1
                x += dx
                y += dy
                if not (0<=x<DX and 0<=y<DY):
                    break
            score -= 1
            
            if score >= 4:
                return True

        return False
 
    def was_vertical_winning(self, m):    
        for dx, dy in [(0,1)]:
            x,y = m, self.hs[m]-1  # after applying move        
            score = 0
            
            while self.board[y][x] == -self.who:
                score += 1
                x += dx
                y += dy
                if not (0<=x<DX and 0<=y<DY):
                    break
            
            x,y = m, self.hs[m]-1      
            dx = -dx
            dy = -dy
            
            while self.board[y][x] == -self.who:
                score += 1
                x += dx
                y += dy
                if not (0<=x<DX and 0<=y<DY):
                    break
            score -= 1
            
            if score >= 4:
                return True

        return False
 
    def is_winning(self, m):    
        for dx, dy in directions:
            x,y = m, self.hs[m]
            score = 0
            
            while True:
                x += dx
                y += dy
                if not (0<=x<DX and 0<=y<DY):
                    break
            
                if self.board[y][x] == self.who:
                    score += 1
                else:
                    break    
                        
            x,y = m, self.hs[m]
            dx = -dx
            dy = -dy
            
            while True:
                x += dx
                y += dy
                if not (0<=x<DX and 0<=y<DY):
                    break
            
                if self.board[y][x] == self.who:
                    score += 1
                else:
                    break    
            
            score += 1
            
            if score >= 4:
                return True

        return False  
        