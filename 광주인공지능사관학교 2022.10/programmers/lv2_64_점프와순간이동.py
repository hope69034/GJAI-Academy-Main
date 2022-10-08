프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/12980



# 첫1칸 점프 -필수
# *2 순간이동 
# 최대 소모 건전지는 전부 점프
# def solution(n):
# 
# argument: n 만큼 떨어진 장소
# 최소 건전지 소모량 솔루션 s = ?
# 최대 건전지 소모량 = n

ex

n=1 일 때
j=1 점프 1번 = 정답
t=0 텔레포트 0번

n=2  
j=1
t=1  

n=3  
j=2
t=1  

n=4  
j=1
t=2

n=5  
j=2
t=2

n=6  
j=2
t=2

    정답
거리  점프 텔레포트
    n   j   t   2제곱    n&j
    1   1   0   0       
    2   1   1   1 
    3   2   1   1   
    4   1   2   2
    5   2   2   2   
    6   2   2   2  
    7   3   2   2
    8   1   3   3

규칙1 : 텔레포트는 - 2제곱  > code   2의 t승과  






    정답
거리  점프 텔레포트
    n   j   t   2제곱    n&j
    1   1   0   0       
    2   1   1   1 
    3   2   1   1   
    4   1   2   2
    5   2   2   2
    6   2   2   2
    7   3   2   2
    8   1   3   3
    9
5000   5   12   12   
    
5000   5    t    ? 5000 은 2의 t승과 같거나 2의 t+1승보다 작다 

    
    
규칙1 : n 은  2의 t승 이상 ~ 2의 t+1승 미만이다  
            즉 n을 알면 t를 알 수 있다.
                n은 2의 t승이거나 t.x승이다

규칙1코드화 
import math
print(int(math.log2(5000)))
    2의 t.x승이 n 일 때 t.x에 인트를 걸어서 소수점을 제거
정리
import math
int(math.log2(n))   이것으로 t를 구했다
    
    


=============



거리  점프 텔레포트
    n   j   t    j&t    n&j
    1   1   0          
    2   1   1    
    3   2   1      
    4   1   2   
    5   2   2   
    6   2   2   
    7   3   2   
    8   1   3   
    9
5000   5   12   



n이랑 t를 아니까
j&t  의 관계를 알면 답을 알 수 있다
n j t의 관계


n=아규먼트로 선언
t=int(math.log2(n))
j= 정답찾기
num=현재위치

t 텔레포트는 기존 넘버에서 곱하기2

현재 위치를 num으로 설정



=====================
=====================
=====================
=====================
=====================
=====================
=====================




n=6
t=int(math.log2(6))  =2
num=0
j= 2가 나와야함

조건1 : num=n  같을 때까지 무한 루프
    코드화
        while num!=n:    n과넘이 같으면 루프 스탑
        

조건2 : num에다  t만큼 2를 곱해야함
    코드화
        for i in range(1,t+1):  # t번 만큼 반복  # 즉 1부터 t까지 i로 들어감
            num *= 2  # t번만큼 2를 곱함

조건3 : num 에 +1로 시작함
    코드화
        num += 1   # 시작 1번
        
#조건4 : 점프를 몇번하는지 카운트
 #   코드화
  #      jcount = 0
   #     jcount += 1  # 점프1번마다 점프 카운트

조건5 : 점프의 횟수
    방법1 j에 0 부터 ~ 넣어봐서 맞는지 틀린지 검사하다가 맞으면 브레이크
        코드화
            j의 최댓값은? : 일단 n을 넘을 수는 없다 n
            for j in range(1,n+1):    로   j에 0부터 n까지 넣어준다

조건6 : 점프와 텔레포트의 분배 방법
    n j t 가 모두 정해졌으니까 > 분배 방법은 ?  
        n=6     t=2      j 는 1,2 3 4 5 6 까지 넣어주는데 분배 방법은?  ( 마지막에 return j로 정답값 )
    
??????????





ex)
n=6 j=1 t=2    num=1 에서 6까지
에서 다음루프로



ex)
n=6 j=2 t=2
에서 break






ex)
n=6 j=1 t=2    num=1 에서 6까지
에서 다음루프로

