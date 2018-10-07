import sys
import math
n=int(float(str(sys.argv[1])))
prime=True
for i in range (2, int(math.sqrt(n))):
    if n%i==0:
        prime=False
print n
print prime 
