from __future__ import print_function
import torch


def init_test():
    return 'init_test'


print(torch.__version__)

x_empty = torch.empty(5, 3)
print(x_empty)

x_rand = torch.rand(5, 3)
print(x_rand)