n=6
j=1
t=2
num=1
while num!=n :    
    
    넘에 +1알 한번하고 곱하기2를 두번 해야함
    
    순열로 보면 3가지 경우의 수
    
    를 체크하며 맞는지 확인
    
    
순열 예시코드  순열 순서를 고려한 뽑기  

import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))
결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

j 는 1 t =2 일 때
j1 t1 t2 를 순열로 뽑기

import itertools
arr = ['j1', 't1', 't1']
lenarr = len(arr)     
nPr = itertools.permutations(arr, lenarr )   
print(list(nPr))

을 하면

[('j1', 't1', 't2'), 
 ('j1', 't2', 't1'), 
 ('t1', 'j1', 't2'), 
 ('t2', 'j1', 't1'), 
 ('t1', 't2', 'j1'), 
 ('t2', 't1', 'j1')]
 
 
#중복제거하는 코드필요
ll=[]
for i in list(nPr):
    #print(i)
    ll.append(i)
print(set(ll))

결과 
{('j1', 't1', 't1'), ('t1', 't1', 'j1'), ('t1', 'j1', 't1')}

중복제거완성

셋에서 리스트로?

=====================
셋에서 리스트로 일단 바꿔놓기



ll=[]
for i in list(nPr):
    #print(i)
    ll.append(i)
print(set(ll))
print(list(set(ll)))

결과
[('t1', 'j1', 't1'), ('t1', 't1', 'j1'), ('j1', 't1', 't1')]
리스트로 순서 뽑아줌














================================================================================
다시 정리





=====================
=====================




n=6
t=int(math.log2(6))  =2
num=0
j= 2가 나와야함

조건1 : num=n  같을 때까지 무한 루프
    코드화
        while num!=n:    n과넘이 같으면 루프 스탑
        

조건2 : num에다  t만큼 2를 곱해야함
    코드화
        for i in range(1,t+1):  # t번 만큼 반복  # 즉 1부터 t까지 i로 들어감
            num *= 2  # t번만큼 2를 곱함

조건3 : num 에 +1로 시작함
    코드화
        num += 1   # 시작 1번
        
#조건4 : 점프를 몇번하는지 카운트
 #   코드화
  #      jcount = 0
   #     jcount += 1  # 점프1번마다 점프 카운트

조건5 : 점프의 횟수
    방법1 j에 0 부터 ~ 넣어봐서 맞는지 틀린지 검사하다가 맞으면 브레이크
        코드화
            j의 최댓값은? : 일단 n을 넘을 수는 없다 n
            for j in range(1,n+1):    로   j에 0부터 n까지 넣어준다

조건6 : 점프와 텔레포트의 분배 방법
    n j t 가 모두 정해졌으니까 > 분배 방법은 ?  
        n=6     t=2      j 는 1,2 3 4 5 6 까지 넣어주는데 분배 방법은?  ( 마지막에 return j로 정답값 )
    

import itertools
arr = ['j1', 't1', 't1']
lenarr = len(arr)     
nPr = itertools.permutations(arr, lenarr )   
print(list(nPr))

ll=[]
for i in list(nPr):
    #print(i)
    ll.append(i)
print(set(ll))
print(list(set(ll)))

결과
[('t1', 'j1', 't1'), ('t1', 't1', 'j1'), ('j1', 't1', 't1')]
리스트로 순서 뽑아줌


조건6-2   arr에서 점프랑 텔레포트 리스트로 뽑아주기

점프랑 텔레포트가 주어졌을 때
그 수만큼 리스트에 넣어줌 순서 상관 없음

arrlist = []
arrlist.append()


j가 2면 j를 두번 어펜드

for i in range(j):
    arrlist.append(j)
for i in range(t):
    arrlist.append(t)


j=2
t=3
arrlist=[]
for i in range(j):
    arrlist.append(j)
for i in range(t):
    arrlist.append(t)
print(arrlist)
결과 [2, 2, 3, 3, 3]
j랑 t 순서대로 넣어줬다





조건 6-3


n=   아큐먼트로 받음
j=2    j는  루프로 1부터 n까지 넣어줌
t=3    t는    t=int(math.log2(n)) 
arrlist=[]
for i in range(j):
    arrlist.append(j)
