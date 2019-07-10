k1,k2=map(int,input().split())
for j in range(1,100000):
   if(j%k1==0 and j%k2==0):
      print(j)
      break
