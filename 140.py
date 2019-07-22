s=int(input())
l=list(map(int,input().split()))
for i in range(s):
    a=0
    for j in range(i+1):
        a+=l[j]
    if a%2==0:
        print(a,end=" ")
    else:
        print(l[i])
