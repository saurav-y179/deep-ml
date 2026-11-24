import numpy as np 
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    an  = np.array(a)
    bn = np.array(b)
    if len(an[0]) != len(bn):
        return -1 
    else:
        c  = an@bn
        return c 
        
    
    
    