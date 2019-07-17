nn=int(input())
l=list(map(int,input().split()[:nn]))
d=0
m=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        d=abs(l[i]-l[j])
        if d>m:
            m=d
print(m)

    
