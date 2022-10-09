https://school.programmers.co.kr/learn/courses/30/lessons/12982
프로그래머스lv1 정답률71% 예산

def solution(d, budget):
파라미터 2개

부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이
매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 
지원할 수 있는지 return

#   d	            budget	result
#   [1,3,2,5,4]	    9	    3
#   [2,2,3,3]	    10	    4

1. 일단 d의 합계 sum(d)가 필요
2. budget >= sum(d) 섬d는 예산이하다
    여기서 max()로 섬d의 최댓값을 구한다
        이 때 총 부서를 구하면 한 부서에서 budget을 전부 썼을 수도 있다 error
    즉 여기서부터가 error 섬d가 중요한 것이 아니라 result 가 최댓값이어야 한다
        d리스트 안에서 예산이하로  sum(콤비네이션)으로 뽑아주고 각 result를 구하고 result의 최댓값을 구한다
        

콤비네이션(조합) 함수
from itertools import combinations
list(combinations(items, 2))

#예제만들기

d=[1,3,2,5,4]	
budget=9
#result=3

# d의 콤비네이션
d=[1,3,2,5,4]	
from itertools import combinations
print(list(combinations(d, 2))) # 2는 2개씩 뽑는거다

즉 2를 파라미터로 줘서 1부터 len(d)까지 레인지로 루프를 돌린다
    모든 경우를 다 들여다보자


    
d=[1,3,2,5,4]
for i in range(1,len(d)+1):

이제 콤비네이션 걸기


d=[1,3,2,5,4]
for i in range(1,len(d)+1):
    from itertools import combinations
    print(list(combinations(d, i))) 
    print("==========================================")
    
출력 
[(1,), (3,), (2,), (5,), (4,)]
==========================================
[(1, 3), (1, 2), (1, 5), (1, 4), (3, 2), (3, 5), (3, 4), (2, 5), (2, 4), (5, 4)]
==========================================
[(1, 3, 2), (1, 3, 5), (1, 3, 4), (1, 2, 5), (1, 2, 4), (1, 5, 4), (3, 2, 5), (3, 2, 4), (3, 5, 4), (2, 5, 4)]
==========================================
[(1, 3, 2, 5), (1, 3, 2, 4), (1, 3, 5, 4), (1, 2, 5, 4), (3, 2, 5, 4)]
==========================================
[(1, 3, 2, 5, 4)]
==========================================




이제 각 조합의 sum을 구하기



d=[1,3,2,5,4]
al=[]
for i in range(1,len(d)+1):
    from itertools import combinations
    comList = list(combinations(d, i)) 
    #print(comList)
    #print(len(comList))
    for j in range(len(comList)):
        al.append(sum(comList[j]))
print(al)

출력
[1, 3, 2, 5, 4, 4, 3, 6, 5, 5, 8, 7, 7, 6, 9, 6, 9, 8, 8, 7, 10, 10, 9, 12, 11, 11, 10, 13, 12, 14, 15]
인덱스를 잡아줘야 할 것 같은데
일단 리절트 먼저 잡아보자

al리스트에서 budget=9 보다 작거나 같은 값 중 최댓값을 찾기

budget=9
for i in al:
    if budget=i :
    elif budget > i :
        if 

9이하의 값에서 al리스트에서 인덱스가 가장 큰 것을 잡아야 한다

그럼 al의 인덱스를 반전 시켜보자

alreverse=[]
for i i al:
    alreverse.insert(0,i):
print(alreverse)






d=[1,3,2,5,4]
al=[]
for i in range(1,len(d)+1):
    from itertools import combinations
    comList = list(combinations(d, i)) 
    #print(comList)
    #print(len(comList))
    for j in range(len(comList)):
        al.append(sum(comList[j]))
print(al)
alreverse=[]
for i in al:
    alreverse.insert(0,i)
print(alreverse)

