n=int(input())
l=int(len(str(n)))
sq=n*n
r=sq%(10**l)
if r==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")