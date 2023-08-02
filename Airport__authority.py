n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
t=int(input())
s=0
for i in range(0,n):
    if l[i]<=t:
        s+=1
    else:
        s+=2
print(s)