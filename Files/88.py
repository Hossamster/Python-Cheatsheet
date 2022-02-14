#all >> return true if all elements of the iterable are truthy
# [<condition(x)> for x in <iterable>]
# not filter it as the list comprehension
# [x for x in <iterable> if <condition(x)>]
print(all([1,2,3])) #true
print(all([0,1,2,3])) #false 3ashan el zero

#[char for char in "aei" if char in "aeiou"] >> ['a','e','i']
print(all(char in 'aeiou' for char in 'wq' )) #false
print(all(char in 'aeiou' for char in 'aei' )) #true

people = ['Charlue','Casey','Cody','Carly','Cristina']
print(all(char[0]=='C' for char in people )) #True

people.append("kristry")
print(all(char[0]=='C' for char in people )) #False

nums = [2,60,26,18]
print(all(num % 2 ==0 for num in nums)) #True

nums = [2,60,26,18,9]
print(all(num % 2 ==0 for num in nums)) #False

##########
"""
Great question! I know it seems like all([])  should return false.  Here's a simplified version of what all looks like behind the scenes:

def all(things):
     for x in things:
         if not x:
             return False
     return True
In the case of an an empty list, it always returns True because there's nothing to loop over.  The for x in things  doesn't loop because it's an empty list, so it just returns True.
"""
##########

#any >> return true if any of the element is truthy
print(any([1,2,3])) #True
print(any([0,1,2,3])) #True

print(any(val > 2 for val in [1,2,3] )) #True
print(any(val > 5 for val in [1,2,3] )) #False

#generator expression
print((val > 2 for val in [1,2,3] ))

import sys
list_comp = sys.getsizeof([x for x in range(1000)])
gen_exp = sys.getsizeof(x for x in range(1000))
print(f"list comprehension = {list_comp} bytes")
print(f"generator expression = {gen_exp} bytes")

#############
#Ex
# def is_all_strings (my_list):
#     return all(type(val) == str for val in my_list)

# print(is_all_strings(['a','b','c']))
# print(is_all_strings(['a','b','c',1]))
# print(is_all_strings(['hello','goodbye','0','100']))
# print(is_all_strings(['hello','goodbye','0',12]))