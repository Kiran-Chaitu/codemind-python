n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
m=0
for i in range(0,n):
    c=1
    if l[i]==-1:
        continue
    else:
        for j in range(i+1,n):
            if l[i]==l[j] and l[j]!=-1:
                c+=1
                l[j]=-1
    if c==k:
        a.append(l[i])
        m+=1
if m>0:
    print(*a)
else:
    print(-1)
        