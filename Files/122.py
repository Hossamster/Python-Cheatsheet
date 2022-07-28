""" Iterator vs iterable """

name = "Hossam" #  iterable 
# print(next(name)) >> error as string object is not iterator

it = iter(name) # convert to iterator
# print(it) # <str_iterator object at 0x7f62a4b30040>

""" print(next(it)) 
print(next(it)) 
print(next(it)) 
print(next(it)) 
print(next(it)) 
print(next(it))  """
# print(next(it)) # stop eteration


nums = [1,2,3,4,5,6,7,8,9,10]
it = iter(nums) # baa iterator
""" print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it)) """
# print(next(it)) #stop iteration


# custom for loop
def my_for(iterable,func):
    iterator = iter(iterable)
    while True:
        try:
            thing = (next(iterator))
        except StopIteration:
            break
        else:
            func(thing)
def square(x):
    print(x**2) 
# my_for('Hello',print)
# my_for([1,2,3,4,5],print)
# (my_for([1,2,3,4,5],square))


# Custom iterator
class Counter:
    def __init__(self,low,high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self

    def __next__(self): 
        if self.current < self.high:
            num  = self.current
            self.current += 1
            return num
        raise StopIteration


for x in Counter(0,10):
    print(x)
            