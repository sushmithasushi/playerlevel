n=int(input())
l=list(map(int,input().split()[:n]))
l.sort()
s=l[0]
for i in range(1,s+1):
    c=0
    for j in range(n):
        if l[j]%i==0:
            c+=1
    if c==n:
        s=i
print(s)
