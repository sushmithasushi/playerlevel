n=int(input())
l=list(map(int,input().split()[:n]))
f=0
for i in l:
    if l.count(i)>1:
        f=1
        break
if f==1:
    print("yes")
else:
    print("no")
