import re
titles = [
"Significant Others (1987)",
"Tales of the City (1978)",
"The Days of Anna Madrigal (2014)",
"Mary Ann in Autumn (2010)",
"Further Tales of the City (1982)",
"Babycakes (1984)",
"More Tales of the City (1980)",
"Sure of You (1989)",
"Michael Tolliver Lives (2007)"
]

titles.sort()
# print(titles)

pattern = re.compile(r'(^[\w ]+) (\(\d{4}\))')
res = pattern.sub("\g<2> - \g<1>" , titles[0])
print(res)

pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
res = pattern.sub("\g<2> - \g<1>" , titles[0])
print(res)

print('*'*44)

fixed_titles = []
# pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')

for book in titles:
    # res = pattern.sub("\g<2> - \g<1>" , book)
    res = pattern.sub("\g<date> - \g<title>" , book)
    fixed_titles.append(res)
    
fixed_titles.sort()
print(fixed_titles)