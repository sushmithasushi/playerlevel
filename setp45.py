l,s=map(int,input().split())
l=l/2
f=0
for i in range(max(l,s)):
    for j in range(max(l,s)):
        if i+j==l and i*j==s:
            f=1
            break
if f==1:
    print("yes")
else:
    print("no")
    
