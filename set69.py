a=int(input())
s=""
b=list(map(int,input().split()[:a]))
c=0
for i in range(len(b)):
    if b[i]==0:
        for j in range(c,i):
            if b[j]==1:
                s+=str(b[j])
                c=i
for i in s:
    print(i,end=" ")
