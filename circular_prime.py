def is_prime(n):
    if n<=1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
if is_prime(n):
    if is_prime(int(str(n)[::-1])):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")