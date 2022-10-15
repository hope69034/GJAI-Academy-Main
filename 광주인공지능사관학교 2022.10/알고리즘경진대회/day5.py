[5일차]

2 숫자퍼즐 100점

from itertools import product
al=[4,7]
K=input()
a=True
def ss():
    count=0
    for i in  range(1,int(K)+1):
        for j in product(al, repeat=i):
            #print(j)
            count+=1
            if count==int(K):
                st=''
                for tt in j:
                    st += str(tt)
                return st
print(ss())

3 분수의덧셈 100점

import fractions
a,b=map(int, input().split())
c,d=map(int,input().split())
aa= a*d+c*b  
dd= d*b   
dddd= fractions.Fraction(aa,dd)
print(f'{dddd.numerator} {dddd.denominator}')

4 수학자도도새  100점

def number(x):
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True # 소수
n=input()
nn=int(n)
a, b = 2, nn-2
while True:
    if number(a)  and number(b) :
        print(f'{nn} = {a} + {b}')
        break
    else:
        a += 1
        b -= 1

7 알고리즘게임구슬게임   80 점

a=input()
if a%4 == 0 :
    print('DODO')
else:
    print('ELICE')

9 직사각형 만들기  60점

import math
a=input()
aa=int(a)
count=0
for i in range(1,aa+1):
    if i == 1 : #예외
        count+=1
    elif i == 2 : #예외
        count+=1
    elif i == 4 : #예외
        count+=2
    else:
        if i % 2 ==0 : #짝수면2
            count+=2
            if (math.sqrt(i)).is_integer() : # 제곱수라면+1 을한다 제곱근이 소수가 아니라면 TRUE반환
                count+=1
        elif i % 2 ==1: #홀수면1
            count+=1
            if (math.sqrt(i)).is_integer() : # 제곱수라면+1 을한다 제곱근이 소수가 아니라면 TRUE반환
                count+=1
print(count)

10 단짠이최고야  80점

nl=[]
n=input()
nn=int(n)
num=0
count=0
a=0
b=0
res=0
for i in range(nn):
    tt = list(map(int,input().split()))
    if count==0:
        num = (max(tt)-min(tt))
        count+=1
        res=num
        a,b = tt[0] ,    tt[1]
    else:
        a=a*tt[0]
        b=b*tt[1]
        if b > a:
            if (b-a) < res:
                res = b-a
        elif a > b:
            if (b-a) < res:
                res = a-b
print(res)