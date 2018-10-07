import sys
import math
def factor(n):
    if n==1:
        return []
    factors=[]
    i=1
    while i < n+1:
        i+=1
        if n%i==0:
            factors.append(i)
            factors= factors +(factor(n/i))
            return factors
