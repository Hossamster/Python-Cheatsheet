'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

def update_users(old_first=1,old_last=1,new_first=1,new_last=1):
    from csv import reader,writer
    with open('ayhaga.csv','r',newline='') as file:
        data = reader(file)
        data = list(data)
    count = 0
    with open('ayhaga.csv','w',newline='') as file:
        csv_writer = writer(file)
        for i in data:
            if i[0] == old_first and i[1] == old_last:
                csv_writer.writerow([new_first,new_last])
                count += 1
            else:
                csv_writer.writerow(i)
    return ("Users updated: {}".format(count))

# update_users("Colt",'Steele','Hossam','Hassan')

'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

def delete_users(first,last):
    from csv import reader,writer
    with open('ayhaga.csv') as file:
        data = reader(file)
        data = list(data)
    count = 0
    new = []
    with open('ayhaga.csv','w',newline='') as file:
        csv_writer = writer(file)
        for i in data: 
            if i[0] == first and i[1] == last:
                count += 1
            else:
                csv_writer.writerow(i)
        
                
    return "Users deleted: {}.".format(count)

print(delete_users('Colt', 'Steele'))