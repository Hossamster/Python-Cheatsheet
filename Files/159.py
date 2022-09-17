""" Regular expressions """ # not a python specific topic
# A way of describing patterns within search strings

# use cases 
# credit card number validating 
# phone number validating
# advanced fing/replace in text 
# formating text/output
# sybtax highlighting

# \d > digits 0-9
# \w > letter, digit, or underscore
# \s > white space character
# \D > not a digit 
# \W > not a word character
# \S > not a white space
# .  > any character except line breaker


""" Quantifiers """
# +   > one or more
# {3} > Exactly x times. {3} - 3 times
# {3,5} > three to five times
# {4,} > four or more times
# * > zero or more times
# ? > once or none(optional)

# anchors and boundaries
# ^ > start of string or line 
# $ > end of string or line
# \b > word boundary

import re

pattern = re.compile(r"\d{3}\s\d{3}-?\d{3,}")

res = pattern.search('Call me at 415 555-4242!')

# print(res)
print(res.group()) # 415 555-4242

##########################

res = pattern.search('Call me at 310 213-4321 or 415 555-4242!')
# print(res)
print(res.group()) # 310 213-4321 > search gives only the first match 

res = pattern.findall('Call me at 310 213-4321 or 415 555-4242!')
print(res)


print(re.search(r"\d{3}\s\d{3}-?\d{3,}",'Call me at 415 555-4242!').group())

