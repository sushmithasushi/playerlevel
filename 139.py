s=int(input())
l=list(map(int,input().split()))
m=0
l.sort()
if l[0]<0:
    m=l[0]
print(m)
