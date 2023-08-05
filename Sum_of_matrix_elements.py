r=int(input())
c=int(input())
s=0
for i in range(r):
    v=list(map(int,input().split()))
    s+=sum(v)
print(s)
