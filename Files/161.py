# https?://www\.[A-za-z-{2,256)\.[a-z{2,6}[-a-zA-Z0-9 @ :%_\+.~#?&//=]*

import re
url_regex = re.compile(r'(https?)://(www\.[A-Za-z]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

match = url_regex.search('http://www.youtube.com/videos')
# print(match.group())
# print('#'*40)
# print(match.groups())
# print('#'*40)
# print('Protocol: ',match.group(1))
# print('Domain: ',match.group(2))
# print('Everything Else: ',match.group(3))




#####################################################

def parse_bytes(input):
    import re
    pattern = re.compile(r'\b[10]{8}\b')
    res = pattern.findall(input)
    return res

print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is: 10101010 11100010"))
print(parse_bytes("asdsa"))