nn=int(input())
ec=0
oc=0
inn=0
l=list(map(int,input().split()[:nn]))
for i in range(0,len(l)):
    if l[i]%2==0:
        ec+=1
        if ec==1:
            inn=i
    if l[i]%2==1:
        oc+=1
        if oc==1:
            inn=i
print(l[inn])    
        
        

    