for i in range(t):
    arrlist.append(t)
print(arrlist)
결과 arrlist는  [2, 2, 3, 3, 3]

import itertools
lenarrlist = len(arrlist)     
nPr = itertools.permutations(arrlist, lenarrlist )   
print(list(nPr))

ll=[]
for i in list(nPr):
    #print(i)
    ll.append(i)
print(set(ll))
print(list(set(ll)))





================================총정리
================================총정리
================================총정리
================================총정리
================================총정리
================================총정리
================================총정리
================================총정리



   

조건1  순열 퍼뮤테이션

num =0 ? 1?   현재위치     n=num 까지 무한루프        while num!=n:    n과넘이 같으면 루프 스탑
n=   아큐먼트로 받음
j=2    j는  루프로 1부터 n까지 넣어줌
t=3    t는    t=int(math.log2(n)) 
arrlist=[]
for i in range(j):
    arrlist.append(j)
for i in range(t):
    arrlist.append(t)
print(arrlist)
결과 arrlist는  [2, 2, 3, 3, 3]

import itertools
lenarrlist = len(arrlist)     
nPr = itertools.permutations(arrlist, lenarrlist )   
print(list(nPr))

ll=[]
for i in list(nPr):
    #print(i)
    ll.append(i)
print(set(ll))
print(list(set(ll)))


조건2 : num에다  t만큼 2를 곱해야함
    코드화
        for i in range(1,t+1):  # t번 만큼 반복  # 즉 1부터 t까지 i로 들어감
            num *= 2  # t번만큼 2를 곱함

조건3 : 점프의 횟수
    방법1 j에 0 부터 ~ 넣어봐서 맞는지 틀린지 검사하다가 맞으면 브레이크
        코드화
            j의 최댓값은? : 일단 n을 넘을 수는 없다 n
            for j in range(1,n+1):    로   j에 0부터 n까지 넣어준다





========================================================================================================================
========================================================================================================================
예제 만들기
========================================================================================================================
========================================================================================================================
========================================================================================================================
========================================================================================================================
========================================================================================================================
========================================================================================================================
========================================================================================================================
========================================================================================================================
========================================================================================================================
========================================================================================================================
========================================================================================================================






1. 아큐먼트 설정

n=6
j=? 0부터 6까지 넣어보기      j=2   j=2가 나와야 한다
t=2   

일단

import math
print(int(math.log2(6)) )
로 t가 2가 나오는 것을 확인

n과 t 선언 완료


2. 순열만들기




num =0 ? 1?   현재위치     n=num 까지 무한루프        while num!=n:    n과넘이 같으면 루프 스탑
n=   아큐먼트로 받음
j=2    j는  루프로 1부터 n까지 넣어줌
t=3    t는    t=int(math.log2(n)) 


arrlist=[]
for i in range(j):
    arrlist.append(j)'''  '''
for i in range(t):
    arrlist.append(t)
print(arrlist)
결과 arrlist는  [2, 2, 3, 3, 3]

import itertools
lenarrlist = len(arrlist)     
nPr = itertools.permutations(arrlist, lenarrlist )   
print(list(nPr))

ll=[]
for i in list(nPr):
    #print(i)
    ll.append(i)
print(set(ll))
print(list(set(ll)))





3. 순열대로 n=num까지 루프돌리다가 j를 리턴 j에 +=1





===========================
===========================
===========================
===========================




n=6 # n=6

import math
t=int(math.log2(6))    # t=2

num = 0   # num 현재 위치 점프 1번으로 시작

# j=?  
# j 를 루프로 1부터 n까지 넣어줌
# 이건천천히

j=2  #일단 j=2 정답값을 넣음

pmlist=[]
for i in range(j):
	pmlist.append(j)
for i in range(t):
	pmlist.append(t)
print(pmlist)

출력 [2, 2, 2, 2]

n=6 j=2 t=2 상황에서 
레인지j로 잡아주니까 pmlist가 숫자로 나와버렸다

j랑 t를 바꿔주자
j는 +1 이고 t는 *2로 바꾸는 거다

j=2 니까 +1이 두개다

pmlist=[]  
for i in range(j):
	pmlist.append("+1")
