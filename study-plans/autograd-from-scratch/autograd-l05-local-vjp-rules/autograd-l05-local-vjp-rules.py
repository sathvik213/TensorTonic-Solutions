def local_vjp(operation: str, inputs: list, output: float, upstream_gradient: float) -> list:
    """
    Returns a list of float gradient contributions in input order.
    """
    upstream_gradient=float(upstream_gradient)
    # pass
    a=float(inputs[0])
    b=float(inputs[-1])
    if operation=='add':
        return [upstream_gradient,upstream_gradient]
    elif operation=='mul':
        return [b*upstream_gradient,a*upstream_gradient]
    elif operation=='tanh':
        return [upstream_gradient*(1-np.square(output))]

    
