# GNN(Graph Neural Networt)
주로 딥러닝 모델은 CNN(Convolution Neural Network), RNN(Recurrent Neural Network), Transformer 등으로 발전해왔다. 하지만 이 신경망 모델들은 복잡한 구조나 다양한 관계를 지닌 문제에 대해서는 그 의미를 임베딩하는 것에 한계가 있었다. 그래서 제안된 GNN 모델은 그래프를 사용해서 다양한 관계를 임베딩할 수 있다는 장점이 있다. 

### 그래프(Graph)의 정의와 사용
그래프는 정점(Node or Vertex)와 그 노드들을 잇는 간선(Edge)들로 이루어진 자료구조로 G = (V, E)로 정의한다. 여기서 V는 정점의 집합, E는 간선의 집합이다. 여기서 간선의 방향이 존재하면 방향 그래프(directed graph), 방향이 없으면 무향 그래프(undirected graph)로 나눌 수 있고, 간선의 가중치가 있는지 없는지에 따라 weighted와 unweighted로 나눌 수 있다. 형태에 따라서는 단순 그래프(simple graph), 간선이 여러 개인 다중 그래프(multi graph), 이분 그래프(bipartite graph) 등으로 나눌 수 있다. 그렇다면 그래프를 Representation Learning에서 왜 사용하는 것일까?    

CNN은 유클리디안 공간에서 이미지를 행과 열로 구성된 픽셀들로 표현하여 특징을 추출한다. 또 LSTM에서는 자기 자신으로 돌아오는 recurrent 구조를 통해 시계열 데이터 sequence의 특징을 추출한다. Transformer는 self-attention 구조를 통해 중요한 부분을 병렬로 처리하며 특징을 추출한다. 그리고 **GNN**에서는 그래프 구조를 통해 관계적 특징을 추출한다. 그래서 원하는 데이터를 그래프로 잘 표현할 수 있다면 그 그래프를 통해 모델로 특징을 학습할 수 있다는 것이다. 그를 통해 얻을 수 있는 이점은 다음과 같다.
- 추상적 개념을 다루기 적합: 그래프는 복잡하게 연결되어 있는 데이터를 표현하기에 좋기 때문에 관계나 상호작용 같은 추상적인 개념을 다루기 적합하다. 둘 이상의 상호작용을 테이블처럼 정형화된 데이터로 표현하면 오히려 복잡해질 수 있지만 그래프를 사용하면 하나로 간단하게 표현할 수 있다.
- Non-Euclidian Space의 표현과 학습이 가능: 이미지, 텍스트, 정형 데이터 등의 많이 쓰이는 데이터는 대부분 격자 형태로 표현할 수 있기 때문에 유한한 실수의 2차원이나 3차원의 유클리디안 공간에 나타낼 수 있다. 하지만 sns 문자 데이터, 분자 데이터 등과 같이 일반적인 유클리디안 공간으로 표현할 수 없는 데이터를 Non-Euclidian space에 표현할 수 있게 된다.

## GNN이란?
https://glanceyes.com/entry/%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C-GNNGraph-Neural-Network%EC%99%80-%EC%9D%B4%EB%A5%BC-%EC%9D%91%EC%9A%A9%ED%95%9C-NGCFNeural-Graph-Collaborative-Filtering%EC%99%80-LightGCN


![url](./ML/Books/카카오 추천팀 논문/240802~.md)