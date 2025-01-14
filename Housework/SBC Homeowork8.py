class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())
print(rect.perimeter)

def greet(name):  # name은 매개변수
    return f"안녕하세요 {name}님!"

greet("봉현")  # "봉현"은 인자

'''Hello, Alice!
Hi, Bob!'''

# 4. *args와 **kwargs의 차이점과 사용 목적을 설명하세요.

# *args: 가변 개수(갯수가 변할 수 있다는 뜻)의 "위치" 인자 => "튜플" 형태로 전달

# 함수 호출 시 "몇 개의 위치 인자를 전달할지 알 수 없을 때" 사용
# 순서대로 전달됨 즉, 위치 기반이기 때문에 함수의 일반 매개변수 "다음에" 와야 함!

def sum_numbers(*args):
    print(f"args: {args}") # 튜플로 전달
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))
# args: (1, 2, 3, 4, 5)
# 15

# **kwargs: 가변 개수의 "키워드" 인자 => "딕셔너리" 형태로 전달

def introduce_person(**kwargs):
    print(f"kwargs: {kwargs}")  # 딕셔너리로 전달
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce_person(name="양봉현", age=100, hobby="개발")
# kwargs: {'name': '양봉현', 'age': 100, 'hobby': '개발'}
# name: 양봉현
# age: 100
# hobby: 개발

# 두개 동시에 쓸 수 있을까?
# 가능하지만 "순서"가 있음 => *args가 먼저 오고 **kwargs가 나중에 와야 함

# def introduce(**kwargs, *args):
#     print("args:", kwargs) # 위치 인자는 튜플로 출력
#     print("kwargs:", args) # 키워드 인자는 딕셔너리로 출력

def introduce(*args, **kwargs):
    print("args:", args) # 위치 인자는 튜플로 출력
    print("kwargs:", kwargs) # 키워드 인자는 딕셔너리로 출력

introduce(1, 2, 3, 5, name="양봉현", age=100)
# 출력:
# args: (1, 2, 3)
# kwargs: {'name': '양봉현', 'age': 100}

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, numbers))
print(result)  # [1, 4, 9, 16, 25]

class Calculation:
    def __init__(self, value):
        self.value = value # 속성

    def double(self): # 메서드
        return self.value * 2

calc = Calculation(2)
result = calc.double()
print(result)

# __init__: 객체 생성 시 호출되며 "초기값 설정"
# __del__: 객체가 삭제될 때 호출되며 자원을 "정리"
class Demo:
    def __init__(self):
        print("객체가 생성되었어요!")

    def __del__(self):
        print("객체가 삭제되었어요!")

obj = Demo()
del obj

# 클래스 메서드: @classmethod 데코레이터, "클래스 자체"를 첫 번째 인자로 받음 (관례적으로 cls 받습니다. 바꿀수는 있는데 개발자들끼리 국룰)
# 정적 메서드: @staticmethod 데코레이터, 클래스나 인스턴스와 "관계없이" 동작

class School:
    total_students = 0 # 전체 학생 수

    @classmethod
    def add_student(cls):
        cls.total_students += 1 # 학생 수 증가

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    @staticmethod
    def get_school_start_time():
        return "학교는 아침 9시에 시작합니다!"

# 학생 입학함
School.add_student()
School.add_student()

# 전체 학생 수 확인
print(School.get_total_students())  # 2

# 학교 시작 시간 확인
print(School.get_school_start_time())  # 학교는 아침 9시에 시작합니다!

# 예시에서의 클래스 메서드는 학교 전체의 학생 수를 관리하는데 사용
# 새로운 학생이 들어오면 학교는 전체 학생 수를 늘려야 하는데 이때 학생을 셀 수 있는 방법을 만들어야 함!
# add_student()는 학생 수를 늘리고, get_total_students()는 학생 수를 파악하는 역할의 메서드
# 학교 "그 자체"를 관리하는 역할이기 때문에 @classmethod, cls를 사용

# 예시에서의 정적 메서드는 학교의 시작시간을 알려주는데 사용
# 학생들이 학교에 오기 전에 매일 학교의 시작 시간을 알고 싶어함. 그런데 이 정보는 "모든 학생"에게 똑같으며 학생 수와 상관없이 "고정된 정보"
# 학교의 상태를 바꾸지 않고 "단순히 시작시간을 알려주는 일"을 함


# 상속이란?
# 기존 클래스(부모 클래스)의 "속성과 메서드"를 물려받아 새로운 클래스를 정의하는 것


# 부모 클래스: 상속을 제공하는 기존 클래스
# 자식 클래스: 부모 클래스를 상속받아 정의된 새로운 클래스

# 목적:
# 코드 재사용: 중복을 줄이면서 기존 코드를 활용하여 효율적으로 설계 가능
# 유지보수성 향상: 부모 클래스를 수정하면 이를 상속받은 자식 클래스에도 반영 가능
# 기능 확장: 부모 클래스의 기능을 바탕으로 새로운 기능 추가 가능

class Animal: # 부모 클래스
    def speak(self):
        return "짖을 수 있어요!"

class Dog(Animal): # 자식 클래스
    def speak(self):
        return "멍멍!"

dog = Dog() # Dog 객체 생성
print(dog.speak()) # 멍멍! => speak() 메서드 오버라이딩

# 자식 => 부모클래스 메서드 호출하려면?
# super()를 사용하자!
class Animal:
    def speak(self):
        return "짖을 수 있어요!"

class Dog(Animal):
    def speak(self):
        # 부모 클래스의 speak() 호출
        parent_message = super().speak()
        return f"{parent_message} 하지만 강아지니까 멍멍!"

dog = Dog()
print(dog.speak())
# 짖을 수 있어요! 하지만 강아지기 떄문에 멍멍!

# 10. 데코레이터의 기능과 사용 목적을 설명하세요.

# 기능: 함수나 메서드의 동작을 "변경 또는 확장"
# 목적: 코드 재사용성과 가독성을 높이기 위함

def decorator(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")
    return wrapper

@decorator
def say_hello():
    print("안녕!")

say_hello()

# 11. 다음 코드에서 프로퍼티(property)의 역할을 설명하세요:

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._property = "값"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

# 역할: 속성 접근을 "제어"하는 데 사용
# 게터(@property)와 세터(@property.setter) 정의, 유효성 검증 가능!
# 양수만 받는다

circle = Circle(5)
print(circle.radius)  # 5
circle.radius = 10
print(circle.radius)  # 10
circle.radius = -5  # ValueError: Radius cannot be negative