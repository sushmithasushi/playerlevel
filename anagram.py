number=int(input())
cc=0
aa=[]
bb=['a','a','b','i','k','l']
for i in range(0,number):
    aa.append(list(input()))
for i in aa:
    s=sorted(i)
    if(bb==s):
        cc=cc+1
print(cc)
