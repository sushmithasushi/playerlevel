inptt1=input()
i2=''
i3='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in inptt1:
    if i in i3:
        inpt4=i3.index(i)
        inpt4=inpt4+3
        i2=i2+i3[inpt4]
print(i2)
