n=int(input())
for i in range(1,n):
    a=n//i
    if a%2==1:
        print(i)
        exit()
