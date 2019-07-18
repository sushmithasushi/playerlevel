import math
m,n=map(int,input().split())
l=math.factorial(m)
a=math.factorial(m-n)
print(int(l/a))
