https://school.programmers.co.kr/learn/courses/30/lessons/17681
프로그래머스lv1 정답률69% 1차비밀지도

["######", 
 "### #", 
 "## ##", 
 " #### ", 
 " #####", 
 "### # "]

["######", 
 "### #", 
 "## ##", 
 " #### ", 
 " #####", 
 "### # "]

-조건

공백 두개 연속이면 1개로 처리
1 ≦ n ≦ 16
arr1, arr2는 길이 n인 정수 배열 
 0 ≦ x ≦ 2n - 1 (정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다.)


-예제

매개변수	값
n	    5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	["#####","# # #", "### #", "# ##", "#####"]

매개변수	값
n	    6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	["######", "### #", "## ##", " #### ", " #####", "### # "]


def solution(n, arr1, arr2):
    파라미터3개
        리턴은 샵과공백리스트


풀이 순서

1. arr를 2진수로 바꾼다
    단 n 길이까지 0을 채워줘야한다
2. arr합치기 
    둘 중 하나라도 벽이면 벽 or  / 둘다 공백이면 공백 and
    즉 1이 하나라도 있다면 1로 바꾸는 이진수로 바꾼다
3. 이진수를 샵으로 변환하여 리턴

이렇게 풀려면 또 포문 5개 이상 때려박고 시간초과 나올게 뻔한데..
간단하게 푸는 방법 없을까

일단 이진수로 바꾸고

arr가 두개니까 집으로 묶어버리고
리스트컴프리헨션에 x,y로 빼주고 1 하나라도 있으면 샵으로 빼주고 아니면 " "으로
바로 빼주기 

일단 무턱대고 번역식 코딩하기 전에 이런 생각 먼저 한 걸 보면 실력이 늘었다.


====================

예제코드)

1.변수선언

n	 =   5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
#출력	["#####","# # #", "### #", "# ##", "#####"]

2. 이진수변환

arr1s=[]
arr2s=[]
for 

아니 집으로 먼저 합쳐버리자


2. 집

arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
arrzip=zip(arr1,arr2)
print(arrzip)
for i in arrzip:
    print(i)
    
출력
<zip object at 0x00000247301B9900>
(9, 30)
(20, 1)
(28, 21)
(18, 17)
(11, 28)

3. 집으로 합치면서 바로 이진수로 바꿔보자

arrbin=[(bin(x),bin(y)) for (x,y) in zip(arr1,arr2) ]
print(arrbin)

출력
[('0b1001', '0b11110'), ('0b10100', '0b1'), ('0b11100', '0b10101'), ('0b10010', '0b10001'), ('0b1011', '0b11100')]

앞에 인덱두개를 빼보자





arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
arrzip=zip(arr1,arr2)
#print(arrzip)
#for i in arrzip:
#    print(i)
    
# arrbin=[(bin(x),bin(y)) for (x,y) in zip(arr1,arr2) ]
# print(arrbin)

arrbin=[(bin(x)[2:],bin(y)[2:]) for (x,y) in zip(arr1,arr2) ]
print(arrbin)

출력
[('1001', '11110'), ('10100', '1'), ('11100', '10101'), ('10010', '10001'), ('1011', '11100')]

집이랑 리스트컴프리헨션 처음 써본다 실력이 많이 늘어난 기분

지금 문제는 숫자 앞에 비는 칸을 0으로 채워야 한다는 거다





=======================================일단 코드 정리
=======================================일단 코드 정리




n	 =   5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
#출력	["#####","# # #", "### #", "# ##", "#####"]
    
arrbin=[(bin(x)[2:],bin(y)[2:]) for (x,y) in zip(arr1,arr2) ]
print(arrbin)

출력
[('1001', '11110'), ('10100', '1'), ('11100', '10101'), ('10010', '10001'), ('1011', '11100')]


할일
    숫자앞에 0으로 채우기
    튜플비교해서 샵이랑 공백으로 변환해서 리턴
    
    
일단 뽑아서 len을 잡고 n보다 작으면 인설트0인덱으로 0을 넣으면 될 듯
    분명 노가다 코드 안쓰고 할 수 있을텐데 arrbin에서 이프를 또 걸어줘야하나
    일단 함해보자

