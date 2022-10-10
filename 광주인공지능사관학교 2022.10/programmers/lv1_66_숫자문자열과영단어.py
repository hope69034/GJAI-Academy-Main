https://school.programmers.co.kr/learn/courses/30/lessons/81301
프로그래머스lv1 정답률66% 숫자문자열과영단어

s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.

숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine

def solution(s):
    
s	                result
"one4seveneight"	1478
"23four5six7"	    234567
"2three45sixseven"  234567
"123"	            123


풀이

1. 일단 보캐불러리를 만들자

voc = {'0':'zero',
    '1':'one', 
    '2': 'two',
    '3':'three', 
    '4': 'four',
    '5':'five', 
    '6': 'six',
    '7':'seven', 
    '8': 'eight',
    '9': 'nine'}

2. 

s에서 첫인덱을 뺀 다음
    인트를 걸어서 숫자인지 문자인지 확인해서 그대로 넣던지 문자면
        보캐에서 대응되는 key값으로 치환하기
        

이 문제 의외로 쉬운 것 같음



예제)

r
e
o
r

s="one4seveneight"
voc = {'0':'zero',
    '1':'one', 
    '2': 'two',
    '3':'three', 
    '4': 'four',
    '5':'five', 
    '6': 'six',
    '7':'seven', 
    '8': 'eight',
    '9': 'nine'}

res=[]
for i,k in enumerate(s):
    try: #숫자라면
        if int(k):
            res.append((i,k))
    except: #문자라면 #에러처리 
        res.append((i,k))
print(res)

출력
[(0, 'o'), (1, 'n'), (2, 'e'), (3, '4'), (4, 's'),
 (5, 'e'), (6, 'v'), (7, 'e'), (8, 'n'), (9, 'e'),
 (10, 'i'), (11, 'g'), (12, 'h'), (13, 't')]

이누머레이트로 인덱스를 달아주고 트라이익셉으로 숫자와 문자를 나눴다






==============











s="one4seveneight"
voc = {'zero':'0',
    'one':'1', 
    'two': '2',
    'three':'3', 
    'four':'4' ,
    'five':'5', 
    'six':'6'  ,
    'seven':'7' , 
    'eight':'8'  ,
    'nine':'9'  }
dic=["zero","one","two","three","four","five","six","seven","eight","nine"]
res=[]
word=""

for i,k in enumerate(s):
    try: #숫자라면
        if int(k):
            res.append(k)
    except: #문자라면 #에러처리 
        word += k
        if word in dic:
            res.append(voc[word])
            word=""

print(res)

출력
['1', '4', '7', '8']
단어집을 추가해서 단어만들고 보캐에서 키로해서 밸류 뽑아서 넣어줌 이제 1478을 합쳐야함




s="one4seveneight"
voc = {'zero':'0',
    'one':'1', 
    'two': '2',
    'three':'3', 
    'four':'4' ,
    'five':'5', 
    'six':'6'  ,
    'seven':'7' , 
    'eight':'8'  ,
    'nine':'9'  }
dic=["zero","one","two","three","four","five","six","seven","eight","nine"]
res=""
word=""

for i,k in enumerate(s):
    try: #숫자라면
        if int(k):
            res+=k
    except: #문자라면 #에러처리 
        word += k
        if word in dic:
            res+=voc[word]
            word=""
            
print(res)  출력 1478
print(type(res))  출력 <class 'str'>


코드 정리하기 / 함수로


def solution(s):
    voc = {'zero':'0',
        'one':'1', 
        'two': '2',
        'three':'3', 
        'four':'4' ,
        'five':'5', 
        'six':'6'  ,
        'seven':'7' , 
        'eight':'8'  ,
        'nine':'9'  }
    dic=["zero","one","two","three","four","five","six","seven","eight","nine"]
    res=""
    word=""
    for k in s:
        try: #숫자라면
            if int(k):
                res+=k
        except: #문자라면 #에러처리 
            word += k
            if word in dic:
                res+=voc[word]
                word=""
    return res


테스트하니 스트링으로 나오니까 오답이라함





def solution(s):
    voc = {'zero':'0',
        'one':'1', 
        'two': '2',
        'three':'3', 
        'four':'4' ,
        'five':'5', 
        'six':'6'  ,
        'seven':'7' , 
        'eight':'8'  ,
        'nine':'9'  }
    dic=["zero","one","two","three","four","five","six","seven","eight","nine"]
    res=""
    word=""
    for k in s:
        try: #숫자라면
            if int(k):
                res+=k
        except: #문자라면 #에러처리 
            word += k
            if word in dic:
                res+=voc[word]
                word=""
    return int(res)



인트로 바꾸니

90%통과
하나는 실패 뜸

s에 머가 들어가면 실패가 뜨는지 보자


일단 s로 0 이 들어가면 에러가 뜨고
        02가 들어가면 2로 뜸
        
하지만 문제에서는 s가 0으로 들어가는 건 주어지지 않는다고 했음



s가 들어갈 땐 문자열
나올 땐 인트



============================================================


