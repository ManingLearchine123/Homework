# 1번 문제
# greetings.py 생성

def say_hello():
    return "안녕하세요"

def say_goodbye():
    return "안녕히 가세요"

def say_good_morning():
    return "좋은 아침입니다"

# greetings.py 모듈 임포트
import greetings

# 함수 호출 및 결과 출력
print(greetings.say_hello())
print(greetings.say_goodbye())
print(greetings.say_good_morning())

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다. 값을 확인해주세요!"

import calculator

first_number = float(input("첫 번째 숫자를 입력하세요: "))
second_number = float(input("두 번째 숫자를 입력하세요: "))

#각
print(f"덧셈: {calculator.add(first_number, second_number)}")
print(f"뺄셈: {calculator.subtract(first_number, second_number)}")
print(f"곱셈: {calculator.multiply(first_number, second_number)}")
print(f"나눗셈: {calculator.divide(first_number, second_number)}")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다. 값을 확인해주세요!"

from simple_math import basic_operations, advanced_operations

first_number = float(input("첫 번째 숫자를 입력하세요: "))
second_number = float(input("두 번째 숫자를 입력하세요: "))

print(f"덧셈: {basic_operations.add(first_number, second_number)}")
print(f"뺄셈: {basic_operations.subtract(first_number, second_number)}")
print(f"곱셈: {advanced_operations.multiply(first_number, second_number)}")
print(f"나눗셈: {advanced_operations.divide(first_number, second_number)}")

# 4번 문제
# file_handler.py 생성
with open('file_handler.py', 'w') as f:
    f.write("""
import csv

def write_text_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def read_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "파일이 존재하지 않습니다. 확인해주세요!"

def write_csv_file(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def read_csv_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        return "파일이 존재하지 않습니다. 확인해주세요!"
""")

# file_handler 모듈 임포트
import file_handler

# 텍스트 파일 테스트
file_handler.write_text_file("sample.txt", "제가 만든 파일핸들러로\n텍스트 파일을 만들거에요!")
print(file_handler.read_text_file("sample.txt"))

# CSV 파일 테스트
test_data = [["이름", "직책"], ["최장범", "매니저"], ["양봉현", "튜터"], ["원유선", "튜터"]]
file_handler.write_csv_file("sample.csv", test_data)
print(file_handler.read_csv_file("sample.csv"))