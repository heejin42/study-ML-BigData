# 경사하강법 (gradient_descent)
* 오차 - 예측값 함수의 값과 실제값의 차   
* 예측값 = ŷ = ax + b   
* 오차 = Σ(ŷ-y)   

## MSE (평균제곱오차)
1/nΣ(ŷ-y)<sup>2</sup> = 오차의 제곱들의 평균 = 손실함수 L   
손실함수는 2차식이며, 가장 낮은 부분을 구하는 것이 오차가 적어진다고 이해할 수 있다.   
손실함수 값이 가장 낮은 부분 == 기울기가 0인 부분   
즉, 손실함수의 기울기가 0이 될 때까지 찾아가는 것이 경사하강법이다.   

ŷ = 예측값 = wx + b (w: weight, b: bias)   
1/nΣ(ŷ-y)<sup>2</sup> = 1/nΣ(wx+b-y)<sup>2</sup>  

## w에 대한 편미분
식 - **∂/∂w(1/nΣ(wx+b-y)<sup>2</sup>)**   
   
**1) chain rule 적용하기**   
   > 위의 식을 w에 대해 편미분을 하여 w에 대한 기울기를 구해야 한다.      
   > -> W(gradient) = (1/n) Σ 2 * (wx+b-y) * x   
   > -> 2/nΣx(wx+b-y)   
   > -> 위 값을 w에 업데이트 해주면 된다.   

**2) learning-rate = 업데이트 W * 0.5, 0.05**   
   > 실제로 w 개수가 많기 때문에 weight update 의 정도를 작아지게 미세 조정하기 위한 방법으로 0.5 혹은 0.05 등을 곱해준다.   
   > 상수를 어차피 곱해주기 때문에 W(gradient) 상수를 무시해도 괜찮다.   

즉 최종적으로 LR * MEAN(x(wx+b-y))라고 할 수 있으며, wx+b = ŷ이므로 다시 한번 정리하면     
**업데이트할 weight** = **LR x MEAN(x(ŷ-y))** 

## b에 대한 편미분
식 - **∂/∂b(1/nΣ(wx+b-y)<sup>2</sup>)**  
   
**1) chain rule 적용하기**   
   > 위의 식을 b에 대해 편미분을 하여 w에 대한 기울기를 구해야 한다.   
   > -> b(gradient) = (1/n) Σ 2*(wx+b-y)   
   > -> 2/nΣ(wx+b-y)   
   > -> 위 값을 b에 업데이트 해주면 된다.   

**2) learning-rate = 업데이트 b * 0.5 or 0.05**   
   > 실제로 b 개수가 많기 때문에 bias update 의 정도를 작아지게 미세 조정하기 위한 방법으로 0.5 혹은 0.05 등을 곱해준다.   
   > 상수를 어차피 곱해주기 때문에 b(gradient) 상수를 무시해도 괜찮다.   

즉 최종적으로 LR * MEAN(wx+b-y)라고 할 수 있으며, wx+b = ŷ이므로 다시 한번 정리하면   
**업데이트할 bias** = **LR x MEAN(ŷ-y)**

## 최종 정리
* LR = Learning Rate   
* <sub>gd</sub>W =  LR · ((ŷ-y)·x)의 평균   
* <sub>gd</sub>b =  LR · (ŷ-y)의 평균   

1) w = w - gradient w   
2) b = b - gradient b    
두가지 변수를 계속 업데이트 해간다.   

