from entity import Entity
import sys
sys.path.insert(0, '/Users/KAREN/SbaProjects')
import numpy as np
import pandas as pd

'''
#### PassengerId  고객ID, 이건 문제
#### Survived 생존여부 -> 머신러닝 모델이 맞춰야 할 답
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
#### Ticket 티켓번호,
Fare 요금,
#### Cabin 객실번호,
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
    def create_label(this) -> object: # 변수라고 통칭 
        return this.train['Survived']  # label은 곧 답이 된다.

    @staticmethod
    def drop_feature(this, feature) -> object: # 삭제하는 것 까지 함. 
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)  # p.149 훈련, 테스트 세트로 나눔
        return this

    # 드롭피쳐를 해서 필요없는 변수를 제거한 후 
    # 남은 변수를 편집하는 함수(메소드)를 간결하게 답 하고 문제 빼고 필요없는거 빼고 남은것들 편집해야된다.  

    @staticmethod
    def pclass_ordinal(this) -> object: # Embarked 에서 이미 숫자로 바꿔줘서 안해도 됨
        return this 
 
    @staticmethod 
    def name_norminal(this) -> object:
        return this

    @staticmethod
    def sex_norminal(this) -> object: 
        # male = 0, female = 1   
        combine = [this.train, this.test] # train과  test가 묶입니다. 
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        this.train = this.train # overriding 
        this.test = this.tes 
        return this    
 
    @staticmethod 
    def age_ordinal(this) -> object: # age 1 count 개수 동반자가 몇명이냐는거니까 
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5) 
        test['Age'] = test['Age'].fillna(-0.5) 
        # age 를 평균으로 넣기도 애매하고, 다수결로 넣기도 너무 근거가 없다...
        # 특히 age 는 생존을 판단에서 가중치(weigth)가 상당하므로 디테일한 접근이 필요합니다.
        # 나이를 모르는 승객은 모르는 상태로 처리해야 값의 왜곡을 줄일수 있어서
        # -0.5 라는 경계값으로 처리했습니다.    
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] # 이 파트는 범위를 뜻합니다.
        # -1 이상 0 미만.... 60이상 기타....
        # [] 에 있으니 이것은 변수명이겠군요..라고 판단하셨으면 잘 이해한 겁니다. 
        # 지도학습, 숫자값을 보낼 것
        label = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']  
        # [] 은 변수명으로 선언되었음
        train['AgeGroup'] = pd.cut(train)['Age'], bins, labels=labels) # Band 처리
        test['AgeGroup'] = pd.cut(test)['Age'], bins, labels=labels) # Band 처리
        age_title_mapping = { # 이게 다시 값이 되버린것임. 34.5라는 애는 여기에서 없어짐. Young Adult이 5라는 것으로 다시 매칭되는것 
            0: 'Unknown',
            1: 'Baby',
            2: 'Child',
            3: 'Teenager',
            4: 'Student',
            5: 'Young Adult', 
            6: 'Adult',
            7: 'Senior'
        } # 이렇게 []에서 {} 으로 처리하면 labels 를 값으로 처리하겠네요. 
        
        return this  
        
    @staticmethod
    def sibSp_normeric(this) -> object:
        return this  

    @staticmethod
    def parch_normeric(this) -> object: # 동승자 count
        return this  
        
    @staticmethod
    def fare_ordinal(this) -> object:
        this.train['FareBand'] = pd.qcut(this['Fare'], 4, labels={1,2,3,4}) # 4등분 중에 하나를 하고 라벨링을 하는데 로우 데이터를 표시함. 
        this.test['FareBand'] = pd.qcut(this['Fare'], 4, labels={1,2,3,4})
        return this  

    @staticmethod 
    def fareBand_nominal(this) -> object: # 요금이 다양하니 클러스터링을 하기위한 준비
        this.train = this.train.fillna({'FarBand' : 1}) # 'FarBand'는 없는 변수인데 추가함
        this.test = this.test.fillna({'FarBand' : 1})  # {} 컬브레이스 1이라는 값을 집어넣어라 이거고 
        return this

    @staticmethod
    def embarked_norminal(this) -> object: 
        this.train = this.train.fiilna({'Embarked': 'S'}) # S가 가장 많아서 빈곳에 채움
        this.test = this.test.fiilna({'Embarked': 'S'}) # 교과서 144
        # 많은 머신러닝 라이브러리는 클래스 레이블이 "정수" 로 인코딩 되었다고 기대함
        # 교과서 146 문자 bule = 0, green = 1, red = 2 로 치환합니다.
        this.train['Embarked'] = this.train['Embarked'].map({'S' : 1, 'C' : 2, 'Q': 3}) # ordinal 아닙니다.
        this.test['Embarked'] = this.train['Embarked'].map({'S' : 1, 'C' : 2, 'Q': 3})    
        return this  


'''
    # 전처리 파트 하고 있음. 교과서 p.136, 142 그림 4-2 룬련레이블 만드는 코드 create_label
    #  @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']  # label은 곧 답이 된다.
    변수에 대한 분류
    카테고리컬, 너미널 

    
    '''