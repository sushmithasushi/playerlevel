l,s=input().split()
s=int(s)
for i in range(s):
    l=[l[-1]+l[:-1]]
for i in range(len(l)):
    print(l[i],end="")
    
