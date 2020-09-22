from dataclasses import dataclass

@dataclass
class Entity:
    # def __init__(self, context, fname, train, test, id, label):
    #     self._context = context # _ 1개 는 default 접근 의미, __ 2개는 private 의미 
    #     self._fname = fname
    # 의미는 똑같음. 간소화됨. 
    context: str = '/Users/KAREN/SbaProjects/titanic/data/'
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''

  

# 생존여부를 판단 할 수 있는 속성값은? 
# property와 일치하는 개념
# 피쳐(Feature)는 기계 학습과 패턴 인식의 용어이다. 
# 피쳐 벡터(feature vector)
# train.csv를 읽어들여야 하기 때문에 읽는 작업을 해야됨. 
# 이미 entity 설계는 10년차 이상이 설계 하기 때문에 왜 fname 이라고 하는지 몰라도 됨
# 추석 전까지 각 팀에 entity 이런거 다 결정하고 싶은 것. 

