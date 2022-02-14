#Reversed()
print(list(reversed([1,23,4,56])))

print("".join(list(reversed("hello"))))

# for x in reversed(range(0,10)):
#     print(x)

#Len()
print(len('asjdshajd'))
print(len({'s':10,'d':434,"dff":"dds","dfdf":"112"}))
print("hello".__len__())

#abs()
print(abs(-5))
print(abs(5))
# print(abs("5")) # error
print(abs(float(20)))
import math
print(math.fabs(-4)) # fabs >> float abs

#sum()
print(sum([1,2,3,4])) #10
print(sum([1,2,3,4],3)) #13
# print(sum(['hi','there'])) #error

#round()
print(round(10.2)) #10
print(round(10.6)) #11
print(round(3.14123,2)) #3.14
print(round(3.512,None)) #4

print(round(9.9999999999999999999999999999999999,15)) #10

###########
#Ex
def max_magnitude(my_list):
    return max(abs(val) for val in my_list)
print(max_magnitude([300,20,-900]))

############
#Ex
def sum_floats(*args):
    return sum(num for num in args if type(num) == float)
print(sum_floats(1.5, 2.4, 'awesome', [], 1))
print(sum_floats(1,2,3,4,5))

