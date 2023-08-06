a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(b):
    t=l[0]
    for j in range(0,a-1):
        l[j]=l[j+1]
    l[a-1]=t
print(*l)