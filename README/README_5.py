'''
variable (변하는 상태) vs constant (변하지 않는 상태)

그중에서 variable 은 분류가 가능합니다.
분류기준을 두고, 나누는데

크게 2분하면
cate, norminal(=: name)
다시 cate 는 ordinal(=: order), numeric (=: number)

그래서 결국은
ordinal, numeric, norminal
변수의 편집방향은 곧 위 3중에 한가지 선택사항으로 
주관식 -> 객관식

이곳(확률통계코딩)은 정답 보다는 적합하다. 라는 개념입니다.

embarked 
교과서 138 누락된 값 처리 방식이 나옴
지금 이 embarked 지우면 안되고 즉 dropna 를 쓰면 안되고
139페이지 대체하는 방식을 사용해야 함. 

여기서 null 값을 무엇으로 넣을 것인가 ?
평균값을 넣자고 책에는 돼있어요.

그러나 이 예제는 str 잖아요. 평균을 구할 수 없어요. 
그래서 이렇게들 합니다. 
가장 많이 승선한 항구로 대체하자.
물론 통계를 왜곡할 수 있지만 그 null 의 수가 적으니 무시하자.
왜냐하면 빈값이 있으면 아예 그 변수를 사용할 수 없어서 
그것보다는 차선을 택하자는 생각입니다. 

이 예제에서는 사우스햄튼에서 승선객의 비율이 높아서 s 로 대체하기로 합니다. 

# 변수명은 ['변수명 '] , 변수값은 {'변수값'}

  @staticmethod
    def sex_norminal(this) -> object:
        # male = 0, female = 1 map 데이터분석시 성별은 반드시 작업이 필요함.  
        this.train['Sex'] = this.train['Sex'].map({'male':0, 'female':1}) # 변수명은 ['변수명 '] , 변수값은 {'변수값'}
        this.test['Sex'] = this.test['Sex'].map({'male':0, 'female':1})
        return this  

코딩은 반복된 코드를 싫어합니다.
for(), while() 이 syntax 가 존재하는 이유.

그래서 위 코드에서 반복을 피하기 위해 (지도학습의 숙명인 train과 test 둘다 편집해야 하는 상황)
다음과 같은 코드가 나옵니다. 

  @staticmethod
    def sex_norminal(this) -> object: 
        # male = 0, female = 1   
        combine = [this.train, this.test] # train과  test가 묶입니다. 
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        this.train = this.train # overriding  덮어쓰기
        this.test = this.tes 
        return this    

이렇게 기존에 있는걸 바꿔치기했음. 
여러분이 주신 코드가 가독성이 훨씬 좋습니다만, 우리가 배우는 입장에서
추가한 것으로 이해바랍니다 변수가 많을 경우에는 이게 더 좋음. 

process
Data 수집 
    - 빙법론
    - 장향 (csv) = 스키마구조 존재. Computer 인식 엑셀 메타데이터 존재하니까 종류는 항상 두가지 존재,비존재에 따라서 나뉜다. 
    - 비정형 ()  = 스키마구조 존재하지 않다. Computor 인식 불가
        - 웹 -> 웹 크롤링 -> 브라우저, RE 정규표현식 
        - 문서 -> 텍스트 마이닝 -> RE 정규표현식  (영상도 포함됨)
Data 정제, 정형화
Modeling 
Learning
Machine
Evaluation


#################### 정규 표현식 re #####################

? : unique
* : all 
+ : not null 
{n} : counting 


([A-Za-z]+) [] 문자 알파벳 , 한글: [ㄱ-힣]
 +  몇 개 있어도 상관없는데 없으면 안되는거 반드시 알파벳이여야 되는거. 
'''
