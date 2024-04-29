import os
import torch

import torch.nn as nn
import torch.optim as optim 
import torch.nn.functional as F

from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader, random_split

from models import *
from dataloaders import *


def train_model(model, trainloader, optimizer, criterion, num_epochs=5, device='cpu', verbose=True):
    if verbose:
        progressbar = tqdm(range(num_epochs), desc='Training', unit='epoch')
    else:
        progressbar = range(num_epochs)

    model.to(device)
    model.train()
    total_batches = len(trainloader)
    for epoch in progressbar:
        running_loss = 0.0
        for i, data in enumerate(trainloader):
            inputs, labels = data
            inputs = inputs.float() # tylko dla feature_vecotr
            inputs, labels = inputs.to(device), labels.to(device)
            
            optimizer.zero_grad()

            outputs = model(inputs)
            # print('inputs labels')
            # print(inputs)
            # print(labels)
            # print('outputs')
            # print(outputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            
            if verbose:
                progress = (i + 1) / total_batches * 100
                progressbar.set_postfix_str(f'Progress: {progress:.2f}%, Loss: {loss.item():.4f}')

        epoch_loss = running_loss / total_batches

    if verbose:
            progressbar.set_postfix_str(f'Progress: 100.00%, Loss: {epoch_loss:.4f}')
        

def check_sample(loaded_data):
    sample = loaded_data[0]
    print(f"Sample: {sample}")
    image, label = sample
    print(f"Image size: {image.size()}")
    print(f"Label: {label}")
    print(image)
    print('types')
    print('img', image.type())
    print('lab', label.type())


if __name__ == '__main__':

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    file_path1 = 'dataset'
    # file_path2 = 'processed_3_channel_data.pt'
    # file_path2 = 'processed_1_channel_data.pt'
    # file_path2 = '7_lables_3_channel_data.pt'# moze byc ciezsze ale ciekawe 
    file_path2 = 'feature_vector_data.pt'

    if os.path.exists(file_path2):
        print("Loading preprocessed data...")
        loaded_data = torch.load(file_path2)
    else:
        # connect4_dataset = Connect4Dataset(file_path1, channels=3, label_num=3)
        connect4_dataset = Connect4Dataset(file_path1, 1, 3, 50, True)
        torch.save(connect4_dataset, file_path2)
        loaded_data = connect4_dataset

    check_sample(loaded_data)
    
    batch_size = 32
    trainloader = DataLoader(loaded_data, batch_size=batch_size, shuffle=True, num_workers=4)

    model = NN1(device=device)
    model_name = 'NN1.pth'

    if os.path.exists(model_name):
        print("Loading model...")
        model.load_state_dict(torch.load(model_name))

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters())

    print('Start training...')
    train_model(model, trainloader, optimizer, criterion, num_epochs=8, device=device, verbose=True)

    print('Saving model...')
    model.to('cpu')
    torch.save(model.state_dict(), model_name)