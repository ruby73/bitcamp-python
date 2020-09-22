class Entity:
    def __init__(self,context,fname,train,test,id,label):
        self._context = context # _ 1개는 default 접근을 의미, __ 2개는 private 접근을 의미한다
        self._fname = fname
        self._train = train
        self._test = test
        self._id = id
        self._label = label
    # context get, set 을 만든다

    # get, set 를 만듭니다.

    @property # 프로퍼티로 되어있는 것은 리턴하는 구조고 데코레이터. 패턴이 유사한 형태 
    def context(self) -> str:  # str 은 파이썬에서 String 타입을 의미하고,  -> 은 리턴하는 타입을 표시합니다
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    # fname get, set 를 만듭니다.
    @property
    def fname(self) -> str:
        return self._fname

    @fname.setter
    def fname(self, fname):
        self._fname = fname

    # train get, set 를 만듭니다.
    @property
    def train(self) -> str:
        return self._train

    @train.setter 
    def train(self, train):
        self._train = train
    
    # test get, set 를 만듭니다.
    @property
    def test(self) -> str:
        return self.test

    @test.setter 
    def test(self, test):
        self._test = test
    
    # id get, set 를 만듭니다.
    @property
    def id(self) -> str:
        return self.id

    @id.setter 
    def id(self, id):
        self._id = id
  
    # label get, set 를 만듭니다. 
    @property
    def label(self) -> str:
        return self.label

    @label.setter 
    def label(self, label):
        self._label = label


# 생존여부를 판단 할 수 있는 속성값은? 
# property와 일치하는 개념
# 피쳐(Feature)는 기계 학습과 패턴 인식의 용어이다. 
# 피쳐 벡터(feature vector)
# train.csv를 읽어들여야 하기 때문에 읽는 작업을 해야됨. 
# 이미 entity 설계는 10년차 이상이 설계 하기 때문에 왜 fname 이라고 하는지 몰라도 됨
# 추석 전까지 각 팀에 entity 이런거 다 결정하고 싶은 것. 

