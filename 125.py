a,b=input().split()
l=len(a)
m=len(b)
res=""
if l==m:
    print(a,end="")
    print(b)
elif l>m:
    for i in range(m):
        res+=(a[i])
    print(res,end="")
    print(b)
else:
    for i in range(l):
        res+=(b[i])
    print(a,end="")
    print(res)
        
