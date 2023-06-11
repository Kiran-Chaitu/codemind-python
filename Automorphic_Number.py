n=int(input())
d=int(len(str(n)))
rm=(n*n)%(10**d)
if rm==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")