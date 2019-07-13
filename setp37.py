x=int(input())
c=0
for i in range(x):
    aa,bb=map(int,input().split())
    if aa<bb:
        c+=1
print(c)
