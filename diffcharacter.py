a,b=input().split()
counter = 0
differences = 0
for i in a:
    if i != b[counter]:
        differences += 1
    counter += 1
if(differences==1):
    print('yes')
else:
    print('no')
