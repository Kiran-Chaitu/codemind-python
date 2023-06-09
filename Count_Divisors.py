a,b,c=map(int,input().split())
c1=0
for i in range(a,b+1):
    if i%c==0:
        c1+=1
print(c1)