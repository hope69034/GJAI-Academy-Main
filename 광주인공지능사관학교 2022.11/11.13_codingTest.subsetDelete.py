# 두 아규먼트가 주어진다 영문소문자텍스트 두개인 레퍼런스와 리절트이다 ex) ref= 'abc'  res=='babca'
#레퍼런스를 받아서 부분집합으로 리절트를 삭제시키고 쓰인 부분집합의 각 len의 최솟값을 앤서로 리턴해야 한다
#먼저 부분집합을 정의해야 할 것이다

# 하나씩 쪼개는 리스트를 만든다
txt = 'abc'
t2 = list(''.join(txt))
#print(t2,type(t2)) # ['a', 'b', 'c', 'd', 'e', 'f'] <class 'list'>

# 조건에 해당하는 부분집합을 구하여 t2를 깊은 복사한 t3에 어펜드한다
t3 =  t2.copy()#깊은복사
from itertools import combinations

for i in range(2,len(txt)+1): # 2~6 콤비네이션
    count=0
    for j in list(combinations(t2, i)): # 2~6 콤비네이션
        j=''.join(j)
        if j[0]==txt[count]:
            count+=1
            t3.append(j)
print(t3) # 부분집합 완성 ['a', 'b', 'c', 'd', 'e', 'f', 'ab', 'bc', 'cd', 'de', 'ef', 'abc', 'bcd', 'cde', 'def', 'abcd', 'bcde', 'cdef', 'abcde', 'bcdef', 'abcdef']

#리절도 위와같이 부분집합을 만들어서 기존 레퍼와 비교하여 연산해야 할 것 같다
#그래서 위와 같은 작업을 리절에도 해준다
txt2 = 'babca'
t22 = list(''.join(txt2))
#print(t22,type(t22)) # ['a', 'b', 'c', 'd', 'e', 'f'] <class 'list'>

# 조건에 해당하는 부분집합을 구하여 t2를 깊은 복사한 t3에 어펜드한다
# t33 =  t22 로 얕은복사를 하는 경우 t33에 어펜드해도 t22에도 들어가기 때문에
# 콤비네이션t22부분이 바뀌면서 문제가 생긴다
t33 =  t22.copy()#깊은복사
from itertools import combinations

for i in range(2,len(txt2)+1): # 2~6 콤비네이션
    count=0
    for j in list(combinations(t22, i)): # 2~6 콤비네이션
        j=''.join(j)
        if j[0]==txt2[count]:
            count+=1
            t33.append(j)
print(t33) # 부분집합 완성 ['a', 'b', 'c', 'd', 'e', 'f', 'ab', 'bc', 'cd', 'de', 'ef', 'abc', 'bcd', 'cde', 'def', 'abcd', 'bcde', 'cdef', 'abcde', 'bcdef', 'abcdef']

#리버스드 후
rt3=list(reversed(t3))
rt33=list(reversed(t33))
#print(rt3)
#print(rt33) 

for i in rt33:
    for j in rt3:
        if i == j :
            txt2=txt2.replace(j, "")
            #print(j)
            if txt2=='':
                print(len(j))
# 여기서 len j 가 최종 결과값이 된다

#def함수로 변경
def main(txt,txt2):
    t2 = list(''.join(txt))
    t3 =  t2.copy()#깊은복사
    from itertools import combinations
    for i in range(2,len(txt)+1): # 2~6 콤비네이션
        count=0
        for j in list(combinations(t2, i)): # 2~6 콤비네이션
            j=''.join(j)
            if j[0]==txt[count]:
                count+=1
                t3.append(j)
    t22 = list(''.join(txt2))
    t33 =  t22.copy()#깊은복사
    from itertools import combinations
    for i in range(2,len(txt2)+1): # 2~6 콤비네이션
        count=0
        for j in list(combinations(t22, i)): # 2~6 콤비네이션
            j=''.join(j)
            if j[0]==txt2[count]:
                count+=1
                t33.append(j)
    rt3=list(reversed(t3))
    rt33=list(reversed(t33))
    for i in rt33:
        for j in rt3:
            if i == j :
                txt2=txt2.replace(j, "")
                #print(j)
                if txt2=='':
                    return len(j)
print(main('abc','babca')) # 1
# 결과가 잘 뽑혔다


# 정리 후 제출
def solution(reference,result):
    from itertools import combinations
    t2 = list(''.join(reference))
    t3 =  t2.copy()#깊은복사
    for i in range(2,len(reference)+1): # 2~len(ref)
        count=0
        for j in list(combinations(t2, i)): # 2~len(ref) 콤비네이션
            j=''.join(j)
            if j[0]==reference[count]:
                count+=1
                t3.append(j)
    t22 = list(''.join(result))
    t33 =  t22.copy()#깊은복사
    for i in range(2,len(result)+1): # 2~len(ref)
        count=0
        for j in list(combinations(t22, i)): # 2~len(ref) 콤비네이션
            j=''.join(j)
            if j[0]==result[count]:
                count+=1
                t33.append(j)
    rt3=list(reversed(t3))
    rt33=list(reversed(t33))
    for i in rt33:
        for j in rt3:
            if i == j :
                result=result.replace(j, "") # 제거
                if result=='': # 완전제거
                    answer=len(j)
                    return answer
                
# 코드리펙토링
def solution(reference,target):
    from itertools import combinations
    subset=[] # 레퍼의 부분집합과 타겟의 부분집합을 담을 리스트
    for r in [reference,target]:
        part=list(''.join(r)) # 원소1개인 부분집합
        for i in range(2,len(r)+1): # 2~len(ref)
            count=0
            for j in list(combinations(list(''.join(r)), i)): # 2~len(ref) 콤비네이션, list(''.join(r)) 을 part로 쓰면 아래 part.append때문에 값이 달라져서 문제가 생김
                j=''.join(j)
                if j[0] == r[count]:
                    count += 1
                    part.append(j)
        reversedPart=list(reversed(part))
        subset.append(reversedPart)
    for i in subset[1]: # 타겟의 부분집합
        for j in subset[0]:  # 레퍼의 부분집합
            if i == j:
                target=target.replace(j, "") # 제거
                if target == '': # 완전제거 후 리턴
                    answer=len(j)
                    return answer