nn=int(input())
l=list(map(int,input().split()[:nn]))
m=0
res=0
c=0
for i in range(0,len(l)-1):
    if l[i]<l[i+1]:
        c+=1
        res=c
    elif c>m:
        m=c
        res=c
        c=0
print(res+1)
        
        

    
