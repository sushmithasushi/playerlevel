s=list(input().split())
a=s[0]
bb=s[1]
for i in a:
    if i in bb:
        print("yes")
        exit()
else:
    print(no)
