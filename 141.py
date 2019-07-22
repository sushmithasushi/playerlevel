s=input()
a=0
for i in s:
    if int(i)%2==1:
        a+=int(i)
if a%2==0:
    print("E")
else:
    print("O")