출력
[1, 3, 2, 5, 4, 4, 3, 6, 5, 5, 8, 7, 7, 6, 9, 6, 9, 8, 8, 7, 10, 10, 9, 12, 11, 11, 10, 13, 12, 14, 15]
[15, 14, 12, 13, 10, 11, 11, 12, 9, 10, 10, 7, 8, 8, 9, 6, 9, 6, 7, 7, 8, 5, 5, 6, 3, 4, 4, 5, 2, 3, 1]

리버스값을 포문으로

al2=[]
for i in alreverse :
    if i == budget:
        print(i)
        break
    elif  i <= budget:
        al2.append(i)
print(al2)









=================




d=[1,3,2,5,4]
al=[]
for i in range(1,len(d)+1):
    from itertools import combinations
    comList = list(combinations(d, i)) 
    #print(comList)
    #print(len(comList))
    for j in range(len(comList)):
        al.append(sum(comList[j]))
print(al)
alreverse=[]
for i in al:
    alreverse.insert(0,i)
print(alreverse)

budget=9

al2=[]
for i in alreverse :
    if i == budget:
        print(i)
        break
    elif  i <= budget:
        al2.append(i)
print(al2)



출력
[1, 3, 2, 5, 4, 4, 3, 6, 5, 5, 8, 7, 7, 6, 9, 6, 9, 8, 8, 7, 10, 10, 9, 12, 11, 11, 10, 13, 12, 14, 15]
[15, 14, 12, 13, 10, 11, 11, 12, 9, 10, 10, 7, 8, 8, 9, 6, 9, 6, 7, 7, 8, 5, 5, 6, 3, 4, 4, 5, 2, 3, 1]
9
[]



    if i == budget:
        print(i)
        break        여기서 브레이크 걸렸다.
    
이 때 브레이크 직전 리절트를 리턴해야한다




d=[1,3,2,5,4]
al=[]
for i in range(1,len(d)+1):
    from itertools import combinations
    comList = list(combinations(d, i)) 
    #print(comList)
    #print(len(comList))
    for j in range(len(comList)):
        al.append(sum(comList[j]))
print(al)
alreverse=[]
for i in al:
    alreverse.insert(0,i)
print(alreverse)

budget=9

al2=[]
for k,i in enumerate(alreverse) :
    if i == budget:
        print(i)
        print("index",k) 
        break
    elif  i <= budget:
        al2.append(i)
print(al2)


출력
[1, 3, 2, 5, 4, 4, 3, 6, 5, 5, 8, 7, 7, 6, 9, 6, 9, 8, 8, 7, 10, 10, 9, 12, 11, 11, 10, 13, 12, 14, 15]
[15, 14, 12, 13, 10, 11, 11, 12, 9, 10, 10, 7, 8, 8, 9, 6, 9, 6, 7, 7, 8, 5, 5, 6, 3, 4, 4, 5, 2, 3, 1]
9
index 8
[]


이누머레이트로 일단 인덱스를 구했다.
근데 반전시킨 상태라 다시 이걸 반전해야 하는데
        
1이면 6인덱이고 > 1이면 -1인덱
2 면 5  -2인덱
3 4
4 3
5 2
6 1 

인덱 8이 나왔으니까 -8 인덱이다
그럼


인덱은 반전 전 -k 인덱이고
반전 전 -k 인덱에서 len을 구하면 result가 나오는데


아 잘못햇다

인덱스는 -(k+1)인덱이다 (반전 후 인덱은 0부터시작이라)


반전 전 -(k+1) 인덱에서 result를 구해야 한다






d=[1,3,2,5,4]
al=[]
comListList=[]
for i in range(1,len(d)+1):
    from itertools import combinations
    comList = list(combinations(d, i)) 
 
    
    for u in comList:
        comListList.append(u)

    #print(len(comList))
    for j in range(len(comList)):
        al.append(sum(comList[j]))
print(comListList)
alreverse=[]
for i in al:
    alreverse.insert(0,i)
 

budget=9

al2=[]
for k,i in enumerate(alreverse) :
    if i == budget:
 
        break
    elif  i <= budget:
        al2.append(i)
 

