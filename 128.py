s=list(map(str,input().split()))
a=[]
for i in s:
    a.append(len(i))
inn=a.index(max(a))
print(s[inn])
