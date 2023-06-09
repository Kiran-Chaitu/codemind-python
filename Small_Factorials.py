n=int(input())
i=1
while i<=n:
    a=int(input())
    f=1
    while a!=1:
       f=f*a
       a-=1
    print(f)
    i+=1