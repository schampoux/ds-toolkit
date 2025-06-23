import torch.nn as nn 

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # input 3C 32x32  
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1), # -> 16C 32x32 
        self.act1 = nn.Tanh(),
        self.pool1 = nn.MaxPool2d(2), # -> 16C 16x16
        self.conv2 = nn.Conv2d(16, 8, kernel_size=3, padding=1), # 8C 16x16
        self.act2 = nn.Tanh(),
        self.pool2 = nn.MaxPool2d(2), # -> 8C 8x8
        # view(-1, 512) see forward()
        # -> batch x 512
        self.fc1 = nn.Linear(8*8*8, 32), # -> batch x 32
        self.act3 = nn.Tanh(),
        self.fc2 = nn.Linear(32, 2) # -> batch x 2

    def forward(self, x):
        out = self.pool1(self.act1(self.conv1(x)))
        out = self.pool2(self.act2(self.conv2(out)))
        out = out.view(-1, 8*8*8)
        out = self.act3(self.fc1(out))
        out = self.fc2(out)
        return out
