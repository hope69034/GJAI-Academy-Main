https://school.programmers.co.kr/learn/courses/30/lessons/68644
프로그래머스 레벨1 정답률65%


a=[2,1,3,4,1]

from itertools import combinations
b=list(combinations(a, 2))
print(b)



# 1. a에서중복제거

a2=list(set(a))
print(a2)

# 2. 중복 제거 후 콤비네이션
from itertools import combinations
a3=list(combinations(a2, 2))
print(a3)

# 3. 각 콤비네이션 합
a3list=[]
for i in a3:
    k=i[0]+i[1]
    #a3list.append(str(i[0][0]+i[0][1]))
    if k not in a3list:
        a3list.append(k)
print(a3list)


#정리

from itertools import combinations
a2=list(set(numbers))
a3=list(combinations(a2, 2))
a3list=[]
for i in a3:
    k=i[0]+i[1]
    #a3list.append(str(i[0][0]+i[0][1]))
    if k not in a3list:
        a3list.append(k)
print(a3list)


# 정리2

from itertools import combinations

def solution(numbers):
    a2=list(set(numbers))
    a3=list(combinations(a2, 2))
    a3list=[]
    for i in a3:
        k=i[0]+i[1]
        if k not in a3list:
            a3list.append(k)
             
    answer = a3list
    return answer


#결과 중복제거를 먼저하니까 1+1=2 같은 것이 삭제되는 문제 발생
from itertools import combinations
numbers=[2,1,3,4,1]

def solution(numbers):
    
    
    
    
    a2=list(set(numbers))
    a3=list(combinations(a2, 2))
    a3list=[]
    for i in a3:
        k=i[0]+i[1]
        if k not in a3list:
            a3list.append(k)
             
    answer = a3list
    return answer

solution(numbers)




# 중복제거를 안하고 콤비네이션

from itertools import combinations
numbers=[2,1,3,4,1]
def solution(numbers):
    a3=list(combinations(numbers, 2))
    a3list=[]
    for i in a3:
        k=i[0]+i[1] #튜플에서각원소뽑아서합
        if k not in a3list:
            a3list.append(k)
    answer = sorted(a3list) # 오름차순정렬
    return answer
print(solution(numbers))


# 제출 100점
from itertools import combinations
def solution(numbers):
    a3=list(combinations(numbers, 2))
    a3list=[]
    for i in a3:
        k=i[0]+i[1] #튜플에서각원소뽑아서합
        if k not in a3list:
            a3list.append(k)
    answer = sorted(a3list) # 오름차순정렬
    return answer
