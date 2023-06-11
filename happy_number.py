n=int(input())
s=0
while 1:
    while n:
        rm=n%10
        s+=rm*rm
        n//=10
    if s<10:
        break
    else:
        n=s
        s=0
if s==1 or s==7:
    print("True")
else:
    print("False")