import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
inset_querry = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(inset_querry, user)

users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz'),
]

cursor.executemany(inset_querry, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()