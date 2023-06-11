n=int(input())
for i in range(1,(n//2)+1):
    if i*(i+1)==n:
        print("YES")
        break
if i>=n//2:
    print("NO")