x=int(input())
c=0
y=[]
ll=list(map(int,input().split()))
for i in ll:
    y.append(i)
ll.sort()
for i in range(len(ll)):
    if ll[i]==y[i]:
        c+=1
if c==len(y):
    print("yes")
else:
    print("no")
