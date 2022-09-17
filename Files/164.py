import re
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) [A-z]+",re.I) 
matches = pattern.search(text)
# print(matches.group())


result = pattern.sub("Redacted",text) # sub for substitution
print(result) # Last night Redacted and Redacted murdered Redacted


result = pattern.sub("\g<1> Redacted",text) # sub for substitution
print(result) # Last night Mrs. Redacted and Mr. Redacted murdered Ms. Redacted


result = pattern.sub("Redacted \g<1>",text) # sub for substitution
print(result) # Last night Redacted Mrs. and Redacted Mr. murdered Redacted Ms.


result = pattern.sub("Redacted \g<1>",text) # sub for substitution
print(result) # Last night Redacted Mrs. and Redacted Mr. murdered Redacted Ms.



pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) ([A-z])[A-z]+",re.I) 

result = pattern.sub("\g<1> \g<2>",text)
print(result)


################################################################



def censor(input):
    import re
    pattern = re.compile(r'(\b[frack][A-z]+?\b)',re.I)
    res = pattern.sub('CENSORED',input)
    return res

print(censor("Frack you"))
print(censor("I hope you fracking die"))
print(censor("you fracking Frack"))

