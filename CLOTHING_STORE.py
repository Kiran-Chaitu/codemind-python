from math import*
n=int(input())
li=list(map(int,input().split()))
li.sort()
c=0
for i in range(0,n-1):
    if li[i]==li[i+1] and li[i]!=-1:
        c+=1
        li[i+1]=-1
print(ceil(c))