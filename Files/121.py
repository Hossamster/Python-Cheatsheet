class GrumpyDict(dict):
    def __repr__(self):
        print("None of your buisness")
        return super().__repr__()

data = GrumpyDict({'first':'Hossam','gender':'male'})
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