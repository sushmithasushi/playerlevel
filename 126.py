n=int(input())
l=list(map(int,input().split()))
a=set(l)
a=list(a)
a.sort()
a=a[::-1]
res=[]
print(a)
for i in a:
    x=l.count(i)
    res.append(x)
print(res)
for i in range(len(res)):
    inn=res.index(max(res))
    res.remove(res[inn])
    a.remove(a[inn])

