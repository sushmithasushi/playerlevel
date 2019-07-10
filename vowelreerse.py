a=int(input())
vr=list(map(str,input()[:a]))
vowels=['a','e','i','o','u','A','E','I','O','U']
rr=[]
for i in vr:
   if i not in vowels:
      rr.append(i)
print(''.join(map(str,rr[::-1])))    