이렇게하면 

comListList 에
[(1,), (3,), (2,), (5,), (4,), (1, 3), (1, 2), (1, 5), (1, 4), (3, 2), (3, 5), (3, 4), (2, 5), (2, 4), (5, 4), (1, 3, 2), (1, 3, 5), (1, 3, 4), (1, 2, 5), (1, 2, 4), (1, 5, 4), (3, 2, 5), (3, 2, 4), (3, 5, 4), (2, 5, 4), (1, 3, 2, 5), (1, 3, 2, 4), (1, 3, 5, 4), (1, 2, 5, 4), (3, 2, 5, 4), (1, 3, 2, 5, 4)]
이렇게 담기니까
여기서  -(k+1) 인덱 잡고 len걸면 
print(len(comListList[-k+1]) )    출력 3 제대로 나왔다







이제 budget보다 적을 때를 잡아줘야 하는데

아 이게 적을 때였고
같은 때





예제)

#result=4
d=[2,2,3,3]
al=[]
comListList=[]
budget=10
alreverse=[]
al2=[]

for i in range(1,len(d)+1):
    from itertools import combinations
    comList = list(combinations(d, i)) 
    for u in comList:
        comListList.append(u)
    for j in range(len(comList)):
        al.append(sum(comList[j]))
for i in al:
    alreverse.insert(0,i)
for k,i in enumerate(alreverse) :
    if i == budget:
        al2.append(i)
        break  # print(len(comListList[-k+1]) )  
    elif  i < budget:
        al2.append(i)
        break
print(len(comListList[-k+1]) )   
 

이렇게 하니까 4가 안나오고 1이 나와버렸음


원래예제코드 조차
버짓을 높게주니까 값이 1로 고정이 되어버린다
버짓이 14가되면 문제가 생긴다
13에서 14가 되면 리절트가 1로 나온다 버짓을 계속 올려도




from itertools import combinations
d=[2,2,3,3]
budget=10
al=[]
comListList=[]
alreverse=[]
al2=[]

상태로 다시 점검해보자..........


휴...........이유를 찾았다
print(len(comListList[-(tt+1)]) ) 
마지막에 인덱스 잡을 떄 ( )를 안쳤다


이제 예제2개
의 result가 올바로 뽑힌다

함수로 만들기











def solution(d, budget):
        
    from itertools import combinations
    al=[]
    comListList=[]
    alreverse=[]
    al2=[]
    tt=0
    tt2=0

    for i in range(1,len(d)+1): # i로 1부터 4까지 들어간다
        comList = list(combinations(d, i))  # d리스트를 1부터 4개까지 뽑는 조합 리스트
        #print(comList)
        for u in comList:
            comListList.append(u)
    #print(comListList) 
        for j in range(len(comList)):
            al.append(sum(comList[j]))
    #print(al)    
    for i in al:
        alreverse.insert(0,i)
    #print(alreverse)
    for k,i in enumerate(alreverse) :
        if i == budget:
            al2.append(i)
            tt=k
            return len(comListList[-(tt+1)])
        elif  i < budget:
            al2.append(i)
            tt2=k
            return len(comListList[-(tt2+1)])
    #print(tt)
    #print(len(comListList[-(tt+1)]) ) 









def solution(d, budget):
    from itertools import combinations
    al=[]
    comListList=[]
    alreverse=[]
    al2=[]
    tt=0
    tt2=0
    for i in range(1,len(d)+1): 
        comList = list(combinations(d, i)) 
        for u in comList:
            comListList.append(u)
        for j in range(len(comList)):
            al.append(sum(comList[j]))   
    for i in al:
        alreverse.insert(0,i)
    for k,i in enumerate(alreverse) :
        if i == budget:
            al2.append(i)
            tt=k
            return len(comListList[-(tt+1)])
        elif  i < budget:
            al2.append(i)
            tt2=k
            return len(comListList[-(tt2+1)])
        
        
        
        
