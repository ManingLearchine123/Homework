number = int(input("숫자를 입력하세요: "))

if number % 2 == 0:
    print(f"{number}는(은) 짝수입니다!")
else:
    print(f"{number}는(은) 홀수입니다!")

    # 2. 1부터 100까지의 숫자 중 3의 배수만 출력하는 프로그램을 작성하세요.

    # 3의 배수는 3으로 나누었을 때 나머지가 0인 숫자!

    for i in range(1, 101):
        if i % 3 == 0:
            print(i)

    # 3. 사용자로부터 점수를 입력받아 A, B, C, D, F 등급을 출력하는 프로그램을 작성하세요. (90이상 A, 80이상 B, 70이상 C, 60이상 D, 60미만 F)

    # 점수에 따라 A, B, C, D, F 등급을 나누기!
    # 조건문을 충분히 사용하면 해결할 수 있음!

    score = int(input("점수를 입력하세요: "))
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
    # 4. 구구단 7단을 출력하는 프로그램을 작성하세요.

    # 구구단은 특정 숫자에 1부터 9까지를 곱한 결과를 보여주는 것!

    for i in range(1, 10):
        print(f"7 x {i} = {7 * i}")
# 5. 1부터 100까지의 숫자 중 3의 배수이면서 5의 배수인 숫자를 모두 출력하는 프로그램을 작성하세요.

# 3의 배수이면서 5의 배수 === 공배수는 동시에 3으로도, 5로도 나누어 떨어지는 숫자!

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# 6
number = int(input("숫자를 입력하세요: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"{number}! = {factorial}")

# 7. 1부터 100까지의 숫자 중 소수(prime number)만 출력하는 프로그램을 작성하세요.

# 소수는 1과 자기 자신만으로 나누어 떨어지는 숫자!

# 2는 1과 2로만 나눌 수 있어요 → 소수!
# 3도 1과 3으로만 나눌 수 있어요 → 소수!
# 4는 1, 2, 4로 나눌 수 있어요 → 소수 아님!
# 2부터 100까지 숫자를 하나씩 검사하며 소수인지 확인

# 소수라고 먼저 가정하기
# 숫자 하나 꺼내기
# 소수인지 확인하기(작은 숫자로 나눠보기)
# 소수라면 출력하기

for num in range(2, 101):  # 1은 소수가 아님
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
# 8. 사용자로부터 숫자 n을 입력받아 피보나치 수열의 n번째 항까지 출력하는 프로그램을 작성하세요.

# 피보나치 수열이란 앞의 두 숫자를 더해 다음 숫자를 만드는 규칙
# 예시로 0, 1, 1, 2, 3, 5, 8...

n = int(input("몇 번째 항까지 출력할까요? "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 9. 사용자로부터 문자열을 입력받아 그 문자열이 팰린드롬(앞뒤로 읽어도 같은 문자열)인지 판별하는 프로그램을 작성하세요.

# 팰린드롬은 앞뒤로 읽어도 같은 단어를 의미
# 예시로 "토마토", "racecar" 같은 것이 있음
# 문자열을 뒤집어서 비교하면 됨!

text = input("문자를 입력하세요: ")
if text == text[::-1]:
    print("팰린드롬입니다!")
else:
    print("팰린드롬이 아닙니다.")
#10 1부터 100까지의 숫자를 출력하되, 3의 배수는 "Fizz", 5의 배수는 "Buzz", 3과 5의 공배수는 "FizzBuzz"를 출력하는 프로그램을 작성하세요.
for e in range(1,101):
    if e%3==0 and e%5==0:
        print('FizzBuzz')
    elif e%3==0:
        print('Fizz')
    elif e%5==0:
        print('Buzz')
    else:
        print(e)