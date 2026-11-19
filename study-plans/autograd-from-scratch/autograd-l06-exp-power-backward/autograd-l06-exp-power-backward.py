import numpy as np

def exp_power_backward(x: float, exponent: float, upstream_gradient: float) -> tuple:
    """
    Returns a tuple of exp output, exp gradient, power output, and power gradient.
    """
    # pass
    y_exp=np.power(np.e,x)
    g_exp=upstream_gradient*y_exp
    if float(exponent)==0.0:
        y_power=1
        g_power=0
        return float(y_exp),float(g_exp),float(y_power),float(g_power)

    y_power=np.power(float(x),float(exponent))
    
    g_power=upstream_gradient*float(exponent)*np.power(float(x),float(exponent)-1)
    return float(y_exp),float(g_exp),float(y_power),float(g_power)
