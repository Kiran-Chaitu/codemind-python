n=int(input())
for i in range(64+n,64,-1):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()