import sqlite3
conn = sqlite3.connect('my_friends.db')
#cursor
c = conn.cursor()

# execute

# c.execute('SELECT * FROM friends')
# for row in c:
#     print(row)

# print(c.fetchall()) # gives list of all rows


# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
# print(c.fetchone())


c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
print(c.fetchall())

# commit changes
conn.commit()
conn.close()