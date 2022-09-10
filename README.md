# Project1 (JS_B_Stardust): 두피 자가진단 시스템 <br> 2022-08-11 ~ 2022-09-05 https://github.com/hope69034/developer.SH/issues/3
<img src="https://user-images.githubusercontent.com/108075604/188791960-6ca55e8f-757e-4b4e-ae9a-65ace5d6c754.gif"> 

## 시스템 설명

### 1. 모델6개 학습

```python
각 증상의 중증도에 따라 0, 1, 2, 3 으로 분류하는 모델이다. (0:양호, 1:경증, 2:중등도, 3:중증) 
 model1_train.py : 미세각질       
 model2_train.py : 피지과다     
 model3_train.py : 모낭사이홍반   
 model4_train.py : 모낭홍반농포   
 model5_train.py : 비듬         
 model6_train.py : 탈모         
```
### 2. 위 모델6개로 사용자의 두피이미지에 대한 프레딕트 값 6개를 얻는다

### 3. 6개의 프레딕트 값을 기반으로 진단 기준에 따라 두피 타입을 진단한다.

```python
    d_list = [] # 두피유형진단결과
    # 두피 유형 진단법
    if m1p == 0 and m2p == 0 and m3p == 0 and m4p == 0 and m5p == 0 and m6p == 0 :
        d1 = '정상입니다.'
        d_list.append(d1)
    elif m1p != 0 and m2p == 0 and m3p == 0 and m4p == 0 and m5p == 0 and m6p == 0 :
        d2 = '건성 두피입니다.'
        d_list.append(d2)
    elif m1p == 0 and m2p != 0 and m3p == 0 and m4p == 0 and m5p == 0 and m6p == 0 :
        d3 = '지성 두피입니다.'
        d_list.append(d3)
    elif m2p == 0 and m3p != 0 and m4p == 0 and m5p == 0 and m6p == 0 :
        d4 = '민감성 두피입니다.'
        d_list.append(d4)
    elif m2p != 0 and m3p != 0 and m4p == 0 and m6p == 0 :
        d5 = '지루성 두피입니다.'
        d_list.append(d5)
    elif m3p == 0 and m4p != 0 and m6p == 0 :
        d6 = '염증성 두피입니다.'
        d_list.append(d6)
    elif m3p == 0 and m4p == 0 and m5p != 0 and m6p == 0 :
        d7 = '비듬성 두피입니다.'
        d_list.append(d7)
    elif m1p == 0 and m2p != 0 and m3p == 0 and m4p == 0 and m5p == 0 and m6p != 0 :
        d8 = '탈모입니다.'
        d_list.append(d8)
    else:
        d9 = '복합성 두피입니다.'
        d_list.append(d9) 
``` 
        
### 4. 두피 타입에 맞는 정보와 관련 제품을 추천한다.
