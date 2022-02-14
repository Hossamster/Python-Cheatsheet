# **kwargs >> keyword args , #most probably actually pronounce it as qwargs
#special operator we can pass to functions , gathers remaining keyword arguments as a dictionary 
def fav_colors(**kwargs):
    print(kwargs)
fav_colors(hossam='blue',jana='red',manar='magenta') # {'hossam': 'blue', 'jana': 'red', 'manar': 'magenta'} dictionary

def fav_colors(**kwargs):
    for person,color in kwargs.items():
        print(f"{person}'s favourite color is {color}")
fav_colors(hossam='blue',jana='red',manar='magenta',Nagla='purple') 

def special_greetings(**kwargs):
    if "Hossam" in kwargs and kwargs['Hossam'] == "special":
        return "u get a special greetings Hossam!"
    elif "Hossam" in kwargs:
        return f"{kwargs['Hossam']} Hossam!"
    return "Not sure who this is"
print(special_greetings(Hossam="special"))
print(special_greetings(Hossam="Hello"))
print(special_greetings(Jana="Hello"))


############
# Ex
def combine_words(string,**kwargs):
    if "prefix" in kwargs:
        return f"{kwargs['prefix']}{string}"
    elif "suffix" in kwargs:
        return f"{string}{kwargs['suffix']}"
    return string
# print(combine_words('child'))
# print(combine_words('child',prefix = 'man'))
# print(combine_words('child',suffix = 'ish'))
