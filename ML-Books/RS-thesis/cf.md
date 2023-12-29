# Collaborative Filtering for Implicit Feedback Datasets
Recommender systems provide users with personalized recommendations for products for services, which hopefully suit their unique tasts and needs.   
The technology is based on systems of profiling users and prodcuts, and finding how to related them.   

### Two different strategies
1. Contents based approach   
- Create a profile for each user or product to characterize its
- User profiles(demographic information or answers to suitable questionnaire) to matching products
- It requires gathering external information 

2. Collaborative Filtering
- It relies only on past user behavior without explicit profiles
- It analyzes relationships between users and interdenpendencies(상호의존성) among products -> identify new user-item associations
- Major appleal of CF is domain-free: 도메인을 가리지 않고 콘텐츠 기반으로 프로파일링 하기 어려운 데이터도 다룰 수 있다. 그러나 콘텐츠 기반 방식이 이미 적합한 곳에는 적용하기 어려운 cold-start 문제가 있다.

명시적인 피드백을 보통 다뤄왔지만, 명시적인 피드백보다 암시적인 피드백에서 유저의 선호를 찾는 것이 관건이다. 예를 들어 유튜브 좋아요, 싫어요 버튼을 클릭한 데이터, 구매 기록보다 브라우징 기록, 시청 기록, 검색 패턴, 심지어 마우스 움직임 데이터까지 사용할 수 있을 것이다. 다음으로는 암시적인 피드백을 활용하는 추천시스템의 주요 특징을 살펴보겠다.

1. **No negative feedback.** 암시적인 데이터에서 좋아하는 선호에 대해 파악하는 것은 가능하지만 불호에 대해 파악하는 것은 쉽지 않다. 예를 들어, 영상 시청 기록에서 특정 영상을 보지 않았다면 그 콘텐츠를 싫어하는 것이라고 판단할 수 없다. 콘텐츠의 존재 여부를 몰랐을 수도 있고, 비교적 다른 콘텐츠가 더 선호였기 때문일 수도 있다. 그러므로 부정적인 피드백을 찾을 수 있는 데이터가 누락되지는 않았는지 파악하는 것이 중요하다.
2. **Implicit feedback is inherently noisy.** 예를 들어, 개인의 구매행동을 볼 수는 있지만 그것이 선물을 위한 것일 수도 있고 사용자가 그 상품에 실망했을 수도 있다. 혹은 TV 시청 기록에서 실제로 시청을 했을지, 그냥 틀어놓고 다른 행동을 했을지 모른다. 그러므로 암시적인 데이터는 본질적으로 노이즈가 많다는 것을 명심해야한다.
3. **The numerical value of implicit feedback indicates confidence.** 명시적인 데이터의 수치값은 선호도를 나타내지만, 암시적 데이터의 수치값은 확신의 정도를 나타낸다. 큰 값을 가지고 있다고 해서 선호도가 높은 것이 아닌 가능성이 높은 것이라고 이해해야하며, 일회성의 이벤트는 사용자의 의지와 관계없이 발생할 수 있기 때문에 여러 번 발생할수록 사용자의 의견이나 의지가 많이 반영되었다고 할 수 있다.
4. **Evaluationofimplicit-feedbackrecommenderrequires appropriate measures.**  암시적 모델을 통해 우리는 품목의 가용성, 다른 품목과의 경쟁, 그리고 반복적인 피드백을 고려해야 한다. 예를 들어, 우리가 텔레비전 시청에 대한 데이터를 수집한다면, 한 번 이상 시청된 쇼를 평가하는 방법, 또는 동시에 켜져 있는 두 개의 쇼를 비교하는 방법은 불분명하며, 따라서 사용자가 둘 다 볼 수 없다.


## Preliminaries
사용자와 항목을 구별하기 위한 특별 인덱싱 문자를 사용하겠다. 사용자 u, v, 그리고 항목 i, j, 입력 데이터는 r<sub>ui</sub> 값을 통해 사용자와 항목을 연관시키며, 그것을 observation이라고 부르겠다. 명시적인 피드백 데이터 세트의 경우, observation은 선호도를 의미하는 항목 i의 사용자 u의 선호도를 나타내는 등급이 될 것이다. 암시적 피드백 데이터 세트의 경우, observation은 사용자 행동에 대한 관찰을 나타낼 것이다. 예를 들어, r<sub>ui</sub>는 아이템 i를 구매한 횟수 또는 웹 페이지 i에 보낸 시간을 나타낼 수 있다. 예를 들어, r<sub>ui</sub> = 0.7은 당신이 쇼의 70%를 시청했음을 나타내는 반면, 쇼를 두 번 본 사용자의 경우 r<sub>ui</sub>=2를 설정할 것이다.

## Previos work
### Neighborhood models 
CF의 가장 일반적인 접근 방식은 Neighborhood models, 이웃 기반 모델을 바탕으로 하는 방식이다. all earier CF systems is user-oriendted. 사용자 지향적인 이웃 기반 모델은 비슷한 생각을 가진 사용자들끼리 같은 등급을 매기는 식으로 진행한다. 그 뒤로 item-oriented methods가 나왔는데, 이 방식은 유사한 항목에 대해 사용자가 매긴 등급을 참고한다. 일반적으로 아이템 지향적인 방식이 more amenable하다. 왜냐하면 사용자가 이전에 선호했던 항목에는 익숙하지만, 일반적으로 같은 생각을 가진 사용자를 알기는 힘들기 때문이다.   
대부분의 아이템 지향적인 접근 방식의 중심에는 아이템 간의 유사도를 계산하는 문제가 있다. 아이템 i와 아이템 j의 유사성을 s<sub>ij</sub> 라고 할 때, 그 값은 피어슨 상관 계수라고 할 수 있다. 우리의 목표는 아이템 i에 대해 사용자 u에게 아직 관찰되지 않은 가치를 r<sub>ui</sub>를 예측하는 것이다. 그러기 위해서는 u가 평가한 항목 중 i와 가장 유사한 항목 k개를 식별해야 한다. 이 K개의 이웃들은 S<sup>k</sup>(i;u)로 표시되는데, r<sub>ui</sub>값은 이 아이템들 'S<sup>k</sup>(i;u)'의 등급에 대한 가중치를 갖게 된다.   
**r<sub>ui</sub> = j∈S<sup>k</sup>(i;u)<sup>s<sub>ij</sub>r<sub>uj</sub></sup> 들의 합 / j∈S<sup>k</sup>(i;u)<sup>s<sub>ij</sub></sup> 들의 합**   
위 구조는 사용자와 아이템에 대한 다양한 수치 평균과 같은 명시적인 피드백에 잘 적용된다. 그러므로 암시적인 피드백에는 단점을 보이는데, 그 이유는 사용자의 선호나 신분을 구별할 수 있는 유연성이 없기 때문이다.

### Latent factor models
잠재 요인 모델은 관찰된 등급을 설명하는 잠재 기능을 다루기 위해 전체적인 목표를 가진 협업 필터링에 대한 대안적인 접근 방식을 제공한다. 이 방식은 사용자와 아이쳄 데이터 행렬의 특이값 분해 (SVD)로 유도된 모델을 사용한다. 
## Our model (collaborative filtering)

## Explaining recommendations

## Experimental study

## Discussion