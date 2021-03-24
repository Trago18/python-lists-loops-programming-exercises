import random

def matrixBuilder(num):
    d1 = []
    d2 = []
 
    for x in range(num):
        d1.append(1)

    for x in range(num):
        d2.append(d1)
    
    return(d2)

print(matrixBuilder(3))
