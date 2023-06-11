def is_prime(n):
    if n<=1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
def pre_prime(n):
    while(is_prime(n)==0):
        n-=1
    return n
def next_prime(n):
    while(is_prime(n)==0):
        n+=1
    return n
t=int(input())
for i in range(1,t+1):
    n=int(input())
    a=n-pre_prime(n)
    b=next_prime(n)-n
    if a<b:
        print(pre_prime(n))
    elif a==b:
        print(pre_prime(n))
    else:
        print(next_prime(n))
    