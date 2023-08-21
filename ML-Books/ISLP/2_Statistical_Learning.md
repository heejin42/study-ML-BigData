# ISLP (Introduction of Statistical Learning by Python)
# 2. Statistical Learning 

## 2.1 What is statistical learning?
Imagine: We are statistical consultants. From client, we get advertising and sales data. It's impossible to directly increase sales of product, but we can control the advertising expenditure. So we can increase salse indirectly.    
SO, Our goal is to develop an accurate model to predict sales on the basis of the three media budgets.
input variables - the advertising budgets    
output variable - sales   
X1 TV budget, X2 the radio budget, and X3 the newspaper budget.   
Y =f(X)+ε.
![img](./img/advertising_sales.png)

### 2.1.1 Why Estimate f(x)?
Prediction   
In many situations, a set of inputs X are readily available, but the output Y cannot be easily obtained. In this setting, since the error term averages to zero, we can predict Y using Y = f(X), where fˆ represents our estimate for f, and Yˆ represents the resulting pre- diction for Y.

Accuracy of Yˆ as a prediction for Y
1) reducible error
    In general, fˆ will not be a perfect estimate for f. This inaccuracy will introduce some error.
2) irreducible error
    Even if it were possible to form a perfect estimate for f, estimated response took the form Yˆ = f(X), we still have some error. Because Y is also a function of ε, which, by definition, cannot be predicted using X.   

**E(Y-Y^)<sup>2</sup>** = **E[f(X) + ε f^(X)]<sup>2</sup>** = **[f[X]-f^[X]]<sup>2</sup> + Var(ε)** = **Reducible + Irreducible**


### 2.1.2 How Do We Estimate f?
- Parametric Methods
- Non-Parametric Methods

### 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability

### 2.1.4 Supervised Versus Unsupervised Learning

### 2.1.5 Regression Versus Classification Problems