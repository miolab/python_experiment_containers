from __future__ import print_function
import torch


def init_test():
    return 'init_test'


def getting_started():
    print(torch.__version__, "\n")

    x_empty = torch.empty(5, 3)
    print(x_empty, "\n")

    x_rand = torch.rand(5, 3)
    print(x_rand, "\n")


getting_started()
