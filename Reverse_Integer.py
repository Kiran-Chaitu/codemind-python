def rev(n):
     return int(str(n)[::-1])
n=int(input())
t=n
if n<0:
     r=rev(-n)
else:
    r=rev(n)
if t<0:
    print(-r)
else:
    print(r)