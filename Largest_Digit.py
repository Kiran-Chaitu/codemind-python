n=int(input())
max=0
while(n):
    rm=n%10
    if max<(rm):
        max=rm
    n//=10
print(max)