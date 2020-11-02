from __future__ import print_function
import torch


def init_test():
    return 'init_test'


def do_getting_started():
    global x_rand

    print(torch.__version__, "\n")

    # Construct a 5x3 matrix, uninitialized:
    x_empty = torch.empty(5, 3)
    print(x_empty, "\n")

    # Construct a randomly initialized matrix:
    x_rand = torch.rand(5, 3)
    print(x_rand, "\n")

    # Construct a matrix filled zeros and of set dtype:
    x_zeros = torch.zeros(5, 3)
    print(x_zeros, "\n")

    x_zeros_dtype_long = torch.zeros(5, 3, dtype=torch.long)
    print("# dtype: long\n", x_zeros_dtype_long, "\n")

    x_zeros_dtype_float = torch.zeros(5, 3, dtype=torch.float)
    print("# dtype: float\n", x_zeros_dtype_float, "\n")

    # Construct a tensor DIRECTLY from data:
    x_directly = torch.tensor([5.5, 3])
    print(x_directly, "\n")

    # Get size:
    print("# x_zeros.size\n", x_zeros.size())
    print("# x_directly.size\n", x_directly.size())

    # ######## for DELIBERATELY Red test ########
    # print(null_function, "\n")


do_getting_started()


def do_operations():
    # Addition:
    y_rand = torch.rand(5, 3)
    print(x_rand + y_rand, "\n")
    print(torch.add(x_rand, y_rand), "\n")

    x_rand.add_(y_rand)
    print(x_rand, "\n")

    # Show like NumPy
    print(x_rand[:, 1], "\n")

    # Resizing
    x = torch.randn(4, 4)
    y = x.view(16)
    z = x.view(-1, 8)

    print(x.size(), y.size(), z.size(), "\n")

    a = torch.randn(1)
    print(a, "\n")
    print(a.item(), "\n")


do_operations()


def do_numpy_bridge():
    # Converting a Torch Tensor to a NumPy Array:
    a = torch.ones(5)
    print(a, "\n")

    a_numpy = a.numpy()
    print(a_numpy, "\n")

    b = a.add_(1)
    print(b, "\n", b.numpy(), "\n")

    # ######## for DELIBERATELY Red test ########
    # print(null_function, "\n")


do_numpy_bridge()