for i2 in range(t):
	pmlist.append("*2")
print(pmlist)

출력 ['+1', '+1', '*2', '*2']
이렇게 문자열로 넣어줬다

여기까지 다시 정리


====================



n=6 # n=6

import math
t=int(math.log2(6))    # t=2

num = 0   # num 현재 위치 점프 1번으로 시작

# j=?  
# j 를 루프로 1부터 n까지 넣어줌
# 이건천천히

j=2  #일단 j=2 정답값을 넣음


pmlist=[]  
for i in range(j):
	pmlist.append("+1")
for i2 in range(t):
	pmlist.append("*2")

이제 퍼뮤테이션을 걸고 중복을 제거하자

import itertools
lenpmlist = len(pmlist)     
nPr = itertools.permutations(pmlist, lenpmlist )   
ll=[]
for i in list(nPr):
    ll.append(i)
print(list(set(ll)))

그럼 점프와 텔레포트의 순서쌍이 완성

다시정리

====================



n=6 # n=6
import math
t=int(math.log2(6))    # t=2
num = 0   # num 현재 위치 점프 1번으로 시작
# j=?  
# j 를 루프로 1부터 n까지 넣어줌
# 이건천천히
j=2  #일단 j=2 정답값을 넣음
pmlist=[]  
for i in range(j):
	pmlist.append("+1")
for i in range(t):
	pmlist.append("*2")
import itertools
lenpmlist = len(pmlist)     
nPr = itertools.permutations(pmlist, lenpmlist )   #순열
ll=[]
for i in list(nPr):
    ll.append(i)
print(list(set(ll)))  #점프와 텔레포트 순서쌍  #순열에서 중복제거

점프와 텔레포트 순서에 맞게 num 스택쌓으면서 n=num 일 때 j를 리턴하자

================================================


pmset = list(set(ll)) # 점프텔레포트순서 문자열로 +1과 *2

for i in pmset:  # pmset에서 하나를 뽑으면 ('+1', '*2', '+1', '*2') 인 상황
    print(i[0])
    
    
    점프랑 텔레포트를 문자열로 하니까 더 어려워보인다
    다시 j와 t로 바꾸고
    이프를 건다
    
    
    
====================================



n=6 # n=6

import math
t=int(math.log2(6))    # t=2

#num = 0   # num 현재 위치 점프 1번으로 시작

# j=?  
# j 를 루프로 1부터 n까지 넣어줌
# 이건천천히

j=2  #일단 j=2 정답값을 넣음

pmlist=[] 
for i in range(j):
	pmlist.append("j")
for i in range(t):
	pmlist.append("t")
 
import itertools
lenpmlist = len(pmlist)     
nPr = itertools.permutations(pmlist, lenpmlist )   
ll=[]
for i in list(nPr):
    ll.append(i)
    
pmset=list(set(ll))

 
def ff():
    for i in pmset:  # pmset에서 하나를 뽑으면('*2', '+1', '+1', '*2'),인 상황
            num=0 # 루프돌때마다 리셋
            for k in i:  
                if k == "j" :
                    num += 1
                    print("j",num)
                    if n == num:
                        print("1:",n,num)
                        print("aa1")
                        return j
                elif k == "t" :
                    num *= 2 
                    print("t",num)
                    if n == num:
                        print("2:",n,num)
                        print("aa2")
                        return j
            print("==============================",num)
            
print(ff())



일단 j값을 리턴할 수 있다

이제 j값을 1부터 n까지 루프를 걸자






===============================================


def ff():
    n=6
    import math
    t=int(math.log2(6))    # t=2
    for j in range(1,n+1):
        pmlist=[] 
        for i in range(j):
            pmlist.append("j")
        for i in range(t):
            pmlist.append("t")
        import itertools
        lenpmlist = len(pmlist)     
        nPr = itertools.permutations(pmlist, lenpmlist )   
        ll=[]
        for i in list(nPr):
            ll.append(i)
        pmset=list(set(ll))
        for i in pmset:  # pmset에서 하나를 뽑으면('*2', '+1', '+1', '*2'),인 상황
                    num=0 # 루프돌때마다 리셋
                    for k in i:  
                        if k == "j" :
                            num += 1
                            if n == num:
                                return j
                        elif k == "t" :
                            num *= 2 
                            if n == num:
                                return j
