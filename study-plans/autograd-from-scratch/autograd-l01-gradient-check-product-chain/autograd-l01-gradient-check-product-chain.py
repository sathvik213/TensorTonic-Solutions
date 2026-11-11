import numpy as np

def gradient_check_product_chain(
    a: float,
    b: float,
    c: float,
    f: float,
    h: float,
) -> tuple[float, list, list, float]:
    """
    Returns loss, analytic gradients, numerical gradients, and maximum error.
    """
    e=float(a*b+c)
    ag_e_a=b
    ag_e_b=a
    ag_e_c=1
    ag_L_e=f
    ag_L_f=e

    loss=float(e*f)
    slope_a_h=((f*((a+h)*b+c))-loss)/h
    slope_b_h=((f*((b+h)*a+c))-loss)/h
    temp=c+h
    slope_c_h=((f*(a*b+temp))-loss)/h
    slope_f_h=((f+h)*e-loss)/h
    ana_g=[f*b,f*a,f,e]
    ana_g=np.array(ana_g,dtype=float)
    num_g=[slope_a_h,slope_b_h,slope_c_h,slope_f_h]
    return loss,ana_g.tolist(),(num_g),float(max([np.abs(xi - yi) for xi, yi in zip(ana_g, num_g)]))
