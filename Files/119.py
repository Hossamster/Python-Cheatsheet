# Polymorphism 
# Poly >> many ,,, morph>>forms

# The same class method works in a similar way for different classes
# Cat.speak()
# Dog.speak()

class Animal():
    def speak(self):
        raise NotImplementedError("subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Fish(Animal):
    pass
d = Dog()
print(d.speak())
c = Cat()
print(c.speak())
f = Fish()
print(f.speak())


# The same operation works for different kinds of objects
# lst = [1,2,3]
# t = (1,2,3)
# len(lst)
# len(t)
#8+2 = 10
#"8"+"2"=82

