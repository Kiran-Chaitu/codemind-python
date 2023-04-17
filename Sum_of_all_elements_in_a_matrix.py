r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
s=0
for i in mat:
   s+=sum(i)
print(s)