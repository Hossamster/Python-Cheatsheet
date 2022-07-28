# map buitin that accepts at least two arguments,a function and an iterable

nums = [2,4,6,8,10]
doubles = [num*2 for num in nums]
print(doubles)

doubles = map(lambda x:x*2,nums)
print(doubles)
print(list(doubles))

people = ["Hassan","Kamel","hossam",'ahmed']
peeps = list(map(lambda name : name.upper(),people))
print(peeps)
# print(list(peeps))

names = [
    {'first':'Hossam','second':'Kamel'},
    {'first':'Ahmed','second':'Shabaan'},
    {'first':'Mohamed','second':'El sayed'} 
]
first_names = map(lambda x:x['first'],names)
print(list(first_names))

last_names = map(lambda x:x['second'],names)
print(list(last_names))


##
def double(x): return x*2
doubles = map(double,nums)
print(list(doubles))


##########################
# Ex
# nums = [1,2,3]
# decrement_list = list(map(lambda x:x-1,nums))
# print(decrement_list)

def decrement_list(nums):
    return list(map(lambda x:x-1,nums))
print(decrement_list([1,2,3]))
