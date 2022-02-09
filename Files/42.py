#what if we want to make all of them upper case
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ''
for i in sounds:
    result += i.upper()
    result += ','
print(result)

#what if we want to make all of them capital case of the first letter
capital  = ''
for i in sounds:
    capital += i.capitalize()
    capital +=','
print(capital)