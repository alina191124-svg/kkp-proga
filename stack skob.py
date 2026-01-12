s=input()
st=[]
p={'{':'}','[':']','(':')'}
flag=True
for i in s:
    if i in p.keys():
        st.append(i)
    elif i in p.values():
        if len(st)!=0:
            if i==p[st[len(st)-1]]:
                st.pop()
        else:
            flag=False
    else:
        flag=False
if len(st)==0 and flag:
    print('YES')
else:
    print('NO')