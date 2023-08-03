a=input()
v=[]
for i in range(0,len(a)):
    if a[i] in "AEIOUaeiou":
        v.append(a[i])
n=[]
v.reverse()
k=0
for i in range(0,len(a)):
    if a[i] in "AEIOUaeiou":
        n.append(v[k])
        k+=1
    else:
        n.append(a[i])
c=""
for i in n:
    c+=i
print(c)