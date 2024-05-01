# class Person:
#     def greeting(self):
#         print('안녕하세요')

# class Student(Person):
#     def study(self):
#         print('공부를 합니다.')
        
# james = Student()
# james.greeting()
# james.study()

# ----------------------------------------------------------

# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'

# class Student(Person):
#     def __init__(self):
#         print('Student __init__')        
#         super().__init__()                 # 기반 클래스에도 파생 클래스에도 모두 __init__메서드가 있을 경우 파생 클래스에서 부모 클래스의 __init__를 사용하렬면 super()를 사용해야함
#         self.school = '파이썬 코딩 도장'

# james = Student()        
# print(james.school)
# print(james.hello)

# ----------------------------------------------------------

# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'

# class Student(Person):
#     pass

# james = Student()
# print(james.hello)

# ----------------------------------------------------------

# class Person:
#     def greeting(self):
#         print('안녕하세요.')

# class Student(Person):
#     def greeting(self):       # 기반클래스의 greeting함수를 오버라이딩 하기.
#         print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')

# james = Student()        
# james.greeting()

# ----------------------------------------------------------

# class Person:
#     def greeting(self):
#         print('안녕하세요.')

# class Student(Person):
#     def greeting(self):   
#         super().greeting()           # 기반클래스의 greeting함수도 함께 호출하기.
#         print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')

# james = Student()        
# james.greeting()

# ----------------------------------------------------------

# class Person:
#     def greeting(self):
#         print('안녕하세요.')

# class University:
#     def manage_credit(self):
#         print('학점 관리')        

# class Undergraduate(Person, University):   # 다중 상속하기.
#     def study(self):
#         print('공부하기')        

# james = Undergraduate()        
# james.greeting()
# james.manage_credit()
# james.study()

# ----------------------------------------------------------

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B, C):          # 다이아몬드 상속.
    pass

x = D()
x.greeting()
