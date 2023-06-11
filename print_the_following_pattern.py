n=int(input())
for i in range(1,n):
    for j in range(1,i+1):
        if i==j or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,n+1):
    print("*",end="")