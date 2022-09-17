import sqlite3
conn = sqlite3.connect("my_friends.db")
# cursor
c = conn.cursor()
# execute
people = [("Roald","Amundsen", 5),("Rosa", "Parks", 8),("Henry", "Hudson", 7),("Neil","Armstrong", 7),("Daniel", "Boone", 3)]

# c.executemany('INSERT INTO friends VALUES (?,?,?)', people)
avg = 0
for person in people:
    c.execute("INSERT INTO friends VALUES(?,?,?)",person)
#     avg += person[2]
# print(avg/len(people))

# commit
conn.commit()
conn.close()