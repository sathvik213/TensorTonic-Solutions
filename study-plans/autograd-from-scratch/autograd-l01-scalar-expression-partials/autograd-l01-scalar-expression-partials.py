def scalar_expression_partials(a: float, b: float, c: float, h: float) -> tuple[float, float, float, float]:
    """
    Returns the expression value and numerical partials for a, b, and c.
    """
    func_abc=float(a*b+c)
    func_a_h=(a+h)*b+c
    func_b_h=(a)*(h+b)+c
    temp=c+h
    func_c_h=a*b+temp
    num_par_a=(func_a_h-func_abc)/h
    num_par_b=(func_b_h-func_abc)/h
    num_par_c=(func_c_h-func_abc)/h

    
    return func_abc,num_par_a,num_par_b,num_par_c