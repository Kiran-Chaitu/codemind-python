t=int(input())
for i in range(t):
    k=input()
    c=0
    for j in range(0,len(k)):
       if (k[j]).isdigit():
           c+=1
    if c==len(k):
        print(True)
    else:
        print(False)