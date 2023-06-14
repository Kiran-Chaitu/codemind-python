n=input()
l=list(n)
s=set(n)
if len(l)==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")