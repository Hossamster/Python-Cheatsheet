#  __name__ variable = __main__ >>> in the same module only

# print(__name__) # __main__ law bet3mel exceute mn 102
                  # file_name law bet3melo import fy module tani

#############

def say_hi():
    print( f'HI! my __name__ is {__name__}')
(say_hi())


# see 102 and 103 together please

if __name__ == "__main__":
    print("u are in 102")
else:
    print("u are not in 102")

"""
if __name__ == "__main__":
    # this code will only run
    # if the file is the main file!
"""