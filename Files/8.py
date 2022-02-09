#format strings 
#interpolate variables >> f-strings
x = 10
formatted = f"I've told u {x} times" 
print(formatted)

#python  2 > 3.5    >>  .format method 
old = "I have told u {} times already!".format(45)
print(old)

#the old way => %operator 
old_awy = "I have told u %d times already!" %(x)
print(old_awy)
