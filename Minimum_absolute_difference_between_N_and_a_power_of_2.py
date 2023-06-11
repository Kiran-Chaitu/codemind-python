import math
n=int(input())
l=2**math.floor(math.log2(n))
r=2*l
if(n-l<r-n):
    print(n-l)
else:
    print(r-n)