class Time:
    def __init__(self, hours, minutes, seconds): # 생성자
        self.hours = hours  # 시
        self.minutes = minutes  # 분
        self.seconds = seconds  # 초

    def to_seconds(self): # 시분초를 모아서 초단위로만 만들기
        return self.hours * 3600 + self.minutes * 60 + self.seconds # (시 * 3600) + (분 * 60) + 초

    @staticmethod
    def seconds_to_time(total_seconds): # 초단위를 시분초로 변환하는 "정적" 메서드 - 단순히 주어진 값만 변환하기에 정적메소드임!
        hours = total_seconds // 3600 # 시 계산
        minutes = (total_seconds % 3600) // 60  # 남은 초에서 분 계산
        seconds = total_seconds % 60  # 남은 초 계산
        return Time(hours, minutes, seconds)

    def add_time(self, second_time): # 두 시간 더하기
        total_seconds = self.to_seconds() + second_time.to_seconds() # 두 시간을 초로 변환, 더하기
        return self.seconds_to_time(total_seconds) # 초를 다시 시분초로 변환

    def interval_time(self, second_time): # 두 시간 차이 계산하기
        total_seconds = max(0, self.to_seconds() - second_time.to_seconds()) # 두 객체의 시간을 초로 변환하여 빼기, 결과가 마이너스면 0으로 처리
        return self.seconds_to_time(total_seconds) # 초를 다시 시분초로 변환

    def __str__(self): # __str__ 매직 메서드로 인스턴스 호출 시 이쁘게 표현
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

class Playlist:
    def __init__(self):
        self.songs = [] # 목록이니 리스트로 초기화

    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}'을(를) 추가했습니다.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}'을(를) 제거했습니다.")
        else:
            print(f"'{song}'은(는) 플레이리스트에 없습니다. 다시 한번 확인해주세요.")

    def __str__(self):
        return "\n".join(self.songs) if self.songs else "플레이리스트가 비어 있습니다."
구조
# calculator/ # 패키지
#     __init__.py
#     basic_operations.py # 모듈
#     advanced_operations.py
# main.py


# basic_operations.py
# def add(a, b): # 함수
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b if b != 0 else "0으로 나눌 수 없습니다."

# advanced_operations.py
# def 제곱(base, exponent):
#     return base ** exponent

# def 제곱근(number):
#     return number ** 0.5 if number >= 0 else "음수는 사용할 수 없습니다."

# from calculator.basic_operations import add, subtract, multiply, divide
# from calculator.advanced_operations import 제곱, 제곱근
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self): # 책 설명
        return f"{self.author} 작가의 '{self.title}'"

    def __eq__(self, second_book): # 저자가 같은지 확인 (equal)
        return self.author == second_book.author

    def __lt__(self, second_book): # 제목이 가나다(자세하게는 유니코드 순서)로 빠른지 확인 (later than)
        return self.title < second_book.title
class ElectronicDevice:
    def power_on(self):
        print("ElectronicDevice: Hello!")

    def power_off(self):
        print("ElectronicDevice: Bye!")

class PortableDevice:
    def charge(self):
        print("PortableDevice: 충전중입니다.")

class CommunicationDevice:
    def call(self, number):
        print(f"CommunicationDevice: {number}로 전화 중입니다.")

    def send_message(self, number, message):
        print(f"CommunicationDevice: {number}로 메시지를 발송합니다: {message}")

class Smartphone(ElectronicDevice, PortableDevice, CommunicationDevice):
    def use_app(self, app_name):
        print(f"Smartphone: '{app_name}'을(를) 사용중입니다.")


