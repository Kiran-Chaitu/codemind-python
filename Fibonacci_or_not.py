n=int(input())
a,b=0,1
c=a+b
while a<=n:
    c=a+b
    if a==n:
        print("True")
        break
    a=b
    b=c
else:
    print("False")