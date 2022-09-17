
class makes_iterable:
    def __init__(self,low,high):
        self.current = low
        self.high = high
    def __iter__(self):
        print('making iterator')
        return myiterator(self.current,self.high)

class myiterator:
    def __init__(self,low,high):
        self.current = low
        self.high = high
        
    def __next__(self):
        if self.current < self.high:
            num  = self.current
            self.current += 1
            return num
        raise StopIteration

po = makes_iterable(1,7)
po = iter(po)
print(po)
print(po.__next__())
print(po.__next__())
print(po.__next__())
# print(po)