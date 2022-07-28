""" Writing a data in csv file"""

# writer >> creates a writer object for writing to csv file

# writerow >> to write a row in csv file

# from csv import reader,writer
# with open('ayhaga.csv', 'w',newline='') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(['Name',"Age"])
#     csv_writer.writerow(['meshmesh',"2"])


# from csv import reader,writer
# with open('fighters.csv','r') as file:
#     data = reader(file)
#     data = [[col.upper() for col in row] for row in data]
#     with open('ayhaga.csv', 'w',newline='') as new_file:
#         lol = writer(new_file)
#         for i in data:
#             lol.writerow(i)


# from csv import reader,writer
# with open('fighters.csv','r') as file:
#     data = reader(file)
#     with open('ayhaga.csv', 'w',newline='') as new_file:
#         lol = writer(new_file)
#         for i in data:
#             lol.writerow([val.upper() for val in i])



################################################


# from csv import reader, DictWriter
# with open('ayhaga.csv', 'w',newline='') as file:
#     headers = ['Name','age']
#     csv_writer = DictWriter(file,fieldnames=headers)
#     csv_writer.writeheader() # it will take the fieldnames
#     csv_writer.writerow({
#         'Name':'Hossam','age':22
#     })



def cm_to_in(cm):
    return int(cm) * 0.393701


from csv import DictReader,DictWriter
with open('fighters.csv','r') as file:
    csv_reader = DictReader(file)
    # for col in csv_reader:
        # print(col)
    csv_reader = (list(csv_reader))
with open('ayhaga.csv', 'w',newline='') as file:
    headers = ['Name','Country','Height']
    csv_writer = DictWriter(file,fieldnames=headers)
    csv_writer.writeheader() 
    for i in csv_reader:
        csv_writer.writerow({'Name':i['Name'],'Country':i['Country'],'Height':cm_to_in(i['Height (in cm)'])})
