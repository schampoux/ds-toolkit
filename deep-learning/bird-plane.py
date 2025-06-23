from torchvision import datasets, transforms
import torch.nn as nn 
import matplotlib.pyplot as plt 
import torch 

# due to the nature of the CIFAR10 dataset size, we will subset images based on their label. 
# instead of implementing a proper Dataset class as a subset. 

def get_mean_std(data):
    imgs = torch.stack([img_tensor for img_tensor, _ in data], dim=3)
    
def main(train, model):
    img, _ = train[0]
    img_batch = img.view(-1).unsqueeze(0)
    out = model(img_batch)
    out 

if __name__=="__main__":
    data_path = './datasets/'

    label_map = {0:0, 2:1}
    class_names = ['airplane', 'bird']

    cifar10 = datasets.CIFAR10(root = data_path, download=False, train=True, transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize()
    ]))
    cifar10_val = datasets.CIFAR10(root = data_path, download=False, train=False)

    cifar2 = [(img, label_map[label]) for img, label in cifar10 if label in [0,2]]
    cifar2_val = [(img, label_map[label]) for img, label in cifar10_val if label in [0,2]]

    n_out = 2
    model = nn.Sequential(
        nn.Linear(3072, 512),
        nn.Tanh(),
        nn.Linear(512, n_out),
        nn.Softmax(dim=1)
    )

    main(cifar2, model) 