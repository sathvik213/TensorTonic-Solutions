import torch

def tanh_forward_backward(x: torch.Tensor, upstream_gradient: torch.Tensor) -> tuple:
    """
    Returns a tuple of scalar tensors: tanh output and input gradient.
    """
    par=upstream_gradient*(1-torch.square(torch.nn.Tanh()(x)))
    return (torch.nn.Tanh()(x),par)