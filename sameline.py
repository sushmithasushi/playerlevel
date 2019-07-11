num1=input().split()
n2=input().split()
n3=input().split()
if(num1[0]==n2[0]==n3[0] or num1[1]==n2[1]==n3[1] or (num1[0]==num1[1] and n2[0]==n2[1] and n3[0]==n3[1])):
    print('yes')
else:
    print('no')
