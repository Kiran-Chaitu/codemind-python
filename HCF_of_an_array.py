n=int(input())
l=list(map(int,input().split()))
c=0
m=min(l)
while(1):
    c=0
    for i in range(0,n):
        if l[i]%m==0:
            c+=1
    if c==n:
        break
    else:
        m-=1
print(m)