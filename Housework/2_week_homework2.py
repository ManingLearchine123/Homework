class Person:
#예시대로 텍스트 사용
    def __init__(self, name, gender, age):
    #예시대로 텍스트 사용
        self.name = name
        #예시대로 텍스트 사용
        self.gender = gender
        #예시대로 텍스트 사용
        self.age = age
        #나온대로 클라쓰 객채 만들엇다 예시대로

    def display(self):
    #예시대로 클라쓰 함수 만들었다 나온대로
        print("이름: " ,self.name, end = ", ")
        print("성별: ",self.gender)
        print("나이: ",self.age)
        #문제 대충봐서 틀릴뻔햇다 같은줄에 이름성별 바꿈

a = Person (input("이름을 입력해주세요"),input("성별을 입력해주세요"),input("나이를 입력해주세요"))
#예시입력 썻다
a.display()
#a 클럐쓰의 디수푸라이 메떠드 불음