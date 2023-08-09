# MLOps for MLE
## Chapter 2. Model Development
지금까지는 MLOps에서 데이터를 생성하고 축적하는 프로세스에 대해 알아보았다. 이번 챕터에서는 그 데이터를 활용해 머신러닝 모델을 학습하고 저장하는 프로세스를 배워보겠다. 앞에서 생성한 postgres server와 data generator, iris 데이터를 이용할 것이다. 

![img](model-development.png)

------------------------

# 실습 - 1
## Base Model Development
목표 - 모델을 학습하고 저장하는 기본적인 파이프라인을 작성한다.
패키지 설치 - pandas, scikit-learn, joblib
코드 - base_train.py, base_validate_saved_model.py



### 1) 학습 및 평가 데이터 선정
- sklearn.datasets 에서 load_iris 함수를 통해 iris 데이터를 불러오고 각각 X, y에 할당한다.
- sklearn.model_selection의 train_test_split 함수를 이용해 데이터를 학습&평가 데이터로 나눈다. 여기서 추후에 재현할 수 있도록 random_seed를 지정한다. 
    - 여기서 random_seed란? random 모듈을 사용한 무작위 공정은 수많은 경우의 수를 가지고 있다. 여기서 공정의 완전한 재현이 가능하게 만들어주는 것이 random 모듈의 seed() 함수로 무작위 결과를 특정한 값으로 고정한다.
- 분리된 데이터에서 학습 데이터를 X_train, y_train에 할당하고, 평가 데이터는 X_valid, y_valid에 할당한다.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True, as_frame=True)
X_train, X_vaild, y_train, y_valid = train_test_split(X, y, train_size=0.8, random_state=2023)
```

### 2) 모델 개발 및 학습
- 데이터를 scaling한다. 학습에 용이하게 데이터를 전처리하는 과정 중에 하나로 평균을 0 , 분산을 1로 조정하는 sklearn.preprocessing의 StandardScaler를 할당했다. 방법은 할당한 scaler를 fit_trainsform(X_train) 한 후, transform(X_valid)하면 된다. scaling 전 데이터와 후 데이터를 비교해서 확인해보자.
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_valid = scaler.transform(X_valid)

print(X_train.values[0])
print(scaled_X_train[0])

# [4.9 3.1 1.5 0.1]
# [-1.17088947  0.11301185 -1.34354813 -1.48656219]
```
- 모델을 학습한다. 사용할 모델은 sklearn.svm의 SVC로 먼저 모델을 classifier에 할당한다. 그리고 fit() 함수와 scaled_X_train, y_train 데이터를 이용한다. 학습한 모델에 predict() 함수를 적용해 주어진 데이터에 대한 예측값을 얻고 각각 train_pred와 valid_pred에 할당해준다.  

```python
from sklearn.svm import SVC
classifier = SVC()
classifier.fit(scaled_X_train, y_train)

train_pred = classifier.predict(scaled_X_train)
valid_pred = classifier.predict(scaled_X_valid)
```

- 정확도를 계산해보자. 정확도는 sklearn.metrics에서 제공하는 accuracy_score를 이용해서 계산한다.
```python
from sklearn.metrics import accuracy_score

train_acc = accuracy_score(y_true=y_train, y_pred=train_pred)
valid_acc = accuracy_score(y_true=y_valid, y_pred=valid_pred)

print("Train Accuracy : ", train_acc)
print("Valid Accuracy : ", valid_acc)

# Load Model Train Accuracy : 0.9833333333333333
# Load Model Valid Accuracy : 0.9666666666666667
```


### 3) 학습된 모델 저장
scikit-learn에서 공식적으로 권장하는 모델 저장 방법은 joblib 패키지를 이용하는 것이다. joblib,dump(model, "model_name") 형식의 코드를 실행하면 경로에 파일이 생성된다.

```python
import joblib
joblib.dump(scaler, "scaler.joblib")
joblib.dump(classifier, "classifier.joblib")
```

### 4) 저장된 모델 불러오기
다음은 모델이 정상적으로 저장이 되었는지 확인하고 검증해보겠다.

- 학습할 때 나눈 데이터를 똑같이 재현한다.
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True, as_frame=True)
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, random_state=2023)
```
- 저장된 모델들을 불러온다.
```python
import joblib

scaler_load = joblib.load("scaler.joblib")
classifier_load = joblib.load("classifier.joblib")
```
- 불러온 모델로 학습 및 평가 데이터를 예측해본다.
```python
scaled_X_train = scaler_load.transform(X_train)
scaled_X_valid = scaler_load.transform(X_valid)

load_train_pred = classifier_load.predict(scaled_X_train)
load_valid_pred = classifier_load.predict(scaled_X_valid)
```
- 정확도 계산해서 불러오기 전의 모델과 정확도가 같은지 비교해본다. 
```python
from sklearn.metrics import accuracy_score

load_train_acc = accuracy_score(y_true=y_train, y_pred=load_train_pred)
load_valid_acc = accuracy_score(y_true=y_valid, y_pred=load_valid_pred)

print("Load Model Train Accuracy :", load_train_acc)
print("Load Model Valid Accuracy :", load_valid_acc)

# Load Model Train Accuracy : 0.9833333333333333
# Load Model Valid Accuracy : 0.9666666666666667
```


------------------------


# 실습 - 2
## Model Pipeline