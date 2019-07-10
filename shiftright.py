kvalue=list(map(int,input().split()))
mvalue=list(map(int,input().split()))
for l in range(0,kvalue[1]):
  mvalue=[mvalue[-1]] + mvalue[:-1]
print(*mvalue,end=' ')
