def is_prime(num):
    if num<=1:
        return False;
    for j in range(2,int(num**0.5)+1):
        if num%j==0:
            return False;
    return True;
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
   if is_prime(i):
       c+=1
print(c)
    