일단 if가 필요하고 len이 n보다 작은지 묻기

[            if n > (  len(bin(x)[2:])  ,  len(bin(y)[2:])  )             for (x,y) in zip(arr1,arr2) ]
튜플 속에 담겨있어서 이걸..




일단 컴프리헨션 없이 적고 나서 해보자








===================================




n	 =   5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
#출력	["#####","# # #", "### #", "# ##", "#####"]
    
arrbin=[(bin(x)[2:],bin(y)[2:]) for (x,y) in zip(arr1,arr2) ]
print(arrbin)

출력
[('1001', '11110'), ('10100', '1'), ('11100', '10101'), ('10010', '10001'), ('1011', '11100')]





n	 =   5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
#출력	["#####","# # #", "### #", "# ##", "#####"]
    
arrbin=[(bin(x)[2:],bin(y)[2:]) for (x,y) in zip(arr1,arr2) ]
print(arrbin[0][0])
을하면 1001 하나가 뽑힌다 여기 앞에 0을 인설트로

아 인설트가 아니라
print("0"+arrbin[0][0])   타입은 <class 'str'>
하면 01001이 되긴 했는데
0을 모자란 만큼 넣어야 하니까
루프를 돌려야 하는데




============================






n	 =   5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
#출력	["#####","# # #", "### #", "# ##", "#####"]
    
arrbin=[(bin(x)[2:],bin(y)[2:]) for (x,y) in zip(arr1,arr2) ]
#print(arrbin[0][0])
#print("0"+arrbin[0][0])
#print(type("0"+arrbin[0][0]))

for i in range(n):  #튜플하나뽑고
    for j in range(2): #튜플에서첫원소랑두번째원소
        arrbin[i][j] = "0"*(n-arrbin[i][j]) + arrbin[i][j]
print(arrbin[0][0])


이렇게 하니까 에러가 뜬다 
    TypeError: unsupported operand type(s) for -: 'int' and 'str'
인트랑 문자 연산 코드에서 확인을 해보자


아코드 실수 
다시



=============




n	 =   5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
#출력	["#####","# # #", "### #", "# ##", "#####"]
    
arrbin=[(bin(x)[2:],bin(y)[2:]) for (x,y) in zip(arr1,arr2) ]
#print(arrbin[0][0])
#print("0"+arrbin[0][0])
#print(type("0"+arrbin[0][0]))

for i in range(n):  #튜플하나뽑고
    for j in range(2): #튜플에서첫원소랑두번째원소
        arrbin[i][j] = "0"*(n-len(arrbin[i][j])) + arrbin[i][j]
print(arrbin)


에러
Traceback (most recent call last):
  File "c:\Users\hope6\Desktop\pp copy 5.py", line 15, in <module>
    arrbin[i][j] = "0"*(n-len(arrbin[i][j])) + arrbin[i][j]
TypeError: 'tuple' object does not support item assignment

튜플에러라는데 포문을 점검 좀

포문 2개 자체는 에러가 안뜸

arrbin[i][j] 에서도 안뜸

"0"*(n-len(arrbin[i][j])) 여기서도 안뜸

"0"*(n-len(arrbin[i][j])) + arrbin[i][j] 여기서도 안뜸

arrbin[i][j] = "0"*(n-len(arrbin[i][j])) + arrbin[i][j]  여기로 오면 에러가 뜬다

이제보니 조금 이상한 느낌도 있는데 정확히 왜 문제인지는 모르겠다

레프트밸류가 변수가 아닌 느낌인데

그럼

arrbin에서 원소를 바꿔넣어줘야 한다는 말인데

그건 힘들 것 같고 새리스트로 만들어야지





==========================




n	 =   5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
#출력	["#####","# # #", "### #", "# ##", "#####"]
    
arrbin=[(bin(x)[2:],bin(y)[2:]) for (x,y) in zip(arr1,arr2) ]
#print(arrbin[0][0])
#print("0"+arrbin[0][0])
#print(type("0"+arrbin[0][0]))

arrbinnew=[]
for i in range(n):  #튜플하나뽑고
    for j in range(2): #튜플에서첫원소랑두번째원소
        arrbinnew.append( "0"*(n-len(arrbin[i][j])) + arrbin[i][j])

