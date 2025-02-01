# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)  # 최대 100자
    content = models.TextField()  # 긴 글을 저장은 TextField 사용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜 자동 기록
    updated_at = models.DateTimeField(auto_now=True)  # 수정 날짜 자동 갱신


a = int(input("숫자를 입력해라"))
if a>0:
    print('양수다')
if a<0:
    print('음수다')
else:
    print('모르겠다')
for i in range(1, 101):
    if i % 7 == 0:
        print(i)
start = int(input("첫 번째 숫자: "))
end = int(input("두 번째 숫자: "))

for i in range(min(start, end), max(start, end) + 1):
    print(i)
for i in range(1, 11):
    print(f"{i}의 제곱은 {i**2}입니다!")
text = input("문자열을 입력하세요: ")

for char in text:
    print(char)
total = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print("3의 배수이거나 5의 배수인 숫자의 합:", total)
n = int(input("숫자: "))

# 팩토리얼 계산
factorial = 1
for i in range(1, n + 1):
    print(i)
    factorial *= i
print(f"{n}!의 값은 {factorial}입니다!")
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
numbers = []
while True:
    num = int(input("숫자를 입력하세요! (0 입력시 종료): "))
    if num == 0:
        break
    numbers.append(num)

if numbers:
    average = sum(numbers) / len(numbers)
    print("숫자 평균:", average)
else:
    print("처음 입력하는 숫자는 0이 아니여야 합니다!")
for i in range(1, 6): # 별이 다섯개!
    print("*" * i)