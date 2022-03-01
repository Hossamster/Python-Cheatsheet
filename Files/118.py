# MRO >>mothed resolution order     
class A:
    def do_something(self):
        print("Method defined in : A")
class B(A):
    def do_something(self):
        print("Method defined in : B")

class C(A):
    def do_something(self):
        print("Method defined in : C")

class D(B,C):
    pass

d = D()
print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.mro())   # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(help(D))