머신러닝 = 기계학습 = ML( == Deep Learning)

ML : 지도, 비지도, 강화
ML Process 4 :(
    1. precprocession 
    2. modeling
    3. learning
    4. evaluation
    
ML  Alogrithm

1. 퍼셉트론(perceptron) -> 뉴런(neuron)
2. 회귀 
3. 분류 
4. SVM
5. Dtree
6. Kmean
7. PCA
8. R-forest -> RF
9. NLP
10. Deep learning -> DL 

여기까지가 chap 13입니다.
외워주세요. 
마치 지도를 외우듯이....

Tensorflow

비즈니스 로직 - service
processing 하는 파일명 
    precprocession 
    modeling
    learning, evaluation
    완성되면 submit (파일로 저장)

# 외부에 있는 파이썬 파일(.py)을 import 해야 속성, 기능을 사용할 수 있다. 
# 내부에서는 이것을 인스턴스화(instance) 해야 한다. 
# entity = Entity()
# 이때 소문자 entity 는 인스턴스라고 하고 이를 객체로 정의한다. 
# 대문자 Entity 는 클래스
# 라운드 브레이스가 있는 Entity() 는 생성자라고 한다. 
# 결론.. 객체지향(OOP)에서는 속성과 기능을 호출하는 구조로
# 두가지 방식이 있는데 
# calc = Calculator() 있다고 하면
# calc 는 인스턴스 객체가 되고
# Calculator 는 클래스 객체(스태틱)라고 한다..
# calc.sum() 하면 인스턴스 호출방식= 다이나믹
# Calculator.sum() 하면 클래스 호출 방식 = 스태틱이라고 한다. 

from titanic.entity import Entity
from titanic.service import Service
class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
