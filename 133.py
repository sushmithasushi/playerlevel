n=int(input())
res=[]
for i in range(2,n):
    if n%i==0:
        c=0
        a=i
        for j in range(2,a):
            if a%j==0:
                c+=1
        if c==0:
            res.append(i)
for i in res:
    print(i,end=" ")
                
            
