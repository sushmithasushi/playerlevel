inptt1=input()
inpt2=''
inpt3='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in inptt1:
    if i in inpt3:
        inpt4=inpt3.index(i)
        inpt4=inpt4+3
        inpt2=inpt2+inpt3[inpt4]
print(inpt2)