테스트 결과
21%통과에 
1개 실패 나머지 
시간초과가 나왓다
시간초과야 당연히 예상한 결과지만
1개 실패는 뭐지?????????

일단 코드정리


from itertools import combinations
def solution(d, budget):
    al=[]
    comListList=[]
    alreverse=[]
    al2=[]
    tt=0
    for i in range(1,len(d)+1): 
        comList = list(combinations(d, i)) 
        for u in comList:
            comListList.append(u)
        for j in range(len(comList)):
            al.append(sum(comList[j]))   
    for i in al:
        alreverse.insert(0,i)
    for k,i in enumerate(alreverse) :
        if i == budget:
            al2.append(i)
            tt=k
            return len(comListList[-(tt+1)])
        elif  i < budget:
            al2.append(i)
            tt=k
            return len(comListList[-(tt+1)])
        
        
1개 실패 때문에
정신승리도 못하겠다......................................................
에러만 안나면 실패가 안뜰텐데
어디서 에러가 뜨는 거지

예산이 0 일 때??
모든 부서가 요구하는 금액이 예산보다 높을 때?
이걸 점검해봐야겠다.



1. 일단 예산을 0을 주면 none값이 뜬다
예산이 0이면 result가 0 이 나와야 할 것이다
그럼 초반에 if로 버짓이 0이면 바로 걸러버리면 되겠지







from itertools import combinations
def solution(d, budget):
    if budget==0:
        return 0
    al=[]
    comListList=[]
    alreverse=[]
    al2=[]
    tt=0
    for i in range(1,len(d)+1): 
        comList = list(combinations(d, i)) 
        for u in comList:
            comListList.append(u)
        for j in range(len(comList)):
            al.append(sum(comList[j]))   
    for i in al:
        alreverse.insert(0,i)
    for k,i in enumerate(alreverse) :
        if i == budget:
            al2.append(i)
            tt=k
            return len(comListList[-(tt+1)])
        elif  i < budget:
            al2.append(i)
            tt=k
            return len(comListList[-(tt+1)])
        
버짓이 0 인지 검사하는 코드를 추가했으나
여전히 21%에 하나의 실패가 있다

그럼 요구예산이 높은 경우를 살펴보자
print(solution([24,34,24,54,9],8)) 식으로 넣으면 
이 경우에도 역시 None이 뜬다 이것도 0으로 리턴이 되게 바꿔보자


k가 끝인덱 까지 갔을 때에 0으로 리턴하면 될 것 같은데


#나의 풀이
from itertools import combinations
def solution(d, budget):
    if budget==0:
        return 0
    al=[]
    comListList=[]
    alreverse=[]
    al2=[]
    tt=0
    for i in range(1,len(d)+1): 
        comList = list(combinations(d, i)) 
        for u in comList:
            comListList.append(u)
        for j in range(len(comList)):
            al.append(sum(comList[j]))   
    for i in al:
        alreverse.insert(0,i)
    for k,i in enumerate(alreverse) :
        if i == budget:
            al2.append(i)
            tt=k
            return len(comListList[-(tt+1)])
        elif  i < budget:
            al2.append(i)
            tt=k
            return len(comListList[-(tt+1)])
        elif i > budget:
            if k==len(alreverse)-1 :
                return 0
            
            
성공! 실패하나를 죽여서
26% 통과에 나머지 시간초과다

시간초과 실패는 정답이나 마찬가지니까
내가 이겼다ㅇㅅㅇ

좋아요 1위 정답을 보자


def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)


d.sort()
	로 d리스트를 오름차순 정렬로 재정렬한다.
d.pop()  
	d리스트의 끝 원소를 제거한다
while budget < sum(d):
	니까  sum(d) budget 이하가 될 때까지 끝 원소를 제거한다
return len(d)


	이하가 되면 원소 수 = 부서 수를 리턴한다.
난 또 번역 하듯이 문제 그대로 코드로 받아 적어서 풀었는데
이건 수학으로 푼 것도 아니고 코딩 문제 답게 문제가 요구하는 풀이로 푼 느낌이다.