
def matrixBuilder(num):
    d1 = []
    for x in range(num):
        d2 = []
        for x in range(num):
            d2.append(1)
        d1.append(d2)
    return(d1)

print(matrixBuilder(3))
