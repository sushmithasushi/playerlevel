
xx,y=map(int,input().split())
f=0
for i in range(xx):
    if y**i==xx:
        f=1
        break
if f==1:
    print("yes")
else:
    print("no")
        
