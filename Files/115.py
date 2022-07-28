# super()

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self,sound):
        print(f'this animal says {sound}')

class Cat(Animal):
    def __init__(self,name,species,breed,toy):
        """Avoid duplication"""
        # self.name = name
        # self.species = species

        # Animal.__init__(self,name,species) 
        super().__init__(name,species)
        self.breed = breed
        self.toy = toy
    
    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def play(self):
        return (f"{self.name} plays with {self.toy}")

blue = Cat("Blue",'Cat','Scotttish Fold','String')
print(blue) # Blue is a Cat
print(blue.species) # Cat
print(blue.breed) # Scotttish Fold
print(blue.toy) # String
print(blue.play()) # Blue plays with String
