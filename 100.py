import math
m,n=map(int,input().split())
l=math.factorial(m)
a=math.factorial(m-n)
ss=math.factorial(n)
s=a*ss
print(int(l/s))
