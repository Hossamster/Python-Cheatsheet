""" Unitest """

# Let's take a TDD approach and write some tests for these
# functions before implementing the functions

def eat(food,is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("Is_healthy must be boolean")
    if is_healthy:
        return f'Eating {food} is healthy'
    return f"Eating {food} is junk food"
def nap(num_hours):
    if num_hours > 2:
        return f"ugh i overslept, i didn't mean to nap for {num_hours} hours"
    return f"I'm feeling refreshed after my {num_hours} hour nap"    
def isfunny(person):
    if 'Hossam' == person:
        return "Hossam is funny"
    # return f"{person} is not funny"

def laugh():
    return 'haha'