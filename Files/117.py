class Aquatic:
  def __init__(self,name):
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"I am {self.name} of the sea!"

class Ambulatory:
  def __init__(self,name):
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"I am {self.name} of the land!"

class Penguin(Aquatic, Ambulatory):
  def __init__(self,name):
    Aquatic.__init__(self,name)
    Ambulatory.__init__(self,name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")
jaws.swim() # 'Jaws is swimming'
# jaws.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
jaws.greet() # 'I am Jaws of the sea!'

# lassie.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
lassie.walk() # 'Lassie is walking'
lassie.greet() # 'I am Lassie of the land!'

captain_cook.swim() # 'Captain Cook is swimming'
captain_cook.walk() # 'Captain Cook is walking'
captain_cook.greet() # 'I am Captain Cook of the sea!'