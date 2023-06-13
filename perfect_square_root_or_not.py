n=int(input())
s=n**0.5
k="{:.2f}".format(s-int(s))
if k=="0.00":
    print("True")
else:
    print("False")