print(solution("10")) 넣으니까 출력이 1로 나옴 왜 0이 빠졌지
print(solution("1zero")) 넣으니까 10 그대로 나옴
print(solution("102zero2"))  넣으니까 1202 나옴
"0"이들어가면 빠진다







여기서 보면


def solution(s):
    voc = {'zero':'0',
        'one':'1', 
        'two': '2',
        'three':'3', 
        'four':'4' ,
        'five':'5', 
        'six':'6'  ,
        'seven':'7' , 
        'eight':'8'  ,
        'nine':'9'  }
    dic=["zero","one","two","three","four","five","six","seven","eight","nine"]
    res=""
    word=""
    for k in s:
        try: #숫자라면
            if int(k):
                res+=k
                print("444")
                print(k)  # 1은 여기로 오고
                print("22")
        except: #문자라면 #에러처리 
            word += k
            if word in dic:
                res+=voc[word]
                word=""
                print("3322")
                #print(k)
    return int(res)
solution("10")

1은 위로올라가는데 0은 증발한다



int("0")에서 문제가 생기는 것 같다
int("0") 자체는 그냥 0 으로 뽑힌다
+=k 로 누적시킬때사라지는것같은데0은스트링인데
왜사라지지

그러고 보면 solution("0") 자체가 에러 나는 것부터가 의문

일단  solution("0")을 보자

solution("0") 에서 리턴을
리턴 int(res) 가 아닌
리턴 res 을 주면 아무 값도 안 뽑히고 에러가 안난다
아무것도 없는데 인트를 거니까 에러가 나는 거다
리턴 type(res) 을 줘도 아무 것도 안 뽑힌다


일단

res=""
print(type(res))
이렇게 하면 타입이 str으로 나오는데
리턴 type(res) 은 타입이 안뽑히는 걸 보면 진짜 아무것도 없다는 말이다

왜??


r="0"
print(int("0"))
을하면 출력이 0


다시보자


r="0"
print(1,int("0"))
print(2,int(r))
출력
1 0
2 0
제대로 나온다



다음은


res=""
k="0"
if int(k):
    res+=k
    print("444")
print(1,res)


아 알았다

if int(k)에서 int(k)에 숫자0으로 들어가니까 if 0: 이라 false라
에러 안나고 이프문으로 못 들어가네


그럼 이프를 하나 더 걸어야지



==============================================




#나의 풀이
def solution(s):
    voc = {'zero':'0',
        'one':'1', 
        'two': '2',
        'three':'3', 
        'four':'4' ,
        'five':'5', 
        'six':'6'  ,
        'seven':'7' , 
        'eight':'8'  ,
        'nine':'9'  }
    dic=["zero","one","two","three","four","five","six","seven","eight","nine"]
    res=""
    word=""
    for k in s:
        try: #숫자라면
            if k=="0":    
                res+=k   
            elif int(k):
                res+=k
        except: #문자라면 #에러처리 
            word += k
            if word in dic:
                res+=voc[word]
                word=""
    return int(res)

100% 정답




==============================================





그런데 이상한 점이
중간에 들어가는 "0"은 잘 뽑히는데

이 코드도 첫번째 나오는 "0"은 안뽑힌다

게다가

print(solution("0")) 는 출력 0
print(solution("012")) 는 출력 12 ??
0이 하나면 제대로 나오는데 뒤에 머가 붙으면 안나온다

스트링으로 스택을 쌓는데 왜 없어지는 거야?

이미 정답은 맞췄지만

다시 점검을 해보자






알았다



def solution(s):
    voc = {'zero':'0',
        'one':'1', 
        'two': '2',
        'three':'3', 
        'four':'4' ,
        'five':'5', 
        'six':'6'  ,
        'seven':'7' , 
        'eight':'8'  ,
        'nine':'9'  }
    dic=["zero","one","two","three","four","five","six","seven","eight","nine"]
    res=""
    word=""
    for k in s:
        try: #숫자라면
            if k=="0":    
                res+=k   
                print("a",res)
            elif int(k):
                res+=k
                print("b",res)
        except: #문자라면 #에러처리 
            word += k
            if word in dic:
                res+=voc[word]
                word=""
    return res

print(solution("01"))
출력
a 0
b 01
01




이렇게 보면

a랑 b로 정상적으로 들어가서 res까지 잘 뽑히는데
마지막에 
int(res)를 걸면 01스트링이 인트1로 바뀐다

그래서 문제에서 

< s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.  >

라고 한 것





좋아요 1위 정답을 보자




num_dic = {"zero":"0", "one":"1", "two":"2",
        "three":"3", "four":"4", "five":"5",
        "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


for in 딕셔너리.아이템   으로 키랑 밸류로 뽑고
리플레이스로 키랑 밸류를 교체

뭐지?

허.. 맞네



dic = {"zero":"0", "one":"1", "two":"2",
        "three":"3", "four":"4", "five":"5",
        "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    for key, value in dic.items():
        s = s.replace(key, value)
    return int(s)


키 있는 것만 숫자문자로 바꿔버리고 인트 

간단하다.
