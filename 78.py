nn,m=map(int,input().split())
l=list(map(int,input().split()[:nn]))
o=list(map(int,input().split()[:m]))
res=[]
res=l+o
res.sort()
for i in res:
    print(i,end=" ")
        

    
