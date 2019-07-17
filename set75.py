n,m=map(int,input().split())
l=list(map(int,input().split()[:n]))
l.sort()
for i in l:
    if l.count(i)==m:
        print(i)
        exit()
