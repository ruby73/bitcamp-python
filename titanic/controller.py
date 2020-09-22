from service import Service
from entity import Entity


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
        print('hello')

    

    def modeling(self, train, test):
        service = self.service
        this = self.preprocessing(train, test)
        print(f'훈련컬럼 : {this.train.columns}')
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def learning(self):
        pass

    def submit(self):
        
        pass

    def preprocessing(self, train, test) -> object:
        service = self.service
        this = self.entity
        this.train = service.new_model(train)  # payload
        this.test = service.new_model(test)
        return this


if __name__ == '__main__':
    ctrl = Controller()
    ctrl.modeling('train.csv', 'test.csv')