nn=int(input())
l=list(map(int,input().split()[:nn]))
m=1
for i in range(len(l)):
    for j in range(i+1,len(l)):
        d=abs(l[i]-l[j])
        if d<m and d!=0:
            m=d
print(m)
