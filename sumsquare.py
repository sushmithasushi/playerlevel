a1=int(input())
b1=0
while(a1>0):
    p=a1%10
    a1=int(a1/10)
    b1+=p*p
print(b1)    
