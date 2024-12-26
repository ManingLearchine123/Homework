# 람다 함수를 사용하여 주어진 리스트의 모든 요소를 제곱하는 함수를 작성하세요
a = lambda x: x**2
# map() 함수와 람다 함수를 사용하여 문자열 리스트의 각 단어의 길이를 구하는 코드를 작성하세요
numbers = ["abc","cb"]
a = list(map(lambda x: len(x), numbers))
# filter() 함수를 사용하여 #부터 #까지의 숫자 중 짝수만 선택하는 코드를 작성하세요
a = list(filter(lambda x: x%2==0, range(0,11)))
# reduce() 함수를 사용하여 리스트의 모든 요소를 곱하는 함수를 작성하세요
from functools import reduce
a = reduce(lambda x,y:x*y,range(1,11))
# 재귀 함수를 사용하여 팩토리얼(n!)을 계산하는 함수`factorial`을 작성하세요
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
# 데코레이터를 만들어 함수의 실행 시간을 측정하는 코드를 작성하세요
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds")
        return result
    return wrapper
@timer
def abc():
    print("Hello, world!")
# 'Person' 클래스를 정의하고, 이름과 나이를 속성으로 가지며, 자기 소개를 하는 메서드를 포함하세요
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f'제 이름은 {self.name}이고 나이는 {self.age}살 입니다.')
a = Person("Tteokbokki",11)