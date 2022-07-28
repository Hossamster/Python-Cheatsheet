def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

# print(fib_list(100000))


def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x+y
        yield x
        count += 1
# k = (fib_gen(100000))
# for n in k:
    # print(n)




'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

def get_multiples(num = 1,count=10):
    k = 1
    while k <=count:
        yield k*num
        k +=1
    

m = (get_multiples(2,3))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))




'''
sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

def get_unlimited_multiples(num=1):
    count = 1
    while True:
        yield num*count
        count += 1

k = get_unlimited_multiples(7)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))




##############################################

""" Generator expressions ()"""
g = (num for num in range(1,10))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))



import time 
gen_start_time = time.time()
print(sum(num for num in range(1000000000)))
gen_stop_time = time.time() - gen_start_time
print(f"the stop time is {gen_stop_time}")


lst_start_time = time.time()
print(sum([num for num in range(1000000000)]))
lst_stop_time = time.time() - lst_start_time

print(f"the stop time is {lst_stop_time}")
