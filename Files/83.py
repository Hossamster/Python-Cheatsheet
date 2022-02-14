#using ** as an argument for dictionary unpacking 
def display_names(first,second):
    print(f"{first} says hello to {second}")
display_names('Hossam','Ahmed')
names = {'first':'Hossam','second':'Ahmed'}
# display_names(names) # Type error 
# solution is to use ** to unpack the dictionary
display_names(**names)

def add_and_mul(a,b,c,**kwargs):
    print (a + b * c)
    print(kwargs)
data = dict(a=1,b=2,c=3,d=55,name="Tony")
add_and_mul(**data,cat='blue')


