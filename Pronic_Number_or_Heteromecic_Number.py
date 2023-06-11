n=int(input())
i=1
while i<= n//2:
    if i*(i+1)==n:
        print("YES")
        break
    i+=1
if i>=n//2:
    print("NO")