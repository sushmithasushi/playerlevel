n=int(input())
l=list(map(int,input().split()[:n]))
if n%2==1:
    a=(n-2)//2
else:
    a=(n-1)//2
l1=l[:a+1]
l2=l[a+1:n]
l1.sort()
l2=sorted(l2,reverse=True)
l=l1+l2
for i in l:
    print(i,end=" ")
