# 주어진 문자열에서 각 문자의 출현 빈도를 계산하는 딕셔너리 컴프리헨션을 작성하세요.
st = "abcdd"
a = set(st)
d = {e: st.count(e) for e in a for i in st if e==i}

# 1부터 100까지의 숫자 중 3의 배수이면서 5의 배수인 숫자만을 포함하는 리스트를 리스트 컴프리헨션으로 생성하세요.
l = [e for e in range(0,101) if e%3==0 and e%5==0]
print(l)

# 두 개의 리스트가 주어졌을 때, 이를 딕셔너리로 결합하는 딕셔너리 컴프리헨션을 작성하세요.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d1 = {keys[i]: values[i] for i in range(0,3) }
print(d1)

# 주어진 리스트에서 중복을 제거하고 고유한 요소만을 포함하는 새로운 리스트를 생성하세요. (힌트: set 사용)
original_list = [1, 2, 2, 3, 4, 4, 5]
l = set(original_list)

# 2차원 리스트를 생성하는 리스트 컴프리헨션을 작성하세요. (예: 5x5 행렬)
l1 = [[j for j in range(5)] for i in range(5)]
print(l1)

# 주어진 문자열 리스트에서 길이가 5 이상인 문자열만 대문자로 변환하여 새로운 리스트를 만드세요.
string_list = ['apple', 'banana', 'pear', 'grape', 'kiwi']
l2 =[]
for i in string_list:
    c = 0
    for j in i:
        c+=1
    if c >= 5:
        l2.append(i)
print(l2)

# 두 개의 집합 A와 B가 주어졌을 때, 두 집합의 대칭 차집합을 구하세요.
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a ^ set_b)

#1부터 10까지의 숫자에 대해 각 숫자의 제곱을 값으로 갖는 딕셔너리를 생성하세요.
d = {x:x**2 for x in range(1,11)}
print(d)

#주어진 리스트에서 짝수만 선택하여 그 제곱값을 가진 새로운 리스트를 생성하세요.
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = [i for i in given_list if i%2==0]
print(l)

#여러 개의 리스트가 주어졌을 때, 이들을 하나의 리스트로 평탄화하는 함수를 작성하세요.
lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
l = []
for i in lists:
    for j in i:
        l.append(j)
print(l)