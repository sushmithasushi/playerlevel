s,m=map(str,input().split())
s=list(s)
m=int(m)
c=0
for i in range(m+1):
    if s.count(str(i))>=1:
        c+=1
if c==m+1:
    print("yes")
else:
    print("no")
    
