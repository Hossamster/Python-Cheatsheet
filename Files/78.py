"""
Ex 1 product function
'''
product(2,2) # 4
product(2,-2) # -4
'''

# define product below:
def product(a,b):
    return a * b
print(product(2,2))
print(product(2,-2))
"""

#############
#Ex2
"""
'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

def return_day(num):
    if num == 7:
        return "Saturday"
    elif num ==1:
        return "Sunday"
    elif num ==2:
        return "Monday"
    elif num ==3:
        return "Tuesday"
    elif num ==4:
        return "Wednesday"
    elif num ==5:
        return "Thursday"
    elif num ==6:
        return "Friday"
    return None



def return_day(num):
    dic = {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
    for i in dic.keys():
        if num == i:
            return dic[num]
    return None
    """

"""
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None
    """
##########
#Ex 3
'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

"""
def last_element(lists):
    if len(lists) == 0: # if not lists:
        return None
    return lists[-1]
print(last_element([1,2,3]))
print(last_element([]))
"""
#######################
#Ex 4

'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

"""def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"
print(number_compare(1,1))
print(number_compare(1,0))
print(number_compare(2,4))"""

##############
#Ex 5
'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
"""def single_letter_count(word,letter):
    count = 0
    for i in word:
        if i == letter.lower() or i == letter.upper():
            count += 1
    return count
print(single_letter_count("HelLo World", "l"))
"""
"""
def single_letter_count(string,letter):
    return string.lower().count(letter.lower())
"""
#####################
#Ex 6
'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

"""
# flesh out multiple_letter count:
def multiple_letter_count(string):
    return {char:string.count(char) for char in string}
print(multiple_letter_count("awesome"))
"""
"""
def multiple_letter_count(word):
    my_dict = {}
    for i in word:
        my_dict.update({i:word.count(i)})
    return my_dict
"""
##################
#Ex 7
"""
def list_manipulation(lists,comm,loc,val=None):
    if comm == "remove" and loc == "end":
        k = lists[-1]
        lists.pop(len(lists)-1)
        return k
    elif comm == "remove" and loc == "beginning":
        k = lists[0]
        lists.pop(0)
        return k
    elif comm == "add" and loc == "beginning":
        lists.insert(0,val)
        return lists
    elif comm == "add" and loc == "end":
        lists.append(val)
        return lists
print(list_manipulation([1,2,3], "remove", "end")) #3
print(list_manipulation([1,2,3], "remove", "beginning")) # 1
print(list_manipulation([1,2,3], "add", "beginning", 20)) # [20,1,2,3]
print(list_manipulation([1,2,3],"add",'end',30)) # [1,2,3,30]
"""
####################
# Ex 8
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('a man a plan a canal panama') # True
'''

"""
def is_palindrome(string):
    string = string.replace(" ", "")
    # if string == string[::-1]:
    #     return True
    # return False
    return string == string[::-1]
print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah'))  # True
print(is_palindrome('robert'))  # False
print(is_palindrome('a man a plan a canal panama')) # True
"""
####################
# Ex 9 
'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

"""
def frequency(lists,search):
    return lists.count(search)
print(frequency([1,2,3,4,4,4,2,3,3,2,2,1,1],2))
print(frequency([True, False, True, True], True))
"""
###############
# Ex 10

'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

"""
def multiply_even_numbers(my_list):
    result = 1
    for i in my_list:
        if i % 2 == 0:
            result *= i
    return result
print(multiply_even_numbers([2,3,4,5,6]))
"""
##########
#Ex 11
'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

"""
def capitalize(string):
    return string[0].upper() + string[1:]
print(capitalize("hossam"))
"""
################
#Ex 12
'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''
"""
def compact(lst):
    return [haga for haga in lst if haga]
print(compact([0,1,2,"",[], False, {}, None, "All done"]))
"""
############
#Ex 13
# flesh out intersection pleaseeeee
"""
def intersection(list1,list2):
    return [val for val in list1 if val in list2]
    # return [val for val in set(list1) & set(list2)] # set solution
print(intersection([1,2,3],[2,3,4]))
print(intersection(["a",'b','c'],['x','c','q']))
"""
##############
#Ex 14
'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
# def isEven(num):
#     return num % 2 == 0

# def partition(my_list,fun):
#     return[[val for val in my_list if fun(val)],[val for val in my_list if not fun(val)]]
#     """  
#     truthy_list = []
#     falsy_list  = []
#     for i in my_list:
#         if isEven(i):
#             truthy_list.append(i)
#         else:
#             falsy_list.append(i)
#     my = []
#     my.extend([truthy_list,falsy_list])
#     return my
#     """ 
# print(partition([1,2,3,4], isEven))