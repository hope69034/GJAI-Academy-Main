[1일차]

1번  잔돈 가득한 세상  100점

N=int(input())
s2=10000-N   
slist= [10000,1000,100,10,1]
count=0
for i in range(len(slist)):
    if s2 != 10000:
        while True:    
            if s2 >= slist[i]:
                s2-= slist[i]
                count+=1
            else:
                break
print(count)

2번 복권 60점 (1개시간초과 1개오답)

import itertools
N=int(input())
n=input() 
nprl=[]
rr=""
try:
    Nl=[]
    for i in range(1,N+1):
        Nl.append(str(i))
    nPr = itertools.permutations(Nl, N)
    for i in nPr:
        nprl.append(i)  
    for j,i in enumerate(nprl):
        str = ' '.join(i)
        if str == n :
            res=nprl[j+1]
    for i in res:
        rr+=i + " "
    print(rr)
except:
    print(-1)

3번 3살엘리스토끼 100점

from string import ascii_lowercase as low_alpha
counts = [0 for _ in range(len(low_alpha))]
alphabet = dict(zip(list(low_alpha), counts))
for s in input():
    alphabet[s] += 1
print(*alphabet.values())

4번 계기판조작하기  80점

n=input().split()
a=n[0]
b=n[1]
c=True
tt=[]
while c:
    a=int(a)+1               #     a=1001
    #인트a무한1증가
    for i in str(a):              
        tt.append(i)          #   i=    1 0 0 1     4개들어감
    if int(b) == len(set(tt)) :  # a에 +1이 몇종인지 
        print(a)
        break
    else:
        tt=[] 
        
6번 익숨함에속아   0점 (all시간초과)

N=input().split()
nn=[]
sr=""
for i in N:
    nn.append(int(i)) 
for i in range(len(nn)-1):
    for j in range(len(nn)-1-i):
        if nn[j] > nn[j+1]:
            nn[j], nn[j+1] = nn[j+1], nn[j]
for i in nn:
    sr+=str(i)+" "
print(sr)

7번 골칫거리버그 100점

import re
word = input()
bug = input()
while bug in word:
    word = re.sub(bug,'',word)
print(word)

8번 숫자놀이 40점  (3개오답)

A=int(input())
B=int(input())
import math
res=[]
if A%2==0 : #짝수자릿수면     # A는2이상
    for i in range(1,10):  # 1부터9까지 첫자릿수 int
        if i+B < 10 : 
            ns = str(i)+str(i+B)
            res.append(ns*int(A/2))
        elif (i-B) == 0 :
            ns = str(i)+str(0)
            res.append(ns*int(A/2))
        elif (i-B) > 0 :
            ns = str(i)+str(i-B)
            res.append(ns*int(A/2))  
elif A==9:
    for i in range(1,10):  # 1부터9까지 첫자릿수 int
        if i+B < 10 : 
            ns = str(i) 
            ns2 = str(i+B)+str(i) 
            ns3 = ns+ns2 * (math.ceil(A/3)+1)  
            res.append(ns3)
        elif (i-B) == 0 :
            ns = str(i)
            ns2 = str(0)+str(i)
            ns3 = ns+ns2 * (math.ceil(A/3)+1)
            res.append(ns3)
        elif (i-B) > 0 :
            ns = str(i)
            ns2 = str(i-B)+str(i)
            ns3 = ns+ns2 * (math.ceil(A/3)+1)
            res.append(ns3)
elif  (A%2) == 1 : #홀수자릿수면  # A는2이상 = 3부터
    for i in range(1,10):  # 1부터9까지 첫자릿수 int
        if i+B < 10 : 
            ns = str(i) 
            ns2 = str(i+B)+str(i) 
            ns3 = ns+ns2 * math.ceil(A/3)  
            res.append(ns3)
        elif (i-B) == 0 :
            ns = str(i)
            ns2 = str(0)+str(i)
            ns3 = ns+ns2 * math.ceil(A/3) 
            res.append(ns3)
        elif (i-B) > 0 :
            ns = str(i)
            ns2 = str(i-B)+str(i)
            ns3 = ns+ns2 * math.ceil(A/3) 
            res.append(ns3)
result=""
for i in res:
    result+=i+" "
print(result[0:-1])