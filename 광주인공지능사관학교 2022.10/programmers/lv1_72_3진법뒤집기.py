https://school.programmers.co.kr/learn/courses/30/lessons/68935
프로그래머스lv1 정답률72% 3진법뒤집기

진법 변환 참고 
https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95#n%EC%A7%84%EC%88%98--%E2%86%92-10%EC%A7%84%EC%88%98



자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤
집은 후, 이를 다시 10진법으로 표현한 수를 리턴 하도록 solution 함수를 완성해주세요

3가지 코드가 필요

10진 > 3진법으로 바꾸는 코드
앞뒤반전코드
3진  > 10진법으로 바꾸는 코드


1. 10진 > 3진법
10진 45 는 3진 1200 이다

검색 
def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
print(solution(45, 3))
출력 1200

10진 45를 3진법으로 나타내면 1200 이다


2. 3진 > 10진으로 바꾸는 코드

3진 0021을 10진으로 바꾸면 7이 나와야 한다


print(solution(int('c',16),4)) # 16진수인 C를 4진수로 바꾸는것
print(solution(int('4',6),3))  # 6진수인 4를 3진수로 바꾸는것
print(solution(int('21',3),7)) # 3진수인 21을 7진수로 바꾸는것
print(solution(int('15',9),5)) # 9진수인 15를 5진수로 바꾸는것
에서
print(solution(int('0021',3),10)) # 3진 0021을 10진으로 바꾸면 7이 나와야 한다



def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
print(solution(int('0021',3),10))

출력 7 제대로 나왔다



3. 마지막 앞뒤 반전 코드

1200을 0021로 반전 시켜야 한다

n=1200
#result=0021

일단 위 코드에서
print(solution(45, 3)) 는 스트링이다
print(solution(int('0021',3),10)) 이것도 스트링이고 0021에서 스트링값으로 받는다

스트링 1200을 스트링 0021로 바꾸면된다
그럼 루프돌려서 앞쪽으로 넣어주면 되는데
검색을하면

list = [2, 9, 3]
list.insert(0, 'a')
print(list)

0인덱스로 a를 넣어주는 코드다

코드화



n="1200"
nl=[]
for i in n:
    nl.insert(0,i)
print(nl)
출력 ['0', '0', '2', '1']
출력이 이렇게 나온다 
이걸 "0021" 로 만들려면
하나씩 뽑아서 +로 붙이기




n="1200"
nl=[]
for i in n:
    nl.insert(0,i)
print(nl)

sl=""
for i in nl:
    sl+=i
print(sl)
print(type(sl))


출력 

['0', '0', '2', '1']
0021
<class 'str'>

스트링으로 0021까지 뽑았다




=============================정리

1,2,3 을 이어보자


1. 10진법의 n을 q진법으로 스트링으로 바꾸는 펑션

def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]      # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
print(solution(45, 3)) # 출력 1200 스트링

2. solution(45, 3) 을 0021로 바꾸는 코드



def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]  

num=solution(45, 3)
nl=[]
for i in num:
    nl.insert(0,i)
sl=""
for i in nl:
    sl+=i
print(sl)   # 출력 0021 스트링


3. 0021을    :  3진 0021을 10진으로 바꾸면 7이 나와야 한다
print(solution(int('0021',3),10)) 





def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]  

num=solution(45, 3)
nl=[]
for i in num:
    nl.insert(0,i)
sl=""
for i in nl:
    sl+=i
print(sl)   # 출력 0021 스트링
print(solution(int(sl,3),10)) # 출력 7


==================마무리


이제 펑션으로 묶고 리턴으로 뽑으면 끝





def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]  

num=solution(45, 3)
nl=[]
for i in num:
    nl.insert(0,i)
sl=""
for i in nl:
    sl+=i
print(sl)   # 출력 0021 스트링
print(solution(int(sl,3),10)) # 출력 7



함수에는
def solution(n): 로 파라미터 n 1개만 들어간다



그냥 복붙해서 시간이 좀 걸렸다.

def solution2(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]  

def solution(n):
    num=solution2(n, 3)
    nl=[]
    for i in num:
        nl.insert(0,i)
    sl=""
    for i in nl:
        sl+=i
    return solution2(int(sl,3),10) 

print(solution(45)) # 출력 7

테스트 ㄱ

함수 두개에 리턴이 두개라 그런지
0%로 나왔다
함수 하나로 합쳐야 한다.


def solution(n):
    # n으로 10진수 45가 들어오면 
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    num = rev_base[::-1]  
    print(num) # 3진수 1200 으로 num에 들어간다

    nl=[]
    for i in num:
        nl.insert(0,i)
    print(nl) # ['0', '0', '2', '1'] 로 반전
    
    sl=""
    for i in nl:
        sl+=i
    print(sl)  # 스트링 0021 로 합치기  
    
    print(int(sl,3)) # 출력 7
    
solution(45)



=====


print(int(sl,3))
여기서 좀 어려웠는데
sl은 "0021" 이고
int(스트링,n)
이면 스트링에는 숫자스트링이 들어가고
그 숫자가 n진수라는 뜻이다
그리고 int를 걸어서 10진수로 바꾼다는 말이다

즉 int("0021",3)이면
3진수 21을 10진수로 바꾼다는 말이다 결과 > 7



======정리


#나의 풀이
def solution(n):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    num = rev_base[::-1]   
    nl=[]
    for i in num:
        nl.insert(0,i)
    sl=""
    for i in nl:
        sl+=i
    return int(sl,3)    # print(solution(45)) # 출력 7   100% 통과




좋아요 1위 정답

def solution(n):
    tmp = ''
    while n:  # n으로 10진수 45가 들어가면 
        tmp += str(n % 3) # 45를 3으로 나눈 나머지가 스트링으로 누적
        n = n // 3 # 그 후 45를 3으로 나눈 몫이 n이 된다
#       print(n) # n이 0이되면 while문을 나간다
#   print(tmp) # 0021  str  
    return int(tmp, 3)
print(solution(45)) 

진법의 원리를 이용한 것 같은데 봐도 모르겠다
간단한 while문으로 10진수를 3진수로 그리고 앞뒤반전까지 끝내버린다
int(str,num)으로  3진수의 tmp스트링을 10진수의 인트로 리턴한다
