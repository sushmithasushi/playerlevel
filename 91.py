n=int(input())
l=list(map(int,input().split()[:n]))
le=[]
for i in range(n):
    for j in range(n):
        le.append(l[i]&l[j])
print(max(le))
