def rev(n):
    return int(str(n)[::-1])
n=int(input())
r=rev(n)
s1=n*n
s2=r*r
if s1==rev(s2):
    print("True")
else:
    print("False")