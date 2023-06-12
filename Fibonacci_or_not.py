n=int(input())
i=1
a=0
b=1
while i<=n:
    c=a+b
    if a==n:
        print("True")
        break
    else:
        a=b
        b=c
    i+=1
if i>=n:
    print("False")