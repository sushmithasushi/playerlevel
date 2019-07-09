a,b=input().split()
a=int(a)
b=int(b)
lists=[]
for i in range (a,b+1):
    j = 1;
    while j*j <= i:
        if j*j == i:
                lists.append(i)  
        j = j+1
    i = i+1
print(len(lists))
