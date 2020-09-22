from entity import Entity

class Service(): # 기능을 담당하는 Service
    def __init__(self): 
        self.entity = Entity()

    def new_model(self, payload):
        pass
    
    @staticmethod
    def create_train(this):
        pass

    @staticmethod
    def create_label(this):
        pass

    @staticmethod
    def drop_feature(this):
        pass