#inheritance >>ability to define a class which inherits from another class

class Animal:
    cool = True
    def make_sound(self,sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    pass

blue = Cat()
blue.make_sound("Meow")
print(blue.cool)
print(Animal.cool)
print(isinstance(blue,Cat))
print(isinstance(blue,Animal))
print(isinstance(blue,object))
  