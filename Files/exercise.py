class GrumpyDict(dict):
    def __repr__(self):
        print("None of your buisness")
        return super().__repr__()

data = GrumpyDict({'first':'Hossam','gender':'male'})
print(data)
