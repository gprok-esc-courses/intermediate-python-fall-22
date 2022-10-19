import sqlite3

db = sqlite3.connect('test.db')

db.execute("""
            CREATE TABLE IF NOT EXISTS users 
            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            username TEXT)
           """)

# db.execute("INSERT INTO users (username) VALUES ('mary')")
# db.execute("INSERT INTO users (username) VALUES ('nick')")
# db.execute("INSERT INTO users (username) VALUES ('tom')")

cursor = db.cursor()
result = cursor.execute("SELECT * FROM users")

for row in result:
    print(str(row[0]) + ": " + row[1])

db.commit()
