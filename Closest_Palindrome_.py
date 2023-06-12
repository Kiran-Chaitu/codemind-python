def rev(n):
    return int(str(n)[::-1])
def is_pal(n):
    if n==rev(n):
        return 1
    else:
        return 0
def pre(n):
    while is_pal(n)==0:
        n-=1
    return n
def next(n):
    while is_pal(n)==0:
        n+=1
    return n
n=int(input())
a=n-pre(n-1)
b=next(n+1)-n
if a<b:
    print(pre(n-1))
elif a==b:
    print(pre(n-1),next(n+1),end=" ")
else:
    print(next(n+1))