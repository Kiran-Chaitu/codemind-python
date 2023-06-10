def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=a+b
while 1:
    c+=1
    if is_prime(c):
        break
print(c-a-b)