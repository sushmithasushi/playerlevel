xx=input()
x=list(xx)
l=[]
y=sorted(x)
for i in xx:
    l.append(xx.count(i))
for i in range(len(l)):
    if l[i]==min(l):
        print(x[i],end=" ")
