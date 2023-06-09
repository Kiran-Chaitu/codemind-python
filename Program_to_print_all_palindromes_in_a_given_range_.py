def r(n):
    revs=str(n)[::-1]
    rev=int(revs)
    return rev
m=int(input())
n=int(input())
for i in range(m,n+1):
    if i==r(i):
        print(i,end=" ")