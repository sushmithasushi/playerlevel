n,m=map(int,input().split())
f=0
for i in range(n):
    aa,b=map(int,input().split())
    if b>=m:
        f=1
if f==1:
    print("yes")
else:
    print("no")
