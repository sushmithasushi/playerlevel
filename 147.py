n=int(input())
l=(bin(n))
l=l[2:]
x=0
a=0
l=l[::-1]
for i in range(len(l)):
    if l[i]=='1':
        a=i
        break
print(a+1)
