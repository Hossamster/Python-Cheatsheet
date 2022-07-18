from doctest import testmod
'''
product(2,2) # 4
product(2,-2) # -4
'''

# define product below:
def product(a=1,b=1):
    """ 
    >>> product(2,4)
    8
    >>> product(3,6)
    18
    """
    return a * b


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
    """ 
    >>> return_day(1) 
    'Sunday'
    >>> return_day(2)
    'Monday'
    """
    lst = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if num >=1 and num <= 7 :
        num = num - 1
        return lst[num]
    return None


'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(lst):
    """ 
    >>> last_element([1,2,3])
    3
    >>> last_element([546,21,545656,212,44])
    44
    """
    if len(lst) >= 1:
        return lst[-1]
    return None


'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(num1,num2):
    """ 
    >>> number_compare(2,4)
    'Second is greater'
    """
    if num1 > num2:
        return "First is greater"
    elif num2 > num1:
        return "Second is greater"
    return "Numbers are equal"



'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

def single_letter_count(word,letter):
    """ 
    >>> single_letter_count("Hello World", "h")
    1
    >>> single_letter_count("Hello World", "l")
    3
    """
    return word.lower().count(letter)



'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(word):
    """ 
    >>> multiple_letter_count("awesome")
    {'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1}
    """
    return {char:word.count(char) for char in word}



'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(lst,aor,eob,num=1):
    """ 
    
    """
    if aor == 'remove' and eob == 'end':
        return lst.pop()
    elif aor == 'remove' and eob == 'beginning':
        return lst.pop(0)
    elif aor =='add' and eob == 'beginning':
        lst.insert(0,num)
        return lst
    elif aor == 'add' and eob == 'end':
        lst.append(num)
        return lst


def say_hi():
    """ 
    >>> say_hi()
    'hi'
    """
    return 'hi'

def true_that():
    """ 
    >>> true_that()
    True
    """
    return True

def make_dict(keys):
    """ 
    >>> make_dict(['a', 'b', 'c'])
    {'a': True, 'b': True, 'c': True}
    """
    return {key:True for key in keys}



'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(lst,aor,eob,num=1):
    """ 
    >>> list_manipulation([1,2,3], "remove", "end")
    3
    >>> list_manipulation([1,2,3], "remove", "beginning")
    1
    >>> list_manipulation([1,2,3], "add", "beginning", 20)
    [20, 1, 2, 3]
    >>> list_manipulation([1,2,3], "add", "end", 30)
    [1, 2, 3, 30]
    """
    if aor == 'remove' and eob == 'end':
        return lst.pop()
    elif aor == 'remove' and eob == 'beginning':
        return lst.pop(0)
    elif aor =='add' and eob == 'beginning':
        lst.insert(0,num)
        return lst
    elif aor == 'add' and eob == 'end':
        lst.append(num)
        return lst



'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''
def is_palindrome(word):
    """ 
    >>> is_palindrome('testing')
    False
    >>> is_palindrome('tacocat')
    True
    >>> is_palindrome('hannah')
    True
    >>> is_palindrome('robert')
    False
    >>> is_palindrome('amanaplanacanalpanama')
    True
    """
    word = "".join(word.split(" "))
    return word == word[::-1]


'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(lst,word):
    """ 
    >>> frequency([1,2,3,4,4,4], 4)
    3
    >>> frequency([True, False, True, True], False)
    1
    """
    return lst.count(word)


'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(lst):
    """ 
    >>> multiply_even_numbers([2,3,4,5,6])
    48
    """
    num = 1
    for i in lst:
        if i % 2 == 0:
            num *= i
    return num


'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(word):
    """ 
    >>> capitalize("tim")
    'Tim'
    >>> capitalize("matt")   
    'Matt'
    """
    return word.capitalize()


'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(lst):
    """ 
    >>> compact([0,1,2,"",[], False, {}, None, "All done"])
    [1, 2, 'All done']
    """
    return [val for val in lst if val]



# flesh out intersection pleaseeeee
def intersection(lst1,lst2):
    """ 
    >>> intersection([1,2,3],[2,4,3])
    [2, 3]
    >>> intersection(['a', 'b', 'c'],['x', 'b', 'z'])
    ['b']
    """
    return [val for val in lst1 if val in lst2]


'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def isEven(num):
    """ 
    >>> isEven(4)
    True
    """
    return num % 2 == 0
def partition(lst,fn=isEven):
    """ 
    >>> partition([1,2,3,4], isEven)
    [[2, 4], [1, 3]]
    """
    even_lst,odd_lst= [val for val in lst if fn(val)],[val for val in lst if not fn(val)]
    return [even_lst,odd_lst]





if __name__ == "__main__":
    testmod(verbose = True)
