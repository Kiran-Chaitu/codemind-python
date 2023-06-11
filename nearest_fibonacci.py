n=int(input())
a=0
b=1
c=a+b
while (c<=n):
    c=a+b
    a=b
    b=c
if(b-n<n-a):
    print(b)
elif b-n==n-a:
    print(a,end=" ")
    print(b)
else:
    print(a)