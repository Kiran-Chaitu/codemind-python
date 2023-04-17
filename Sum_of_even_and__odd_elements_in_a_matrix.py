r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
se,so=0,0
for i in range(r):
    for j in range(c):
        if (mat[i][j])%2==0:
            se+=mat[i][j]
        else:
            so+=mat[i][j]
print(se,so,end=' ')