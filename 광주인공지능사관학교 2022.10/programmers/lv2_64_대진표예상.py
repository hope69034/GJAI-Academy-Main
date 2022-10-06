N명 참가 토너먼트
1번토너먼트 1번부터 ~ N번 번호
2번토너먼트 1번부터 ~.N/2번 번호
1명남을때까지 부전승x     
a b 눈 무조건 승


앞이 홀수 뒤가 짝수에 연이은 수라면 매칭 성립



n

                  n/2*2*2               라운드는 n/2번
            1           n/2*2       
         1    2      3        n/2
       1  2  3 4   5   6    7     n
    

번호 변화
               n은 8
1번
	1 1 1 1    a a a a
2번 
 	2 1 1 1   a  a//2 
3번
	3 2 1 1  a  a//2
4번 
	4 2 1 1
5번 
	5 3 2 1
6번
	6 3 2 1
7번 
 	7 4 2 1
n번
	n     n/2     n/2*2   n/2*2*2



1 2      1
2 3      2
3 4      1

4 5      4      n/2 라운드에서 무조건 만난다  왼쪽면 vs 오른쪽면이면 if문 하나

5 6      1
6 7      2
7 8      1





n이 8 일 때   2에 3승

if
	n/2 라운드에서 무조건 만난다  왼쪽면 vs 오른쪽면이면 if문 하나
if
	연이은 수 이고 앞이 홀수 뒤가 짝수면      1라운드  n/2*2*2 라운드
	연이은 수 앞이 짝수 뒤가 홀수면 2라운드   n/2*2 라운드  == 3승-1

 

                    1 
         1                        2 
    1          2             3             4
 1      2    3     4      5      6       7       8
1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  n

n은 16   2에 4승
if
	n/2 라운드에서 무조건 만난다  왼쪽면 vs 오른쪽면이면 if문 하나
if
	연이은 수 이고 앞이 홀수 뒤가 짝수면  1라운드 ==  n/2*2*2*2 라운드
	연이은 수 앞이 짝수 뒤가 홀수면       2라운드   n/2*2*2 라운드  == 3승-1


1이랑 5면  3라운드
	반에서 다시 반을 해서 떨어져있으면   



	반띵이면 4라운드





n 8기준

3라운드 반띵이면    
2라운드 연이은 수 앞이 짝수 뒤가 홀수면 
1라운드 연이은 수 이고 앞이 홀수 뒤가 짝수면

8 나누기2 
8 나누기2나누기2 
8 나누기2 나누기2 나누기2 

n 16기준

4라운드 반띵이면 4라운드             최대라운드는 하나씩증가 2에4승이면 최대라운드가 4라운드  
3라운드 반에서 다시 반을 해서 떨어져있으면   
2라운드 연이은 수 앞이 짝수 뒤가 홀수면 
1라운드 연이은 수 이고 앞이 홀수 뒤가 짝수면


16나누기2
16나누기2 나누기2
16나누기2 나누기2나누기2
16나누기2 나누기2나누기2나누기2



n 기준

n라운드 반띵이면 4라운드             최대라운드는 하나씩증가 2에4승이면 최대라운드가 4라운드  
.
.
3라운드 반에서 다시 반을 해서 떨어져있으면   
2라운드 연이은 수 앞이 짝수 뒤가 홀수면 
1라운드 연이은 수 이고 앞이 홀수 뒤가 짝수면




        2의x승 곱2
n나누기 2의x승     2의x승==n


2로 몇번나누는지가 기준?





ex)

n을 16
a를 2 
b를 7




n나누기 2는 8


1. if문 n을 2로 나눠서 
a랑 b가 반으로 갈리는지 확인 
반이 맞으면  n이 2의 x승이면 답은 x 이다.


1-1. 2로 몇번 나뉘는지에 따라  1부터 x까지 답이 나뉜다

이프문 하나 


===================================


n=16
a=2
b=7
//result=3

n이 2의 x승일 때

