import re
def parse_name(input):
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) ([A-Za-z]+) ([A-z]+)$')
    matches = name_regex.search(input)
    # for i in matches.groups():
    #     print(i)
    return matches.groups()

# (parse_name('Mrs. Tilda Swinton'))



import re
def parse_name(input):
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-z]+)$')
    matches = name_regex.search(input)
    return matches.group('first'), matches.group('last')

# print(parse_name('Mrs. Tilda Swinton'))



########################################################


def parse_date(input):
    import re
    pattern = re.compile(r'(?P<day>[0-2][1-9]|3[0-1])[/,.,](?P<month>0[1-9]|1[0-2])[/,.,](?P<year>\d{4})')
    res = pattern.search(input)
    if res:
        return {'d':res.group('day'),'m':res.group('month'),'y':res.group('year')}
    return None
    
# print(parse_date("12/04/2003"))
# print(parse_date("01/22/1999"))
