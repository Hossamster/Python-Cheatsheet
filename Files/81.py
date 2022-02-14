#parameters ordering
# parameters ,  *args , default parameters , **kwargs
def display_info(a,b,*args,instructor = "Hamada", **kwargs):
    return [a,b,args,instructor,kwargs]
print(display_info(1,2,3,last_name='Kamel',first_name="Hossam"))
# a = 1  , b=2
# args = 3
# instructor = hamada
#kwargs {last_name='kamel',first_name='Hossam'}
            