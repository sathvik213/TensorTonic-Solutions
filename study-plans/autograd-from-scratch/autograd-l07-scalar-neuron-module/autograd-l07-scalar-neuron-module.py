import torch

def scalar_neuron_module(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor, nonlinear: bool) -> torch.Tensor:
    """
    Returns a scalar tensor preserving the input dtype and device.
    """
    # pass
    
# if inputs and weights:
    prod = torch.sum(inputs*weights)
    result=bias+prod
    # result=float(result)
    # return result
    if not nonlinear:
        return result
    else:
        return torch.tanh(result)
    # else:
    #     return torch.tensor(bias)
