n=int(input())
t=n
l=len(str(n))
s=0
while n:
    rm=n%10
    s+=rm**l
    n//=10
    l-=1
if s==t:
    print("True")
else:
    print("False")