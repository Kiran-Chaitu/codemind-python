t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    for a in range(1,n+1):
        c=0
        for b in l:
            if b==a:
                c+=1
                break
        if c==0:
            print(a)
            break