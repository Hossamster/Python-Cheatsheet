""" Testing """
# Reduce bugs in existing code 
# Ensure bugs that are fixed stay fixed
# Ensure that new features don't break old ones
# Ensure that cleaning up code doesn't introduce new bugs
# Makes development more fun!


""" # Test driven development
!1) Development begins by writing tests
?2) Once tests are written, write code to make tests pass
*3) Once tests pass, a feature is considered complete """

""" Mantra of the test driven development:
!Red : write a test that fails
*Green : Write the minimal amount of code necessary to make the test pass
Refactor - Clean up the code, while ensuring that tests still pass
"""

#todo: Assert statemnt

def add_positive_number(x,y):
    assert x > 0 and y > 0 , "Both numbers must be positive"
    return x + y

print(add_positive_number(6, 4))
# print(add_positive_number(6, -4))

# assert 4==2 


def eat_junk(food):
    assert food in ['pizza',
                    'ice cream', 'fries'], "food must be junk"
    return f"I am eating {food}"


print(eat_junk('pizza'))
print(eat_junk('candy'))


""" Disable Assertions """
# python -O filename.py