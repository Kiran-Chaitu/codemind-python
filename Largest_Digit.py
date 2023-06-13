n=int(input())
l=[]
while n:
    rm=n%10
    l.append(rm)
    n//=10
print(max(l))