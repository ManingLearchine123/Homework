# "Book" 클래스를 만드세요
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def get_info(self):
        return self.title, self.author, self.price

# "BankAccount" 클래스를 만드세요

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def withdraw(self, a):
        self.balance -= a
    def deposit(self, a):
        self.balance += a
# "Student" 클래스를 만드세요
class Student:
    school_name = "Sparta"
    def __init__(self,name,grade,scores):
        self.name = name
        self.grade = grade
        self.scores = scores
    def add_score(self,subject, score):
        self.scores[subject]+=score
    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)
    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name
# "Product" 클래스를 만드세요
class Product:
    total_products = 0
    def __init__(self,name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        Product.total_products += 1
    def sell(self,quantity):
        self.stock = self.stock - quantity
    def restock(self,quantity):
        self.stock = self.stock + quantity
    @classmethod
    def get_total_products(cls):
        return cls.total_products
    @staticmethod
    def is_in_stock(self,stock):
        if self.stock > stock:
            return True
# "Car" 클래스를 만드세요
    class Car:
        total_cars = 0
        def __init__(self,make, model, year):
            self.make = make
            self.model = model
            self.year = year
        def get_info(self):
            return self.make,self.year
        @classmethod
        def get_total_cars(clscls):):
            return cls.get_total_cars()
        @staticmethod

        def is_antique(self,year):
            if 2024-year>25:
                return True