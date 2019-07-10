qw=int(input())
ss=list(map(int,input().split()[:qw]))
count=0
for j in range(0,qw+1):
   if(ss.count(j)==1):
      print(j)
