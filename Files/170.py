# SQL injection is a code injection technique that might destroy your database.   

import sqlite3
conn = sqlite3.connect('users.db')
# cursor
c= conn.cursor()

# execute
# c.execute('CREATE TABLE users (user_name Text,password Text)')

# data = [('Hossam','12345'),('Manar','77324'),('Jana','jana123')]
# c.executemany("INSERT INTO users VALUES (?,?)",data)

""" username = input('Enter username')
password = input('Enter password')
query = f"SELECT * FROM users WHERE user_name = '{username}' AND password = '{password}'"
c.execute(query)
result = c.fetchone()
if result: 
    print('Welcome Back')
else:
    print('Failed login') """

#! ' OR 1=1--
#? f"SELECT * FROM users WHERE user_name = 'Hossam' AND password = '' OR 1=1 --'"
#                                                                        True .....  -- eliminates the '


username = input('Enter username')
password = input('Enter password')

query = f"SELECT * FROM users WHERE user_name =? AND password =?"
c.execute(query,(username,password))

result = c.fetchone()
if result: 
    print('Welcome Back')
else:
    print('Failed login')

# commit changes
conn.commit()
conn.close()