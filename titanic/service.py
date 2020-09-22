from entity import Entity
import sys
sys.path.insert(0, '/Users/KAREN/SbaProjects')
import numpy as np
import pandas as pd

'''PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
'''


class Service:
    def __init__(self):
        self.entity = Entity()  # = @Autowired Entity entity

    def new_model(self, payload) -> object:
        this = self.entity
        this.fname = payload
        return pd.read_csv(this.context + this.fname)  # p.139 / df = tensor

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)  # train은 답이 제거된 데이터셋이다.

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']  # label은 곧 답이 된다.

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)  # p.149 훈련, 테스트 세트로 나눔