def retrocontador(e):
    if e>0:
        print("{}\t".format(e), end ="")
        retrocontador(e-1)
    return None


def sumatorio(n):
    resultado =n
    if n >0:
         resultado += sumatorio(n-1)
    return resultado

retrocontador (10)
sumRec = sumatorio(10)
print("\n")
print (sumRec)