2로 한번 갈리면 답은 x
2로 두번          x-1    x-
2로 세번         x-2



2로 1번 갈리면 답은 x        == x
2로 2번          x-1        == x-t+1
2로 t번         x-(t-1)     == x-t+1


* n에서 x변수 뽑기
* 변수t  뽑기

===================================

1. x변수 잡아주기
n=16
n은 2의 x승

x=0
n=16
while n != 1 :

	n /= 2
	x += 1
print(x) 
================================================
//이렇게하면 x를 구했다.

2. 변수 t 잡아주기
a와 b를 2로 t번 나눠야 서로 반으로 갈리는지 잡아주기 

a=2
b=7
이라고 했을 때
n=16 에서 2로 1번 나누면   8 이니까 실패
8에서 2로 한번 더 나누면 4니까 성공
즉 2번 나눴으니까 t는 2니까 답은 
x-t+1 에서 4-2+1  은 즉 3


n나누기 t 하ㅣㄴ 것이 a와 비 사이인지



n/2   이하인지 a랑 b가 동시에    
또는 n/2 초과인지 a랑 b가 동시에  그렇면 cloollect


n/t   //n을 t로 나누는데 t로 나눌때마다 t counter에 1씩 누적하여 몇번나눴는지


a=2
b=7
n=16
tcounter = 0 
for i in range(1,n):
	if n != 2 :	
  		#t = 2**i 
		n /=  2    
		tcounter += 1
		#print(tcounter)
		#print(n)

print(tcounter)

#tcounter는 3나옴

#이제 중간에끊는 이프문추가해야함





a=1
b=2
n=16
import math
t = int(math.log2(n))

for i in range(1,t+1):
   #현재 t (정답) 은 4인 상황이니까 반띵이되면 바로 브레이크해야함
   if a <= n/2**i and n/2**i < b :
      print(t)
      break
   else:
      t-=1
   # 이제 답이4가되야하는데 반으로 자르고 또 반으로 잘라야함
 
얼떨결에 그냥 성공
함수로 바꿔주자



def solution(n,a,b):
	import math
	t = int(math.log2(n))
	for i in range(1,t+1):
		#현재 t (정답) 은 4인 상황이니까 반띵이되면 바로 브레이크해야함
		if a <= n/2**i and n/2**i < b :
			return t
			break
		else:
			t-=1
   # 이제 답이4가되야하는데 반으로 자르고 또 반으로 잘라야함
 
   
테스트 결과 26퍼센트가 나왓다

a와 b의 대소관계에 관한 코드를 추가해야하는 것 같다
위코드는 무조건 b가 a보다 크다는 가정을 해서 오류가 생긴 것 같다








def solution(n,a,b):
	import math
	t = int(math.log2(n))
	for i in range(1,t+1):
		
		if a < b :
			if a <= n/2**i and n/2**i < b :
				return t
				break
			else:
				t-=1
		elif a > b : 
			if b <= n/2**i and n/2**i < a :
				return t
				break
			else:
				t-=1

a와b의 대소관계에 관한 코드를 추가하니까
정확도가 52프로로 올랐지만 여전히 반은 오답이다
elif a > b를 else로 바꿔도 정확도는 그대로

정확도로 봤을 땐 완벽한 코드 같은데
왜 오답이 뜨는지 모르겠네






def solution(n,a,b):
	import math
	t = int(math.log2(n))
	for i in range(1,t+1):
		
		if a < b :
			if a <= n/(2**i) and n/(2**i) < b :
				return t
				break
			else:
				t-=1
		elif a > b : 
			if b <= n/(2**i) and n/(2**i) < a :
				return t
				break
			else:
				t-=1
 
거듭제곱이먼저니까이것도당연히그대로
어디가 문제일까

일단 코드 정리





