s=input()
if len(s)==10:
    if s[2] is '/' and s[5] is '/':
        dd=s[:2]
        mm=s[3:5]
        yy=s[6:]
    if int(dd)>=1 and int(dd)<=31 and int(mm)>=1 and int(mm)<=12:
        print("yes")
    else:
        print("no")
else:
    print("no")
