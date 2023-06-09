def rev(n):
    revs=str(n)[::-1]
    revn=int(revs)
    return revn
n=int(input())
while(1):
    add=rev(n)
    x=n+add
    if(x==rev(x)):
        break
    else:
        n=x
print(x)
    