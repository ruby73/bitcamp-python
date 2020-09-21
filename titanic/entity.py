class Entity:
    def __init__(self, context, fname, train, test, id, label):
        self.context = context # _ 1개 는 default 접근 의미, __ 2개는 private 의미 
        self.fname = fname
        self.train = train
        self.test = test
        self.id = id
        self.label = label

    # get, set 를 만듭니다.

    @property
    def context(self) -> str:  # str 은 파이썬에서 String 타입을 의미하고,  -> 은 리턴하는 타입을 표시합니다
        return self._context

    @context
    def context(self, context):
        self._context = context

    # fname get, set 를 만듭니다.
    @property
    def fname(self) -> str:
        return self.fname

    @context 
    def fname(self, fname):
        self.fname = fname

    # train get, set 를 만듭니다.
    @property
    def train(self) -> str:
        return self.train

    @context 
    def train(self, fname):
        self.train = train
    
    # test get, set 를 만듭니다.
    @property
    def test(self) -> str:
        return self.test

    @context 
    def test(self, test):
        self.test = test
    
    # id get, set 를 만듭니다.
    @property
    def id(self) -> str:
        return self.id

    @context 
    def id(self, fname):
        self.id = id
  
    # label get, set 를 만듭니다. 
    @property
    def label(self) -> str:
        return self.label

    @context 
    def label(self, fname):
        self.label = label


# 생존여부를 판단 할 수 있는 속성값은? 
# property와 일치하는 개념
# 피쳐(Feature)는 기계 학습과 패턴 인식의 용어이다. 
# 피쳐 벡터(feature vector)
# train.csv를 읽어들여야 하기 때문에 읽는 작업을 해야됨. 