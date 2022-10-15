[3일차]

1 주식 투자 기법 60점     2오답

a=input()
b=list(map(int,a.split()))
cn=0
for i in b:
    b.pop(0)
    for j in b:
        if (i-j) < cn:
            cn=(i-j)
print(cn*-1)

2 당신의분할은 100점

arr = list(map(int, input().split()))
cnt = 0
sum_index = 0
sum_value = 0
for i in range(len(arr)):
    sum_index+=i
    sum_value+=arr[i]
    if sum_index == sum_value:
        cnt+=1
print(cnt)

3 최강의패 60점  2오답

a='5 2 52 100'
b=list(map(int,a.split()))
#print(b)  #[5, 2, 52, 100]
from itertools import permutations
aa=list(permutations(b, len(b)))
#print(aa)
stt=[]
st=''
for i in aa:
    for j in i:
        st+=str(j)
        #print(''.join(str(j)))
    stt.append(st)
    st=''
print(max(stt))

6 덧셈을 모르는 체셔  100점

a=input()
if len(a) == 4 :
    print(20)
elif len(a) == 3 :
    if int(a[0]) == 1 :
        print( 10 + int(a[2]))
    elif  int(a[0]) != 0 :
        print(10 + int(a[0]))
elif len(a) == 2 :
    if int(a[0]) == 0 :
        print(a[1])
    elif int(a[1]) == 0 :     
        print(a[0])
    else:
        print(int(a[0])+int(a[1]))

7 숫자 나라 특허 전쟁 100점

a=int(input())
rr=0
for i in range(1,a):
    if i % 3 == 0 and i % 5 == 0 :
        rr+=i 
    elif i % 3 == 0   :
        rr+=i
    elif i % 5 == 0 :
        rr+=i 
print(rr)

10 엘리스의동물어수업 100점  3오답

a=input()
b=input()
from collections import Counter
count=0
for i in range(int(b)):
    c=input()
    cc=Counter(c)
    if len(cc) <= int(a):
        count += 1
print(count)