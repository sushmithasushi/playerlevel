a,b,k=input().split()
k=int(k)
counter = 0
differences = 0
for i in a:
    if i != b[counter]:
        differences += 1
    counter += 1
if(differences==k):
    print('yes')
else:
    print('no')
