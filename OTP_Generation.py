a=input()
s=""
l=[]
for i in range(0,len(a)):
    if int(a[i])%2!=0:
        l.append(int(a[i])*int(a[i]))
for i in l:
    s+=str(i)
print(s)