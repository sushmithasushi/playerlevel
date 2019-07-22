n,m=map(int,input().split())
l=list(map(int,input().split()[:n]))
res=[]
for i in l:
    if l.count(i)<m:
        res.append(i)
res.sort()
for i in res:
    print(i,end=" ")
