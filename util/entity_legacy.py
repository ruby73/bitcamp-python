class Entity:
    # entity 속성을 담당 entity + service = object 
    # 같은 컨셉을 공유하는 클래스의 집합.
    # 모델에 AI 개념이 없으면 web에서 말하는 모델이고
    # AI 개념이 존재하면 인공지능 model이 된다. 
    def __init__(self, context,  fname, train, test, id, label):
        self._context = context # _는 default 접근의미, __2개는 private 접근의미
        self._fname = fname
        self._train = train
        self._test = test
        self._id = id
        self._label = label

    # get, set
    # property로 되어있는 것은 리턴하는 구조고 데코레이터. 패턴이 유사한 형태 
    
    # context get, set
    @property
    def context(self) -> str: #str 은  python 에서 String타입을 의미, -> 은 리턴하는 타입을 표시합니다. 
        return self._context
    
    @context.setter
    def context(self, context):
        self._context = context    
    
    # fname get, set
    @property
    def fname(self) -> str:
        return self._fname
    
    @fname.setter
    def fname(self, fname):
        self._fname = fname
    

    # train get, set 
    @property
    def train(self) -> str:
        return self._train

    @train.setter
    def train(self, train):
        self._train = train

    # test get, set
    @property
    def test(self) -> str:
        return self._test

    @test.setter
    def test(self, test):
        self._test = test

    # id get, set
    @property
    def id(self) -> str:
        self._id = id
    
    @id.setter
    def id(self, test):
        self._id = id

    # label get, set
    @property
    def laber(self) -> str:
        return self._label
    
    @label.setter
    def label(self, label):
        self._label = label
    
    # 롬복 쓰기 전에 상황임. 
    # 옛날꺼.

