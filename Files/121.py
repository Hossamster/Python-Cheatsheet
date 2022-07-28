class Dic(dict):
    def __repr__(self):
        print ("None of ur buisness ")
        return super().__repr__()
    def __missing__(self,val):
        return f"The thing [{val}] u want is not here"
    def __set_item__(self,key,val):
        print("Alright") 
        super().__set_item__(key,val)
        print("Done")
    def __contains__(self, key):
        return True if key in self.__dict__.keys() else False

data = Dic({'first':'Hossam','gender':'male'})
print(data)

"""
class Train:
    def __init__(self,num_cars):
        self.num_cars = num_cars
    def __len__(self):
        return self.num_cars
    def __repr__(self):
        return '{} car train'.format(self.num_cars)

a_train = Train(4)
print(a_train)
print(len(a_train))


"""