import re

def contains_phone(input):
    phone_regex = re.compile(r'\b\d{3}\s\d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None
    
# print(contains_phone('my number is 432 567-4349'))
# print(contains_phone('my number is 432 567-4349321'))
# print(contains_phone('432 567-4349 sdsakjd'))
# print(contains_phone('432 567-4349'))


def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3}\s\d{3}-\d{4}\b')
    match = phone_regex.findall(input)
    if match:
        return match
    return None

# print(extract_all_phones('my number is 432 567-4349 or call me at 345 666-3456'))
# print(extract_all_phones('my number is 432 567-4 or call me at 345 6-456'))

def is_valid_phone(input):
    phone_regex = re.compile(r'^\d{3}\s\d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match: return True  
    return False

def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3}\s\d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match: return True  
    return False
# print(is_valid_phone("432 567-4349"))
# print(is_valid_phone("432 567-4349 ads"))
# print(is_valid_phone("asd 432 567-4349 d"))    




############################################################################

def is_valid_time(input):
    import re
    # pattern = re.compile(r"\d{1,2}:\d{2}")
    pattern = re.compile(r"^([0-9]|0[0:9]|1[2:9]|2[0:3]):[0-5][0-9]$")
    # res = pattern.fullmatch(input)
    res = pattern.search(input)
    if res: return True
    return False

print(is_valid_time("19:23"))
print(is_valid_time("1:23"))
print(is_valid_time("10.45"))
print(is_valid_time("1999"))
print(is_valid_time("145:23"))
print(is_valid_time("it is 12:15"))
print(is_valid_time("12:15"))