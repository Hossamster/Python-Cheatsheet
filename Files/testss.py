class GrumpyDict(dict):
    def __repr__(self):
        print('none of ur buisness')
        return super().__repr__()
    def __missing__(self,key):
        return (f"u want {key}? msh hena")

    def __setitem__(self, key, val):
        self[key] = val



k = GrumpyDict({})
print(dir(dict))
