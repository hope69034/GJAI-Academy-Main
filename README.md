# Project1 (JS_B_Stardust): 두피 자가진단 시스템 <br> 2022-08-11 ~ 2022-09-05 https://github.com/hope69034/developer.SH/issues/3
<img src="https://user-images.githubusercontent.com/108075604/188791960-6ca55e8f-757e-4b4e-ae9a-65ace5d6c754.gif"> 

## 시스템 설명

### 1. 모델6개 학습
https://github.com/hope69034/developer.SH/blob/main/%EA%B4%91%EC%A3%BC%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90%202022.08/JS_B_Stardust_Project/SD_Project_Final_Code/9_10_sd_project_train_add_graph.ipynb
```python
각 증상의 중증도에 따라 0, 1, 2, 3 으로 분류하는 모델이다. (0:양호, 1:경증, 2:중등도, 3:중증) 
 model1.py : 미세각질       
 model2.py : 피지과다     
 model3.py : 모낭사이홍반   
 model4.py : 모낭홍반농포   
 model5.py : 비듬         
 model6.py : 탈모
 
최종 모델 벨리셋 / 테스트셋 정확도 (낮은 컴퓨터 사양 탓에 batch size=2, 낮은 epochs 로 학습)
# 모델1
model1(미세각질) : 모델 생성 완료(epoch 15회 best val score : 63.4%)
train/val : 12739/3639
100%|██████████| 238/238 [03:01<00:00,  1.31it/s]
Test set: Average Loss: -1.9017, Accuracy: 289/476 (60.7143%)
# 모델2
model2(피지과다) : 모델 생성 완료(epoch 2회 best val score : 57.6%)
train/val : 56826/16236
100%|██████████| 662/662 [01:17<00:00,  8.54it/s]
Test set Accuracy: 324/662 (48.9426%)
# 모델3
model3(모낭사이홍반) : 모델 생성 완료(epoch 5회 best val score : 78.4)
train/val : 47726/13635
100%|██████████| 359/359 [03:24<00:00,  1.76it/s]
Test set: Average Loss: -2.2255, Accuracy: 461/718 (64.2061%)
# 모델4
model4(모낭홍반농포) : 모델 생성 완료(epoch 50회 best val score : 72.4)
train/val : 3750/1070
100%|██████████| 197/197 [01:32<00:00,  2.12it/s]
Test set: Average Loss: -3.4693, Accuracy: 281/394 (71.3198%)
# 모델5
model5(비듬) : 모델 생성 완료(epoch 5회 best val score : 73.4)
trian/val : 28873/8248
100%|██████████| 310/310 [02:31<00:00,  2.05it/s]
Test set: Average Loss: -2.0950, Accuracy: 370/620 (59.6774%)
# 모델6
model6(탈모) : 모델 생성 완료(epoch 8회(4회×2) best val score : 74.7)
trian/val : 18513/5288
100%|██████████| 577/577 [05:12<00:00,  1.85it/s]
Test set: Average Loss: -1.3145, Accuracy: 633/1154 (54.8527%)
```
### 2. 위 모델6개로 사용자의 두피이미지에 대한 프리딕트값 6개를 얻는다.

### 3. 위 6개의 프리딕트 값을 기반으로 다음 진단 기준에 따라 두피 타입을 진단한다.
https://github.com/hope69034/developer.SH/blob/main/%EA%B4%91%EC%A3%BC%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90%202022.08/JS_B_Stardust_Project/SD_Project_Final_Code/9_10_sd_project_web.ipynb

```python
#진단
d_list = []     # 두피유형진단결과
#두피 유형 진단법                    
if fm1p < 1  and fm2p < 1 and fm3p < 1 and fm4p < 1 and fm5p < 1 and fm6p < 1 :
    d1 = '정상입니다.'
    d_list.append(d1)
elif fm1p >= 1 and fm2p < 1 and fm3p < 1 and fm4p < 1 and fm5p < 1 and fm6p < 1 :
    d2 = '건성 두피입니다.' 
    d_list.append(d2)
elif fm1p < 1 and fm2p >=1  and fm3p < 1 and fm4p < 1 and fm5p < 1 and fm6p < 1 :
    d3 = '지성 두피입니다.'
    d_list.append(d3)
elif fm2p < 1 and fm3p >= 1 and fm4p < 1 and fm5p < 1  and fm6p < 1 :
    d4 = '민감성 두피입니다.'
    d_list.append(d4)
elif fm2p >= 1 and fm3p >= 1 and fm4p < 1 and fm6p < 1 :
    d5 = '지루성 두피입니다.'
    d_list.append(d5)
elif fm3p < 1 and fm4p  >= 1 and fm6p < 1 :
    d6 = '염증성 두피입니다.'
    d_list.append(d6)
elif fm3p < 1 and fm4p < 1 and fm5p >= 1 and fm6p < 1 :
    d7 = '비듬성 두피입니다.'
    d_list.append(d7)
elif fm1p < 1 and fm2p >= 1 and fm3p < 1 and fm4p < 1 and fm5p < 1 and fm6p >= 1 :
    d8 = '탈모입니다.'
    d_list.append(d8)
else:
    d9 = '복합성 두피입니다.'
    d_list.append(d9)
print(d_list[0])
``` 
        
### 4. 두피 타입에 맞는 정보와 관련 제품을 추천한다.

## 향후 발전 방향성

### 1. 모델 accuracy 향상.
### 2. 광고, 제휴 수수료를 통한 수익.
### 3. AI기술이 접목된 두피 전문 의료기구 개발 및 판매.
### 4. AI피부인식을 통한 자가피부진단시스템 개발 및 서비스, 전문 의료기구에 접목.
### 5. 반려동물 케어로의 확장.
<br><br><br>
<hr>
# Project2 (JS_B_*): *
2022-*-* ~ 2022-*-*
