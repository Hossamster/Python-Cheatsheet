""" Serialization in Python """

#The serialization process is a way to convert a data structure into a linear form that can be stored or transmitted over a network.

""" 
In Python, serialization allows you to take a complex object structure and transform it into a stream of bytes that can be saved to a disk or sent over a network.
You may also see this process referred to as marshalling. 
The reverse process, which takes a stream of bytes and converts it back into a data structure, is called deserialization or unmarshalling. """



class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

blue = Cat('meshmesh','scotish fold','annabele')
custy = Cat('custy','scotish fold','annabele')

import pickle
with open('pets.pickle','wb') as file:
    pickle.dump((blue,custy), file)

whiskers = Cat("whiskers", "gray", "thing1")
tubbs = Cat("tubbs", "short hair", "thing2")

with open("pets.pickle", "ab") as file:
	pickle.dump((whiskers,tubbs), file)

# with open('pets.pickle','rb') as file:
#     a,b = pickle.load(file)
#     c,d = pickle.load(file)


#! The objects in a pickle file can only be unpickled one at a time. 
#? If there are multiple objects in there, you need run pickle.load() multiple times to get everything.