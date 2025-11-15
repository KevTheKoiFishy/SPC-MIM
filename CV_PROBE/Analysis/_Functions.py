from _Constants import *

def format_suffix(f) -> str:
    """
    Replaces 1000 with k, 0.001 with m, etc.
    ie. Scientific Notation in steps of 10^3.
    """

    if f == 0:
        return f"{0.0:8.2f}  "
    
    if f <= 1:
        suffix = " munpf"
        i = 0
        while f < 1:
            f *= 1e3
            i += 1
        
        return f"{f:8.2f} {suffix[i]}"

    if f >= 1:
        suffix = " KMGTPE"
        i = 0
        while f >= 1e3:
            f *= 1e-3
            i += 1
        
        return f"{f:8.2f} {suffix[i]}"
    
    # f was not a number
    return f"{0.0:8.2f}  "

def get_expected_Cp_by_Diameter(eps_r):
    return dict(zip(list(D), EPS_0 * eps_r * A / S))

def get_expected_Gp_by_Diameter(sigma):
    return dict(zip(list(D), sigma * A / S))