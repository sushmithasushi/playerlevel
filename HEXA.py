try:
    a1=input()
    a1=int(a1,16)
    a1=str(a1)
    if a1.isnumeric()==True:
        print('yes')
except:
    print('no')
