a=input()
st=[]
c=0
for i in range(0,len(a)):
    if a[i]=="[" or a[i]=="{" or a[i]=="(":
        st.append(a[i])
    elif a[i]=="}":
        if "{" in st:
            st.remove("{")
        else :
            print("False")
            break
    elif a[i]=="]":
        if "[" in st:
            st.remove("[")
        else:
            print("False")
            break
    elif a[i]==")":
        if "(" in st:
            st.remove("(")
        else:
            print("False")
            break
else: print(st==[])