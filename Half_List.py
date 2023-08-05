n=int(input())
l=list(map(int,input().split()))
v=[]
for i in range(n-1,(n//2)-1,-1):
    v.append(l[i])
for i in range(0,n//2):
    if l[i] not in v:
        v.append(l[i])
print(*v)