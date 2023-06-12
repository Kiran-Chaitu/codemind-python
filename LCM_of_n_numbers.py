n=int(input())
l=list(map(int,input().split()))
la=max(l)
c=0
m=la
while 1:
    c=0
    for i in range(0,n):
        if m%l[i]==0:
            c+=1
    if c==n:
        break
    else :
        m+=la
print(m)