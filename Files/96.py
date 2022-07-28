#try: except: else: finally:

# try:
#     num = int(input("please enter a number "))
# except : # law el try tel3 fy haga msh mazbota
#     print('ya haywan ba2olak number!!') 
# else: # hatet3mel law el except 8alt 
#     print('ana fel else now')
# finally: # hatet3mel kda kda sawa except aw else
#     print("Runs no matter what!!")

# while(True):
#     try:
#         num = int(input("please enter a number: "))
#     except:
#         print("Ya haywan ba2olak number")
#     else:
#         print("3ash enta kda da5lt number")
#         break
#     finally:
#         print('let\'s repeat')

def divide(a,b):
    try:
        result = a / b
    # except ZeroDivisionError:
    #     return (f"don't divide by zero ya haywan")
    # except TypeError as err:
    #     print(f"a,b must be int or float")
    #     print(err)

    except (ZeroDivisionError,TypeError) as err:
        print("something went wrong")
        return (err)
    else:
        return result
print(divide(1,0))
print(divide(1,2))
print(divide('dsd','ds'))

