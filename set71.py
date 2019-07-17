a=list(map(int,input().split()))
bb=list(map(int,input().split()[:a[0]]))
for i in range(a[0]):
    for j in range(i+1,a[0]):
        if bb[i]+bb[j]==a[1]:
            print("yes")
            exit()
else:
    print("no")
