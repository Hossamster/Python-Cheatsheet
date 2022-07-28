# using * as an argument
# argument unpacking (tuple and list)
def sum_all_vales(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(sum_all_vales(1,2,3,4))
nums_list = [1,2,3,4,5,6]
nums_tuple= (1,2,3,4)
"""
print(sum_all_vales(nums_list))           # error unsupported operand
print(sum_all_vales(nums_tuple))          # error unsupported operand
"""
# so the solution to unpack the values are to use * as shown below
print(sum_all_vales(*nums_list))           # 21
print(sum_all_vales(*nums_tuple))          # 10

"""
# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1,4,7)

result2 = count_sevens(*nums)
print(result1)
print(result2)
"""
