n=int(input())
l=list(map(int,input().split()[:n]))
i=60
c=0
for i in range(2,100000):
    c=0
    for j in range(n):
        if i%l[j]==0:
            c+=1
    if c==n:
        print(i)
        exit()
    
