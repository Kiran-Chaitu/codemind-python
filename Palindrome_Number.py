def rev(n):
    return int(str(n)[::-1])
t=int(input())
i=1
while i<=t:
    n=int(input())
    if n==rev(n):
        print("True")
    else:
        print("False")
    i+=1
    