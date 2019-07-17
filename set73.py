n=int(input())
a=list(map(int,input().split()[:n]))
bb=list(map(int,input().split()[:n]))
for i in a:
    if i in bb:
        print(i,end=" ")

