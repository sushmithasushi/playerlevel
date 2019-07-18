n=int(input())
l=list(map(int,input().split()[:n]))
mm=l[0]
for i in range(1,n):
       mm=mm | l[i] 
print(mm)
