# 경사하강법  파이썬 코드 구현
# 참고 링크 - https://www.youtube.com/watch?v=KgH3ZWmMxLE

# 업데이트할 W = Learning Rate · ((ŷ-y)·x)의 평균
# 업데이트할 b = Learning Rate · (ŷ-y)의 평균

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = 0.2 * x + 0.5
plt.figure(figsize=(8,6))
plt.scatter(x, y)
plt.show()

# 선형 함수가 그려진 것을 확인할 수 있다.

def plot_prediction(pred, y):
    plt.figure(figsize=(8,6))
    plt.scatter(x, y)
    plt.scatter(x, pred)
    plt.show()  
    
# 실제값과 예측값을 확인할 수 있는 함수를 정의했다.
# 다음으로 w 함수를 만들자
# Gradient Descent 구현

w = np.random.uniform(-1, 1)
b = np.random.uniform(-1, 1)

learning_rate = 0.7
for epoch in range(200):
    y_pred = w*x + b
    error = np.abs(y_pred-y).mean()
    if error<0.001:
        break
    
    #gradient descent
    w_gred = learning_rate * ((y_pred-y)*x).mean()
    b_gred = learning_rate * (y_pred-y).mean()
    # weight, bias 갱신
    w = w - w_gred
    b = b - b_gred
    
    if epoch%5==0:
        y_pred = w*x + b
        plot_prediction(y_pred, y)
        

# 실제로 x는 x1, x2, x3 ... 많은 feature를 갖는다.
# 그 말은 weight도 그만큼 많다는 것으로 많은 w1, w2, w3 ... 들을 업데이트 해가게 될 것이다.