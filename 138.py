s=int(input())
l=list(map(int,input().split()))
m=1
for i in l:
    m*=i
if m%2==0:
    print("even")
else:
    print("odd")
