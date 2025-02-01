"""python -m venv myenv
source myenv/Scripts/activate
pip install django
django-admin --version()

django-admin startproject my_project
manage.py: 프로젝트 관리 명령어 실행 스크립트
my_project/__init__.py: 패키지로 인식되도록 하는 파일
my_project/settings.py: 프로젝트 설정 파일
my_project/urls.py: URL 라우팅 설정 파일
my_project/asgi.py: ASGI 설정 파일
python manage.py startapp user
python manage.py startapp post"""

a = input("이름을 입력해라")
print(f'안녕 {a}님')
for i in range(1,11):
    print(i)
a = int(input("숫자를 입력해라"))
if a>0:
    print('양수다')
if a<0:
    print('음수다')
else:
    print('모르겠다')
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
total = 0
for _ in range(5):
    num = int(input("숫자를 입력하세요: "))
    total += num
print(f"합계: {total}")
for i in range(1, 10):
    print(f"2 x {i} = {2 * i}")
n = int(input("숫자를 입력하세요: "))
total = sum(range(1, n + 1))
print(f"1부터 {n}까지의 합: {total}")
for i in range(1, 11):
    if i % 3 == 0:
        print(i)
num = int(input("숫자를 입력하세요: "))
print(f"절대값: {abs(num)}")
for _ in range(3):
    num = int(input("숫자를 입력하세요: "))
    numbers.append(num)
print(f"가장 큰 수: {max(numbers)}")






