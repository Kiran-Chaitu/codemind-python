r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
se,so,k=0,0,1
for i in mat:
    if k%2==0:
        se+=(sum(i))
        k+=1
    else:
        so+=(sum(i))
        k+=1
print(so,se,end=' ')