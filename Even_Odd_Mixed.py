n=int(input())
c1,c2=0,0
while n:
    rm=n%10
    if rm%2==0:
        c1+=1
    else:
        c2+=1
    n=n//10
if c1==0:
    print("Odd")
elif c2==0:
    print("Even")
else :
    print("Mixed")