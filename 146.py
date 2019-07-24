n,m=map(int,input().split())
l=list(map(int,input().split()[:n]))
for i in l:
    if m==i:
        s=l.count(m)
        print("yes",s)
        exit()
