n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(1,k+1):
    a=l[n-1]
    for j in range(len(l)-1,0,-1):
        l[j]=l[j-1]
    l[0]=a
print(*l)
        