print(arrbinnew)

출력
['01001', '11110', '10100', '00001', '11100', '10101', '10010', '10001', '01011', '11100']

리스트에 어펜드 해줘서 튜플이 깨져버렸음

원소 갈아끼는 함수를 찾아보자

아..

튜플이 이뮤터블이라 리스트로 만들고 다시 튜플로 만들라는데

print(tuple(arrbinnew)) 이렇게하면

('01001', '11110', '10100', '00001', '11100', '10101', '10010', '10001', '01011', '11100')
이렇게 전체가 묶인다

두개씩 어떻게 묶지

또 루프돌려야겠다

아 어짜피 샵으로 변환할 때 튜플에서 바로 못 바꾸니까 그냥 해야지


arrbinnew 리스트에서 홀수번째랑 짝수번째랑 구분하면 된다.


 



=========================================================







n	 =   5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
#출력	["#####","# # #", "### #", "# ##", "#####"]
arrbin=[(bin(x)[2:],bin(y)[2:]) for (x,y) in zip(arr1,arr2) ]
arrbinnew=[]
for i in range(n):  #튜플하나뽑고
    for j in range(2): #튜플에서첫원소랑두번째원소
        arrbinnew.append( "0"*(n-len(arrbin[i][j])) + arrbin[i][j])
result=[]
for i in range(0,n*2-1,+2) :   #n이 5면 i는 0 2 4 6 8 이 들어오게끔 만들었다
    reslist=[]
    for j in range(n):
        if arrbinnew[i][j] == "1" or arrbinnew[i+1][j] == "1" :
            reslist +="#"
        else :
            reslist +=" "
    result.append(reslist)
print(result)

출력
[['#', '#', '#', '#', '#'], ['#', ' ', '#', ' ', '#'], ['#', '#', '#', ' ', '#'], ['#', ' ', ' ', '#', '#'], ['#', '#', '#', '#', '#']]

일단 값은 제대로 뽑혔다 
이제 묶어서 나와야 하는데





==============================



n	 =   5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
#출력	["#####","# # #", "### #", "# ##", "#####"]
arrbin=[(bin(x)[2:],bin(y)[2:]) for (x,y) in zip(arr1,arr2) ]
arrbinnew=[]
for i in range(n):  #튜플하나뽑고
    for j in range(2): #튜플에서첫원소랑두번째원소
        arrbinnew.append( "0"*(n-len(arrbin[i][j])) + arrbin[i][j])
result=[]
for i in range(0,n*2-1,+2) :   #n이 5면 i는 0 2 4 6 8 이 들어오게끔 만들었다
    reslist=""
    for j in range(n):
        if arrbinnew[i][j] == "1" or arrbinnew[i+1][j] == "1" :
            reslist +="#"
        else :
            reslist +=" "
    result.append(reslist)
print(result)

출력
['#####', '# # #', '### #', '#  ##', '#####']




출력예시를 보면
#출력	["#####","# # #", "### #", "# ##", "#####"]
이렇게 공백두개가 합쳐지면 공백 하나로 출력하는 것처럼 보이는데

일단
함수로 바꾸고 테스트 해보자



====================================





#나의 풀이
def solution(n, arr1, arr2):
    arrbin=[(bin(x)[2:],bin(y)[2:]) for (x,y) in zip(arr1,arr2) ]
    arrbinnew=[]
    for i in range(n):  #튜플하나뽑고
        for j in range(2): #튜플에서첫원소랑두번째원소
            arrbinnew.append( "0"*(n-len(arrbin[i][j])) + arrbin[i][j])
    result=[]
    for i in range(0,n*2-1,+2) :   #n이 5면 i는 0 2 4 6 8 이 들어오게끔 만들었다
        reslist=""
        for j in range(n):
            if arrbinnew[i][j] == "1" or arrbinnew[i+1][j] == "1" :
                reslist +="#"
            else :
                reslist +=" "
        result.append(reslist)
    return result



100%통과 정답이다
이번엔 그나마 리스트컴프리헨션써서 코드를 많이 줄인 것 같다
그래도 for가 5개다 (시간초과안뜨네)