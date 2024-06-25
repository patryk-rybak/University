
import os
import torch
import torch.nn as nn
import torch.optim as optim 
import torch.nn.functional as F
from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader, random_split
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class NN1(nn.Module):
    def __init__(self, device='cpu'):
        super(NN1, self).__init__()
        self.device = device
        self.fc1 = nn.Linear(14, 1000)
        self.fc2 = nn.Linear(1000, 700)
        self.fc3 = nn.Linear(700, 400)
        self.fc4 = nn.Linear(400, 100)
        self.fc5 = nn.Linear(100, 3)
        self.sigm = nn.Sigmoid()

    def forward(self, x):
        x = self.sigm(self.fc1(x.to(device)))
        x = self.sigm(self.fc2(x))
        x = self.sigm(self.fc3(x))
        x = self.sigm(self.fc4(x))
        x = self.fc5(x)
        return x

class CNN3(nn.Module):
    def __init__(self, hidden_dim=1000, out_dim=3, device='cpu'):
        super(CNN3, self).__init__()
        self.device = device

        self.conv1 = nn.Conv2d(3, 64, kernel_size=5, padding=2, stride=1)
        self.norm1 = nn.BatchNorm2d(64)
        self.conv2 = nn.Conv2d(64, 64, kernel_size=4, padding=2, stride=1)
        self.norm2 = nn.BatchNorm2d(64)
        self.conv3 = nn.Conv2d(64, 64, kernel_size=2, padding=1, stride=1)
        self.norm3 = nn.BatchNorm2d(64)
        self.conv4 = nn.Conv2d(64, 64, kernel_size=2, padding=1, stride=1)
        self.norm4 = nn.BatchNorm2d(64)

        self.relu = nn.ReLU()
        # self.sig = nn.Sigmoid()
        self.faltten = nn.Flatten()

        self.fc1 = nn.Linear(9*10*64, 1000)
        self.fc2 = nn.Linear(1000, 500)
        self.fc3 = nn.Linear(500, 3)
        #  moze dodac jeszcze jakas aktywacje miedzy full connected

    def forward(self, x):
        x = self.norm1(self.relu(self.conv1(x.to(device))))
        x = self.norm2(self.relu(self.conv2(x)))
        x = self.norm3(self.relu(self.conv3(x)))
        x = self.norm4(self.relu(self.conv4(x)))
        x = self.faltten(x)
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

class CustomResidualBlock(nn.Module):
    def __init__(self, features, kernel_size=2, padding=1, device="cpu", padd_first=None, padd_second=None):
        super(CustomResidualBlock, self).__init__()
        padding = padding if padd_first is None else padd_first
        self.conv1 = nn.Conv2d(features, features, kernel_size=kernel_size, padding=padding)
        padding = padding if padd_second is None else padd_second
        self.conv2 = nn.Conv2d(features, features, kernel_size=kernel_size, padding=padding)
        self.relu = nn.ReLU()
        self.device = device

    def forward(self, x):
        x_tmp = self.relu(self.conv1(x.to(self.device)))
        x_tmp = self.relu(self.conv2(x_tmp))
        return x_tmp + x

class CNN2(nn.Module):
    def __init__(self, hidden_dim=512, out_dim=3, device='cpu'):
        super(CNN2, self).__init__()
        self.device = device

        self.conv1 = nn.Conv2d(3, 64, kernel_size=4, padding=2) # (7x8)
        self.conv2 = nn.Conv2d(64, 32, kernel_size=3, padding=1) # (7x8)
        self.rc2 = CustomResidualBlock(32, kernel_size=3, padding=1, device=self.device) # (7x8)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=2, padding=0) # (6x7)
        self.rc3 = CustomResidualBlock(32, kernel_size=2, padd_first=1, padd_second=0, device=self.device) # -> (7x8) -> (6x7)

        self.fc1 = nn.Linear(32 * 6 * 7, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim//2)
        self.fc3 = nn.Linear(hidden_dim//2, out_dim)

        self.relu = nn.ReLU()
        self.flatten = nn.Flatten()

    def forward(self, x):
        x = self.relu(self.conv1(x.to(self.device)))
        x = self.relu(self.conv2(x))
        x = self.rc2(x)
        x = self.relu(self.conv3(x))
        x = self.rc3(x)
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x 

class CNN1(nn.Module):
    def __init__(self, hidden_dim=1000, out_dim=3, device='cpu'):
        super(CNN1, self).__init__()
        self.device = device

        self.conv1 = nn.Conv2d(3, 64, kernel_size=5, padding=2, stride=1)
        self.conv2 = nn.Conv2d(64, 64, kernel_size=4, padding=2, stride=1)
        self.conv3 = nn.Conv2d(64, 64, kernel_size=2, padding=1, stride=1)
        self.conv4 = nn.Conv2d(64, 64, kernel_size=2, padding=1, stride=1)

        self.relu = nn.ReLU()
        self.sig = nn.Sigmoid()
        self.faltten = nn.Flatten()

        self.fc1 = nn.Linear(9*10*64, 1000)
        self.fc2 = nn.Linear(1000, 500)
        self.fc3 = nn.Linear(500, 3)

    def forward(self, x):
        x = self.relu(self.conv1(x.to(device)))
        x = self.relu(self.conv2(x))
        x = self.relu(self.conv3(x))
        x = self.relu(self.conv4(x))
        x = self.faltten(x)
        x = self.sig(self.fc1(x))
        x = self.sig(self.fc2(x))
        x = self.fc3(x)
        return x


class CNN_1_channel(nn.Module):
    def __init__(self, device='cpu'):
        super(CNN_1_channel, self).__init__()
        self.device = device
        self.conv1 = nn.Conv2d(1, 64, kernel_size=4, padding=2, stride=1)
        self.conv2 = nn.Conv2d(64, 64, kernel_size=2, padding=1, stride=1)
        self.conv3 = nn.Conv2d(64, 64, kernel_size=2, padding=1, stride=1)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(9*10*64, 3)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.conv1(x.to(self.device)))
        x = self.relu(self.conv2(x))
        x = self.relu(self.conv3(x))
        x = self.flatten(x)
        x = self.fc1(x)
        return x


class CNN_3_channel(nn.Module):
    def __init__(self, device='cpu'):
        super(CNN_3_channel, self).__init__()
        self.device = device
        self.conv1 = nn.Conv2d(3, 64, kernel_size=4, padding=2, stride=1)
        self.conv2 = nn.Conv2d(64, 64, kernel_size=2, padding=1, stride=1)
        self.conv3 = nn.Conv2d(64, 64, kernel_size=2, padding=1, stride=1)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(9*10*64, 3)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.conv1(x.to(self.device)))
        x = self.relu(self.conv2(x))
        x = self.relu(self.conv3(x))
        x = self.flatten(x)
        x = self.fc1(x)
        return x
