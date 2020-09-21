Object = 기능(function) + 속성(Property, Attribute, Feature) => 파라미터( AI 파트 )
하나의 { ... } 에 같이 있음
() 라운드 {} 컬 [] 스퀘어 브레이스는 총 3가지 (전 프로그래밍 공통)
() 컨티션, 파라미터존, 튜플
{} 블락, JSON, Dict(딕셔너리)
[] array, 
[[]] matrix

===> notation 이라 합니다.
===> 언어 기호학

기본적으로 컴공 0, 1 만이 존재합니다. 이진수 binary code

위키 Geoge bool 이란 사람 검색...
T, F 판단 1850년 --> 전선 (모스부호) --> 컴퓨터

선택지는 항상 두가지 중에 하나를 선택하는 구조 -> 컴공 해법

on, off 의 개념이다.
요소가 존재, 비존재 로 종류가 나뉜다. => Decision Tree (Origin AI 알고리즘)

Q. 객체지향 vs 함수형 프로그래밍 를 구분하는 기준은
무엇이 있고 없고 인가 ?
A ... 속성이 있으먄 객체지향, 없으면 함수형 프로그래밍

class Calculator:
    def __init__(self, num1, num2): 
    # 생성자 함수 ==>인스턴스(객체)만드는 함수 __언더스코어라고함. 2개를 사용. 접근제한 private (내부적으로 사용한다.) 

        self.num1 = num1     
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

클래스는 저장하는 파일이고, num1, num2 속성값을 갖고있기 때문에
calc는 객체 

def sum 은 함수고 

결론: 객체지향은 속성이 존재해야 한다. 그리고 속성을 정의하는 곳은 __init__ (속성파라미터 (외부에서 주입되는 값을 파라미터라고 함)) 이다. 

self 는 객체내부의 속성에 접근하는 키워드

객체속성은 은닉화때문에 반드시 self. 로만 접근할 수 있다. 
이는 보안의 기본처리이다. __init__은 클래스 내부에서만 접근한다. 

클래스 내부에서 메소드의 종류는 몇가지인가 ?
해석 : 
기준 : self  입니다. 
self exist dynamic -> 데이터를 메모리에서 메소드가 유효한 시간동안만 존재, 그 메소드가 소멸된 후 값은 self 에 저장된다 (저장위치가 움직이는 것)
self !exist static -> 반 영속적으로 저장됨.(프로젝트가 끝나면 서버 내리면 제거되는 형식)
dynamic 동적 , static 정적 

(self) 가 있으면 

@어노테이션 붙어있는  걸 static 메서드라고 함. 
