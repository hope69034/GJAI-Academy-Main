[4일차]

1 생수통 100점

abc=[]
de=[]
for i in range(3):
    abc.append(int(input()))
for i in range(2):
    de.append(int(input()))    
print(min(abc)+min(de)+10)

3 수학 못하면될떄까지  100점

s=input()
ss=int(s)
num=0
count=0
for i in range(1,ss+1):
    num+=i
    count+=1
    if ss <= num:
        break
if num == 1 :
    print(count)
elif  ss == num:
    print(count)
else:    
    print(count-1)

6번 수학 버스 100점

a,b= map(int,input().split())
for i in range(max(a,b),(a*b)+1):
    if i%a ==0 and i%b==0:
        print(i)
        break

9번 목표량 80점

a=input()
b=list(map(int,a))
from itertools import permutations
dd=list(permutations(b, len(b)))
dl=''
if len(a) >= 2:
    for i in dd[1]:
        dl+=str(i)
    print(dl)
else:
    if a=='1':
        print(1)
    else:
        print(dd[0][0])