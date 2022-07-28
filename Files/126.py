""" Decorator """
# Decorator enhance other functions (@)

def be_polite(fn):
    def wrapper():
        print("What pleasure to meet u")
        fn()
        return ("Have a good day")
    return wrapper

@be_polite # >> greet = be_polite(greet)
def greet():
    print("My name is Hossam")

# k = be_polite(greet)
# print(k())


print(greet())

@be_polite # >> rage = be_polite(rage)
def rage():
    print("I Hate u ")

print(rage())
