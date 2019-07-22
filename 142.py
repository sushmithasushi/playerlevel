s=input()
l=list(s)
res=[]
c=0
for i in range(len(l)-1):
    if (int(l[i])+int(l[i+1]))%2!=0:
        c+=1
    else:
        res.append(c)
        c=0
    res.append(c)
a=max(res)
if a==0:
    print(a)
else:
    print(a+1)
        
        
