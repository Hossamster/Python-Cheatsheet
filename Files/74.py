#Common return mistakes 
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total

print(sum_odd_numbers([1,2,3,4,5,6,7])) # 1 WHY ? HOW !

# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:  # [1,2,3,4,5,6,7]
#         if num % 2 != 0: # 1 is odd yes
#             total += num # total = 1
#         return total     # return means leave the function as we said before

#### so the solution for this is to make the return total after the for loop
#### complete it's total execution as shown below

def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:  # [1,2,3,4,5,6,7]
        if num % 2 != 0: # 1 odd yes,2 no,3 yes,4 no,5 yes,6 no,7 yes
            total += num # 1st loop t=1,2nd loop t=1,3rd loop t=1+3=4
            #4th loop t=4, 5th loop t=4+5=9, 6th loop t=9, 7th loop t=9+7=16
    return total #after execution the loop >> retun total=16 which means leave
                 # the funtion

print(sum_odd_numbers([1,2,3,4,5,6,7])) # 16 >> GOT it ?


### unnecessary else
def is_odd_num(num):
    if num % 2 != 0:
        return True
    else:
        return False

# print(is_odd_num(4))
# print(is_odd_num(9))

def is_odd_num(num):
    if num % 2 != 0:
        return True # if the number is odd it will return true which means 
            #that it will leave the function and not complete its execution
    return False

print(is_odd_num(4))
print(is_odd_num(9))


'''
# Without adding any new lines of code, make count_dollar_signs work as intended
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
        # return count   # 1
    return count
print(count_dollar_signs("$uper $ize")) #2

''' 