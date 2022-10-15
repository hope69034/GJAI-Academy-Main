[2일차]

2. 병정369게임
ii=input().split()
at=ii[0]
bs=ii[1]
na = int(at)
nb = int(bs)
ttt=["3","6","9"]
count=0
for i in range(na,nb+1): # i int
    if i % 3 == 0:
        #print(i)
        count+=1
    else:
        for j in str(i):
            if j in ttt:
                count+=1
                #print(i)
print(count)