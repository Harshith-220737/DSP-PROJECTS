# 1. Student class with percentage and grade
class Student:
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
        self.percentage = sum(marks) / len(marks)

    def grade(self):
        if self.percentage >= 90:
            return 'A'
        elif self.percentage >= 75:
            return 'B'
        elif self.percentage >= 50:
            return 'C'
        else:
            return 'D'

sid = int(input("Enter ID: "))
name = input("Enter name: ")
marks = list(map(int, input("Enter marks: ").split()))
s = Student(sid, name, marks)
print("Percentage:", s.percentage)
print("Grade:", s.grade())


# 2. Parameterized constructor for employee
class Employee:
    def __init__(self, eid, name, salary, doj):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.doj = doj

    def display(self):
        print(self.eid, self.name, self.salary, self.doj)

e = Employee(1, "John", 30000, "01-01-2024")
e.display()


# 3. Count number of objects
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
        print("Objects:", Counter.count)

c1 = Counter()
c2 = Counter()


# 4. Built-in attributes
class Demo:
    def __init__(self, x):
        self.x = x

d = Demo(10)
print("Class name:", d.__class__.__name__)
print("Object id:", id(d))
print("Instance vars:", d.__dict__)


# 5. Simple inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Student2(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

st = Student2("Ram", 101)
print(st.name, st.roll)


# 6. Multiple inheritance
class Teacher:
    def teach(self):
        print("Teaching")

class Person2:
    def info(self):
        print("Person info")

class Staff(Person2, Teacher):
    pass

t = Staff()
t.info()
t.teach()


# 7. Random numbers in range
import random
low = int(input("Low: "))
high = int(input("High: "))
n = int(input("Count: "))
for _ in range(n):
    print(random.randint(low, high))


# 8. Area and circumference using math
import math
r = float(input("Radius: "))
print("Area:", math.pi * r * r)
print("Circumference:", 2 * math.pi * r)


# 9. Phone number validation
import re
ph = input("Enter phone (XXX-XXX-XXXX): ")
pattern = r'^\d{3}-\d{3}-\d{4}$'
if re.match(pattern, ph):
    print("Valid")
else:
    print("Invalid")


# 10. List operations
scores = list(map(int, input("Enter scores: ").split()))
scores.sort()
scores = list(set(scores))
avg = sum(scores) / len(scores)
print("Sorted unique:", scores)
print("Average:", avg)


# 11. Bank account class
class Bank:
    def __init__(self, bal):
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt

    def withdraw(self, amt):
        if amt <= self.bal:
            self.bal -= amt
        else:
            print("Insufficient")

    def show(self):
        print("Balance:", self.bal)

b = Bank(1000)
b.deposit(500)
b.withdraw(200)
b.show()


# 12. Library system
class Book:
    def __init__(self, name):
        self.name = name
        self.borrowed = False

class Member:
    def borrow(self, book):
        if not book.borrowed:
            book.borrowed = True
            print("Borrowed", book.name)

    def return_book(self, book):
        book.borrowed = False
        print("Returned", book.name)

bk = Book("Python")
m = Member()
m.borrow(bk)
m.return_book(bk)