def solution(n,a,b):
	import math
	t = int(math.log2(n))
	for i in range(1,t+1):
		if a < b :
			if a <= n/(2**i) and n/(2**i) < b :
				return t		
			else:
				t-=1
		elif a > b : 
			if b <= n/(2**i) and n/(2**i) < a :
				return t
			else:
				t-=1
 
   
생각하다보니까
이게좀이상하다
반으로가르는코드가제대로동작안할듯

첫턴 후
두번째 턴에서
4만 잡으니까 문제가 생긴다
4랑 12를 같이 잡아줘야 하는데









def solution(n,a,b):
	import math
	t = int(math.log2(n))
	for i in range(1,t+1):
		if a < b :

			if a <= n/(2**i) and b <= n/(2**i) :
				t-=1
			elif 	a > n/(2**i) and b > n/(2**i) :
				t-=1
			elif a <= n/(2**i) and n/(2**i) < b :
				return t


4랑 12를 같이 잡아주는 건 힘들 것 같다

a랑 b를 줄여줘야한다




def solution(n,a,b):
	import math
	t = int(math.log2(n))
	for i in range(1,t+1):
		if a < b :
			if a <= n/(2**i) and n/(2**i) < b :
				return t		
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a > b : 
			if b <= n/(2**i) and n/(2**i) < a :
				return t
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)

정확도가 29프로로 줄었다
a랑 b의 수를 라운드별로 반으로줄이고 올림해줘서 
정확하게 잡아줫는데 뭐지

a랑 b가 같아지는 경우에 문제가 생기는 건가





def solution(n,a,b):
	import math
	t = int(math.log2(n))
	for i in range(1,t+1):
		if a < b :
			if a <= n/(2**i) and n/(2**i) < b :
				return t		
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a > b : 
			if b <= n/(2**i) and n/(2**i) < a :
				return t
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a == b :
			t-=1


a==b를 추가하니 32프로다
근데 a==b일 때 바로 리턴t를 하는 게 아닌 것 같다












def solution(n,a,b):
	import math
	t = int(math.log2(n))
	for i in range(1,t+1):
		if a < b :
			if a <= n/(2**i) and n/(2**i) < b :
				return t		
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a > b : 
			if b <= n/(2**i) and n/(2**i) < a :
				return t
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a == b :
			if a==2 or a==1 :
				return t+2	
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)


이건 32퍼센트










def solution(n,a,b):
	import math
	t = int(math.log2(n))
	for i in range(1,t+1):
		if a < b :
			if a <= n/(2**i) and n/(2**i) < b :
				return t		
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a > b : 
			if b <= n/(2**i) and n/(2**i) < a :
				return t
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a == b :
			if a==2 or a==1 :
				return t+1	
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)



이건 35퍼센트








def solution(n,a,b):
	import math
	t = int(math.log2(n))
	count = 0 
	for i in range(1,t+1):
		if a < b :
			count+=1
			if a <= n/(2**i) and n/(2**i) < b :

				return t		
			else:

				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a > b : 
			count+=1
			if b <= n/(2**i) and n/(2**i) < a :
				return t
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a == b :
			count+=1
			return count

이상하다 이건 진짜 맞는 것 같은데
a랑 b가 가깝게 나왔을 때 카운트로 역으로 올라가면서 센다






def solution(n,a,b):
	import math
	t = int(math.log2(n))
	count = 0 
	for i in range(1,t+1):
		if a < b :
			count+=1
			if a <= n/(2**i) and n/(2**i) < b :
				return t		
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a > b : 
			count+=1
			if b <= n/(2**i) and n/(2**i) < a :
				return t
			else:
				t-=1
				a=math.ceil(a/2)
				b=math.ceil(b/2)
		elif a == b :
			count+=1
			return count-1


return count-1 로

드디어 100% 정답 

물론
count+=1 을 빼고
return count 만 써도 정답이다

역시 2레벨은 진득하게 단계적으로 풀어나가면 불가능한 수준은 아니다

실전에 이런거 나오면
빨리 포기해야 한다
그런데 될 것 같으면서 안되는 게 문제
