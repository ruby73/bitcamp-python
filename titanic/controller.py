from service import Service
from entity import Entity
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


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
        print('hello')

    def modeling(self, train, test):
        service = self.service
        this = self.preprocessing(train, test)

        this.label = service.create_label(this)
        this.train = service.create_train(this)
        
        return this

    def preprocessing(self, train, test) -> object:
        service = self.service
        this = self.entity
        this.train = service.new_model(train)  # payload
        this.test = service.new_model(test) # payload
        this.id = this.test['PassengerId'] # machine(인스턴스 객체) 이에게는 이것이 qeustion 이 됩니다. 이 id는 
        print(f'드롭 전 변수 : {this.train.columns}')
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket') # 티켓번호 랜덤으로 날리기 때문에 필요 없음. 
        print(f'드롭 후 변수 : {this.train.columns}')
        return this


    def learning(self):
        pass

    def submit(self): # machine 이 된다. 이 단계에서는 캐글에게 내 머신이를 보내서 평가 받게 하는 단계입니다. 마치 수능장에 자식보낸 부모의 마음..
        pass

if __name__ == '__main__':
    ctrl = Controller()
    ctrl.modeling('train.csv', 'test.csv')

