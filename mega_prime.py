import math
def is_prime(n):
    if n<=1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
d=int(len(str(n)))
c=0
if is_prime(n):
    while n:
        rm=n%10
        if is_prime(rm):
            c+=1
        n//=10
    if c==d:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")