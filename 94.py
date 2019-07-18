n=int(input())
l=list(map(int,input().split()[:n]))
mm=[]
for i in range(n):
    for j in range(i+1,n):
       mm.append(l[i] | l[j])
print(max(mm))
