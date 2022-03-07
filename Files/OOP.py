from ast import Return
from datetime import date
class Student:
    no_of_students = 0 # class attribute >> it can be accessed by objects
    def __init__(self,name,age=0,courses='none'): #slef refers to the object that will be instantiated from the class 
        self.__age = age
        self.__name = name
        self.__courses = courses
        Student.no_of_students += 1
    
    def get_name(self):
        return self.__name

    def set_name(self,new):
        self.__name = new

    def describe(self):
        return (f"my name is {self.__name} and my age is {self.__age}")
    
    def is_old(self,val):
        if self.__age <= val:
            print('student is not old')
        else:
            print('student is old')
    @classmethod
    def initfrombirthyear(cls,name,birthyear):
        return cls(name,date.today().year - birthyear) # initialize with another format with destroying the init function 

s1 = Student('hossam',22,['bio','math','geo'])
# print(s1.no_of_students)
# s2 = Student('hossam',22,['bio','math','geo'])
# s3 = Student('hossam',22,['bio','math','geo'])
# print(Student.no_of_students)
# print(s1)
# <__main__.Student object at 0x00000218709EBD30>

# print(s1.name)
# print(s1.age)
# print(s1.courses)

# s1.name = 'ahmed'
# print(s1.name)

# print(s1.describe())

# s1.is_old(39)

# print(s1.get_name())
# (s1.set_name('hamada'))
# print(s1.get_name())

# print(s1.__name) error
#print(s1.name) #error

# s1.name = 'mickey'
# print(s1.name)

# print(s1._Student__name)
# print(s1.describe())

# s1 = Student.initfrombirthyear("nagla",1976)
# print(s1.describe())

class Pizza:
    def __init__(self,ingrediants,radius = 1):
        self.ingrediants = ingrediants
        self.radius = radius
    @classmethod
    def veg(cls):
        return cls(['mushroms','olives','onions'])
    
    @classmethod
    def margherita(cls):
        return cls(['mozarilla','sauce']) 

    
    def __str__(self):
        return f"Pizza ingrediants are {self.ingrediants}"

    def area(self):
        return Pizza.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * Math.PI()
# p1 = Pizza(['tomates','olives'])
# p2 = Pizza.veg()
# p3 = Pizza.margherita()

# print(p1,p2,p3) # <__main__.Pizza object at 0x0000019A293F78B0> <__main__.Pizza object at 0x0000019A293F75E0> <__main__.Pizza object at 0x0000019A297C3550> 
# How to change these messages above to be more beautiful >> Dunder functions >> double underscores
# print(dir(Pizza))


# print(p1,p2,p3) # Pizza ingrediants are ['tomates', 'olives'] Pizza ingrediants are ['mushroms', 'olives', 'onions'] Pizza ingrediants are ['mozarilla', 'sauce']

class Math:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def add5(num):
        return num + 5
    @staticmethod
    def add10(num):
        return num + 10
    @staticmethod
    def PI():
        return 3.14

x = Math.add(5,10)
y = Math.add5(x)
z = Math.add10(y)
# print(x,y,z)


# p = Pizza(['mozarilla','tomatoes'],6)
# print(p.area()) # 113.04
# print(Pizza.circle_area(5)) # 78.5


class Dates:
    def __init__(self, date):
        self.__date = date
    def getDate(self):
        return self.__date
    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

date = Dates ("15-12-2016") 

dateFromDB = "15/12/2016"

dateWithDash = Dates.toDashDate(dateFromDB)

# if(date.getDate() == dateWithDash):
#     print('equal')
# else:
#     print('not equal')



from datetime import date
#######
#polymorphism
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return f"name is {self.name} and age is {self.age}"
    # def __str__(self):
    #     return f"name is {self.name} and age is {self.age}"
    @classmethod
    def initfrombirthyear(cls,name,birthyear,extra):
        return cls(name,date.today().year - birthyear,extra)

class Man(Person):
    gender = 'Male'
    no_of_men = 0
    def __init__(self,name,age,voice):
        super().__init__(name,age)
        self.voice = voice
        Man.no_of_men += 1
    def display(self):
        string = super().display()
        return f"{string} and voice is {self.voice} and gender is {self.gender}"

# m = Man("Hossam",22,'hard')
# print(m.display())

class Woman(Person):
    gender = 'female'
    no_of_women = 0
    def __init__(self,name,age,hair):
        super().__init__(name,age)
        self.hair = hair
        Woman.no_of_women += 1
    def display(self):
        string = super().display()
        return f"{string} and her hair is {self.hair} and gender is {self.gender}"

# f = Woman("Soha",43,'curly')
# print(f.display())
# print(Woman.no_of_women)

# f = Woman("Soha",43,'curly')
# print(Woman.no_of_women)

# k = Man.initfrombirthyear('hossam',2000,'hard')
# print(k.display())

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Sqaure(Shape):
    def __init__(self, side):
        self.__side = side 
    def area(self):
        return self.__side ** 2
    def perimeter(self):
        return self.__side * 4

class Rect(Shape):
    def __init__(self, length, width):
        self.__length = length 
        self.__width = width
    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return (self.__length + self.__width) * 2
# s = Sqaure(10)
# print(f"square area is {s.area()} and perimeter is {s.perimeter()}")

# r = Rect(5,3)
# print(f"rectangle area is {r.area()} and perimeter is {r.perimeter()}")


class Man():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        names = self.name + " and " + other.name 
        ages = self.age + other.age
        return f"names combined are {names} and sum of ages is {ages}"

    def __lt__(self, other): 
        return self.age < other.age

    def display(self):
        return f"name is {self.name} and age is {self.age}"


man = Man("hossam",20)
man2 = Man("ahmed",43)
print(man+man2)
print(man<man2)
print(dir(Man))


