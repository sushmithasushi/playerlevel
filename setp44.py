l,s=input().split()
s=int(s)
l=list(l)
for i in range(s):
    l=list(l[-1])+list(l[:-1])
for i in range(len(l)):
    print(l[i],end="")
