r=int(input())
c=int(input())
l=[]
a=[]
for i in range(0,r):
    v=list(map(int,input().split()))
    a.append(sum(v))
    l.append(v)
print(sum(a))
    