n=int(input())
t=n
l=int(len(str(n)))
s=0
while n:
    rm=n%10
    s+=rm**l
    l-=1
    n//=10
if s==t:
    print("True")
else:
    print("False")
    