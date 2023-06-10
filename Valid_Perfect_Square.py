import math
t=int(input())
i=1
while i<=t:
    n=int(input())
    sq=float(n**0.5)
    dp="{:.1f}".format(sq-int(sq))
    if dp=="0.0":
        print("True")
    else:
        print("False")
    i+=1