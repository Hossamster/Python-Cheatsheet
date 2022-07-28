""" CSV  """

# reading in a bad way
with open(r"C:\Users\Hossam\Downloads\fighters.csv", "r") as file:
    data = file.read()

# print(data)

""" 
?    reader - lets you iterate over rows of the CSV as lists
*    DictReader - lets you iterate over rows of the CSV as OrderedDicts
"""

from csv import reader
with open(r"C:\Users\Hossam\Downloads\fighters.csv") as file:
    data = reader(file)
    # for row in data:
    #     print(row)

# print(data)

with open(r"C:\Users\Hossam\Downloads\fighters.csv") as file:
    data = reader(file)
    next(data) # to skip the headers
    # for row in data:
    #     print(f"{row[0]} is from {row[1]}")


with open(r"C:\Users\Hossam\Downloads\fighters.csv") as file:
    data = reader(file)
    data = list(data)
    # print(data)

from csv import DictReader
with open(r"C:\Users\Hossam\Downloads\fighters.csv") as file:
    data = DictReader(file)
    for row in data:
        print(row)    
        

with open(r"C:\Users\Hossam\Downloads\fighters - Copy.csv") as file:
    data = reader(file,delimiter = '|')
    # for row in data:
    #     print(row)

    