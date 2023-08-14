t=int(input())
for k in range(t):
    s=input()
    l=[]
    for i in range(len(s)):
        l.append(int(s[i]))
    l.sort()
    for i in range(0,len(l)-1):
        if l[i]!=(l[i+1]-1):
            print("NO")
            break
    else:
        print("YES")