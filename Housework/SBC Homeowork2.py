# 사용자의 이름을 입력받아 "안녕하세요, [이름]님!"이라고 출력하는 함수`say_hello`를 작성하세요
s = lambda x: print(f"안녕하세요, {x}님!")
s("[이름]")
def say_hello(n):
    print('안녕하세요,',n+'님!')
say_hello('[이름]')
# 두 개의 숫자를 입력받아 큰 수를 반환하는 함수`find_larger`를 작성하세요
s = lambda x,y: x if x>y else y
def find_larger(x,y):
    if x>y:
        return x
    else:
        return y
print(find_larger(1,3))
print(s(3,1))
# 리스트를 입력받아 그 리스트의 첫 번째 요소와 마지막 요소를 출력하는 함수`print_first_last`를 작성하세요
def print_first_last(a):
    print(a[0],a[-1])
s = lambda x: print(x[0], x[-1])
print_first_last([1,2,3])
print(s([1,2,3]))
# 숫자를 하나 입력받아 그 숫자가 짝수인지 홀수인지 출력하는 함수`even_or_odd`를 작성하세요
def even_or_odd(a):
    if a % 2 == 0:
        print('Jjak sooh')
    else:
        print('Hol sooh')
even_or_odd(1)
s = lambda x: print('Jjak sooh') if x%2==0 else print('Hol sooh')
s(1)
# 문자열을 입력받아 그 문자열을 대문자로 변환하여 반환하는 함수`to_uppercase`를 작성하세요
def to_uppercase(x):
    return str(x).upper()
print(to_uppercase('abc'))
s = lambda x: str(x).upper()
print(s("abc"))
# 두 숫자를 입력받아 더한 결과를 반환하는 함수`add_numbers`를 작성하세요
def add_numbers(x,y):
    return x+y
print(add_numbers(1,3))
s = lambda x,y: x+y
print(s(1,3))
# 리스트를 입력받아 모든 요소의 합을 반환하는 함수`sum_list`를 작성하세요 (내장 함수 sum을 사용하지 않고 구현해보세요)
l = [1,3]
def sum_list(x):
    y=0
    for i in x:
        y+=i
    return y
print(sum_list(l))
s = lambda x: sum(x)
print(s(l))
# 임의의 개수의 숫자를 입력받아 그 평균을 계산하는 함수`calculate_average`를 작성하세요 (가변 인자를 사용하세요)
def calculate_average(*x):
    return sum(x)/len(x)
print(calculate_average(1,2,3))
s = lambda *x: sum(x)/len(x)
print(s(1,2,3))
# 문자열을 입력받아 그 문자열의 길이를 반환하는 람다 함수를 작성하세요
def lambda(x):
    return len(x)
print(lambda('1,3'))
s = lambda x: len(x)
print(s('1 3'))
# 재귀 함수를 사용하여 팩토리얼(n!)을 계산하는 함수`factorial`을 작성하세요
# lambda 안되네요 ㅠ
def factorial(x):
    f=x
    for i in range(1,int(x),1):
        x *= f-i
factorial(3)
# 딕셔너리를 입력받아 키와 값을 바꾼 새로운 딕셔너리를 반환하는 함수`swap_dict`를 작성하세요
def swap_dict(d):
    s = {v:k for k,v in d.items()}
    return print(s)
swap_dict({'a':1})
# 기본 매개변수를 사용하여 인사말을 출력하는 함수`greet`를 작성하세요 이름이 주어지지 않으면 "Guest"라고 인사하도록 합니다
def greet(a="안녕 안녕 안녕 Guest"):
    if a=="안녕 안녕 안녕 Guest":
        print(a)
    else:
        print("안녕 안녕 안녕",a)

greet('A')