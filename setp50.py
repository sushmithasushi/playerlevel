n=int(input())
f=0
for i in range(1,n):
    if n%i==0:
        f=1
        break
if f==1:
    print("yes")
else:
    print("no")
