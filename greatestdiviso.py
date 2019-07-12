numa,numb=input().split()
numa=int(numa)
numb=int(numb)
c=0
for i in range(2,numb+1):
    if(numa%i==0 and numb%i==0):
         c=i
print(c)
