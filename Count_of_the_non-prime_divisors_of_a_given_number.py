def p(n):
    if n<=1:
        return False
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            return False
    return True
n=int(input())
c1=0
c2=0
for i in range(1,n+1):
    
    if n%i==0:
        c2+=1
        if p(i):
            c1+=1
print(c2-c1)