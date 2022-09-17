# while True:
#     try:
#         hours = (input("enter the hours "))
#         rate = (input('enter the rate '))
#         if float(hours) > 40:
#             new_hours = float(hours) - 40
#             hour = 40
#         else : 
#             new_hours = 0
#             hour = float(hours)
#         new_rate = 1.5 * float(rate)
#         print(hour*float(rate) + float(new_hours)*float(new_rate))
#         break
#     except:
#         print('please enter integers or floats')

# x=5
# while x >0:
#     # print(x)
#     # if x==3:
#     #     continue
#     # else:
#     #     x=x-1
#     pass
# if x is 5:
#     print('Trueeeee')
lst= [1,2,3,4,5]
# big = x[0]
# for num in lst:
#     if num > big:
#         big = num
# print(big)
sum = 0 
for i in lst:
    sum += i
print(sum/len(lst))
