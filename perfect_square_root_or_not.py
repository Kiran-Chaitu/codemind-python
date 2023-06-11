n=int(input())
sq=n**0.5
f="{:.2f}".format(sq-int(sq))
if f=="0.00":
    print("True")
else:
    print("False")