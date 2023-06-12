a,b=map(int,input().split())
if a<b:
    min=a
    max=b
else:
    min=b
    max=a
i=max
while 1:
    if max%min==0:
        lcm=max
        break
    else:
        max+=i
print((a*b)//lcm)