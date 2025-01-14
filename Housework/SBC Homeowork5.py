# "Animal", "Flyable", "Swimmable" 클래스를 만들고, 이를 다중상속받는 "Duck" 클래스를 만드세요
import abc as ABC
from abc import abstractclassmethod


class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Quack")
class Flyable:
    def fly(self):
        print("Flying")
class Swimmable:
    def swim(self):
        print("Swimming")
class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name)
duck = Duck("Duck1")
duck.fly()
duck.swim()
# "Person" 클래스와 이를 상속받는 "Student" 클래스를 만드세요
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return self.name
class Student(Person):
    def __init__(self, name, age,grade):
        super().__init__(name,age)
        self.grade = grade
    def introduce(self):
        return self.grade
    def __lt__(self, other):
        return self.grade > other.grade
# "Shape" 추상 클래스와 이를 상속받는 "Circle"과 "Rectangle" 클래스를 만드세요
    from abc import ABC, abstractmethod
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass
        @abstractmethod
        def perimeter(self):
            pass
    class Circle(Shape):
        def __init__(self,radius):
            self.radius = radius
        @property
        def radius(self):
            return self.radius
        @radius.setter
        def radius(self,value):
            if value < 0:
                raise ValueError("음수")
            self.radius = value
        def area(self):
            return 3.14*self.radius**2
        def perimeter(self):
            return 2 * 3.14 * self.radius

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)
# "Playlist" 클래스를 만들고 이에 대한 매직 메서드를 구현하세요
    class Playlist:
        def __init__(self):
            self.songs = []

        def __len__(self):
            return len(self.songs)

        def __getitem__(self, index):
            return self.songs[index]

        def __setitem__(self, index, value):
            self.songs[index] = value

        def __iter__(self):
            return iter(self.songs)
# "Temperature" 클래스를 만들고 섭씨/화씨 변환을 위한 프로퍼티를 구현하세요
    class Temperature:
        def __init__(self, celsius):
            self.celsius = celsius

        @property
        def celsius(self):
            return self._celsius

        @celsius.setter
        def celsius(self, value):
            self._celsius = value

        @property
        def fahrenheit(self):
            return self.celsius * 9 / 5 + 32

        @fahrenheit.setter
        def fahrenheit(self, value):
            self.celsius = (value - 32) * 5 / 9

        def __eq__(self, other):
            return self.celsius == other.celsius

        def __lt__(self, other):
            return self.celsius < other.celsius
