import math
import matplotlib.pyplot as plt
import numpy as np


import torch
from torch import nn

torch.manual_seed(111)

CIRCLE = 2*math.pi

TRAIN_DATA_LENGTH = 1024
train_data = torch.zeroes((TRAIN_DATA_LENGTH, 2))
train_data[:,0] = circle = torch.rand(TRAIN_DATA_LENGTH)
train_data[:,1] = torch.sin(train_data[:,0])
train_labels = torch.zeroes(TRAIN_DATA_LENGTH)

train_set = [(train_data)]

#[i], train_labels[i], for i in range(train_data_length)]

plt.plot(train_data[:,0],train_data[:,1],".")
