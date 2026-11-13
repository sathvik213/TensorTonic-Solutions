import torch

def neuron_forward(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor) -> tuple:
    """
    Returns a tuple of scalar tensors: preactivation and tanh output.
    """
    output=torch.dot(inputs,weights)+bias
    return (output,torch.nn.Tanh()(output))
    # pass
