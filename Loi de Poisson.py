from math import exp
def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def loi_de_pison(k,n,p):
    proba=(exp(-n*p)) * ((n*p)**k)/factorielle(k)
    print(proba)

loi_de_pison(0,50,0.04)
