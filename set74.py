n,m=map(int,input().split())
l=list(map(int,input().split()[:n]))
l.sort()
for i in l:
    if i<m:
        print(i,end=" ")
