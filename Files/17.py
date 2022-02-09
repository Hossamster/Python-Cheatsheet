#logical operators (AND & OR)
city = input("where do u live? ")
if city == "los angeles" or city == "san francisco":
    print("u live in california\n")
elif city == "Cairo" or city == "Alex":
    print("u live in Egypt\n")
else:
    print("u live somewhere else\n")