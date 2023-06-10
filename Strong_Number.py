n=int(input())
t=n
s,fs=1,0
while n:
    s=1
    rm=n%10
    while (rm)>1:
        s*=rm
        rm-=1
    fs+=s
    n//=10
if fs==t:
    print(f"The number {t} is a strong number")
else:
    print(f"The number {t} is not a strong number")
    