print(ff())

j를 1부터 n까지 루프 
j는 2라는 정답을 뽑아낸다
이제 n을 파라미터로 바꾸면 끝난다





=======================================================


def ff(n):
    n=n
    import math
    t=int(math.log2(n))    # t=2
    for j in range(1,n+1):
        pmlist=[] 
        for i in range(j):
            pmlist.append("j")
        for i in range(t):
            pmlist.append("t")
        import itertools
        lenpmlist = len(pmlist)     
        nPr = itertools.permutations(pmlist, lenpmlist )   
        ll=[]
        for i in list(nPr):
            ll.append(i)
        pmset=list(set(ll))
        for i in pmset:  # pmset에서 하나를 뽑으면('*2', '+1', '+1', '*2'),인 상황
                    num=0 # 루프돌때마다 리셋
                    for k in i:  
                        if k == "j" :
                            num += 1
                            if n == num:
                                return j
                        elif k == "t" :
                            num *= 2 
                            if n == num:
                                return j
print(ff(6))

파라미터로 n=6을 넣으니까 정확하기 2를 뽑았다 
이제 프로그래머스에서 정답 테스트를 해보자

테스트결과
    기본테스트 3개중 2개통과 나머지 1개는 시간초과
    실전테스트 16.7%통과 나머지는 전부 시간초과

코드를 좀 줄여보자



import math
import itertools
def solution(n):
    t=int(math.log2(n))   
    for j in range(1,n+1):
        pmlist=[] 
        for i in range(j):
            pmlist.append("j")
        for i in range(t):
            pmlist.append("t")
        lenpmlist = len(pmlist)     
        nPr = itertools.permutations(pmlist, lenpmlist )   
        ll=[]
        for i in list(nPr):
            ll.append(i)
        pmset=list(set(ll))
        for i in pmset:   
                    num=0  
                    for k in i:  
                        if k == "j" :
                            num += 1
                            if n == num:
                                return j
                        elif k == "t" :
                            num *= 2 
                            if n == num:
                                return j
                            

0.1%도 안오른다



import math
import itertools
def solution(n):
    t=int(math.log2(n))   
    for j in range(1,n+1):
        pmlist=[] 
        for i in range(j):
            pmlist.append("j")
        for i in range(t):
            pmlist.append("t")   
        nPr = itertools.permutations(pmlist, len(pmlist))   
        ll=[]
        for i in list(nPr):
            ll.append(i)
        for i in list(set(ll)):   
                    num=0  
                    for k in i:  
                        if k == "j" :
                            num += 1
                            if n == num:
                                return j
                        elif k == "t" :
                            num *= 2 
                            if n == num:
                                return j

0.1%도 안오른다



import math
import itertools
def solution(n):
    t=int(math.log2(n))   
    for j in range(1,n+1):
        pmlist=[] 
        for i in range(j):
            pmlist.append("j")
        for i in range(t):
            pmlist.append("t")   
        nPr = itertools.permutations(pmlist, len(pmlist))   
        ll=[]
        for i in list(nPr):
            ll.append(i)
        for i in list(set(ll)):   
                    num=0  
                    for k in i:  
                        if k == "j" :
                            num += 1
                        elif k == "t" :
                            num *= 2 
                    if n == num:
                        return j
                    
                    
0.1%도 안오른다





import math
import itertools
def solution(n):
    t=int(math.log2(n))   
    for j in range(1,n+1):
        pmlist=[] 
        for i in range(j):
            pmlist.append("j")
        for i in range(t):
            pmlist.append("t")   
        ll=[]
        for i in list(itertools.permutations(pmlist, len(pmlist))):
            ll.append(i)
        for i in list(set(ll)):   
                    num=0  
                    for k in i:  
                        if k == "j" :
                            num += 1
                        else :
                            num *= 2 
                    if n == num:
                        return j
                    
역시 0.1%도 안오른다
이젠 더 줄이지도 못한다
n에 1000을 줘보니까 엄청 느려진다
시간초과는 정답이나 마찬가지니까 만족하자 ㅇㅅㅇ
