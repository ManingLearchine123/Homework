from django.db import models  # Django의 ORM을 사용하기 위해 models 모듈을 가져옴
from django.contrib.auth.models import User  # 기본 Django 제공 User 모델인데 별도로 만들어도 문제 없음

# 블로그 게시글 저장 모델
class Post(models.Model):
    title = models.CharField(max_length=255)  # 제목 (최대 길이 255자)
    content = models.TextField()  # 게시글 본문 저장
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    # User 모델과 1:N 관계 (ForeignKey) => 유저 한명이서 여러개의 Post를 만들 수 있음
    # on_delete=models.CASCADE => User가 삭제되면 관련된 Post도 삭제됨
    # related_name="posts" => user.posts로 해당 유저의 모든 게시글 조회 가능
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 생성된 시간 자동 저장 (최초 생성 시 한 번만 설정됨)

    def __str__(self):
        return self.name # 객체 print()할 때 게시글 제목으로 반
from django.db import models  # Django의 ORM을 사용하기 위해 models 모듈을 가져옴
from django.contrib.auth.models import User  # 기본 Django 제공 User 모델인데 별도로 만들어도 문제 없음

# 블로그 게시글 저장 모델
class Post(models.Model):
    title = models.CharField(max_length=255)  # 제목 (최대 길이 255자)
    content = models.TextField()  # 게시글 본문 저장
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    # User 모델과 1:N 관계 (ForeignKey) => 유저 한명이서 여러개의 Post를 만들 수 있음
    # on_delete=models.CASCADE => User가 삭제되면 관련된 Post도 삭제됨
    # related_name="posts" => user.posts로 해당 유저의 모든 게시글 조회 가능
    created_at = models.DateTimeField(auto_now_add=True)
    # 생성된 시간 자동 저장 (최초 생성 시 한 번만 설정됨)
    image =
    tags = models.ManyToManyField('Tag', related_name="posts")
    # 다대다(M:N) 관계 (ManyToManyField)
    # 하나의 게시글에 여러 개의 태그를 가질 수 있고 하나의 태그가 여러 게시글에 사용될 수 있음
    # related_name="posts" => tag.posts로 해당 태그가 포함된 모든 게시글 조회 가능


    def __str__(self):
        return self.title  # 객체 print()할 때 게시글 제목으로 반환

# 태그 저장 모델
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # 태그 (최대 길이 50자, 중복 불가)

    def __str__(self):
        return self.name  # 객체 print()할 때 태그 이름으로 반환
from django.db import models  # Django ORM을 사용하기 위한 models 모듈
from django.contrib.auth.models import User  # Django 기본 제공 User 모델

# 프로필 정보 모델
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # User 모델과 1:1 관계 (OneToOneField)
    # on_delete=models.CASCADE => User가 삭제되면 해당 Profile도 함께 삭제됨
    # related_name="profile" => user.profile로 프로필 정보에 접근 가능

    bio = models.TextField(blank=True, null=True) # 자기소개 필드 (기획 상 무조건 쓰지 않는다면 비어있어도 무방)

    def __str__(self):
        return self.user.username  # 객체 print()할 때 사용자 이름으로 반환
print(multiply(2, 3, 4)) 24임
# @classmethod: 클래스 자체를 다루는 기능을 가질 때 사용
# @staticmethod: 클래스나 인스턴스와 무관한 독립적인 기능을 수행할 때 사용
# 공통점이라면 둘 다 인스턴스를 생성하지 않고 "클래스에서 직접 호출 가능"
class School:
    break_time = 10  # 쉬는 시간 (클래스 변수)

    @classmethod
    def change_break_time(cls, new_time):
        """학교 휴식 시간"""
        cls.break_time = new_time  # 규칙 변경

    @staticmethod
    def calculate_average(scores):
        """시험 평균점수 계산"""
        return sum(scores) / len(scores)



# 기존 쉬는 시간 확인
print(School.break_time) # 10

# 2025년도 학교 규칙 변경 ("모든 학생"에게 적용)
School.change_break_time(15)

# 변경된 쉬는 시간 확인
print(School.break_time) # 15

# 평균 계산
scores = [90, 85, 88, 92, 78, 77, 66, 87, 98, 99, 23, 92, 55, 83, 86, 85, 88, 97, 87, 69]
average = School.calculate_average(scores)  # 스태틱 메서드는 그냥 호출 가능
print(f"평균: {average:.2f}")
# 여기서는 섭씨 온도만 넣으면 자동으로 화씨 온도를 알려주는 계산기능을 @property를 이용해서 만들었음
# 함수처럼 안 써도(() 없이) 변수처럼 쓸 수 있어서 편리함
# @staticmethod 그리고 @property

# staticmethod
# 매개변수가 필요함 => "데이터를 넣어야 동작"
# 단순한 유틸(함수) 만들 때 사용

# property
# 매개변수 없이 사용 가능
# "계산된 속성"을 변수처럼 사용할 수 있음
class Animal:
    def speak(self):
        return "동물이 소리를 냅니다"

class Dog(Animal):
    def speak(self):
        return "멍멍!"


animal = Animal()
dog = Dog()
print(animal.speak())
print(dog.speak())
# 상속이란 부모의 기능을 물려받은 것을 의미
# 오버라이딩이란 부모의 기능을 자기 스타일로 바꾼것을 의미


