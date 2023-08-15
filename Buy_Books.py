n=int(input())
m=list(map(int,input().split()))
b=list(map(int,input().split()))
s=sum(b)-sum(m)
if s>0:
    print(s)
else :
    print(0)