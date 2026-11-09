import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Ism TEXT NOT NULL,
    Familiya TEXT NOT NULL,
    Yosh INTEGER
)
""")

con.commit()
con.close()

print("Data baza yaratildi")

# import sqlite3
# con = sqlite3.connect("database.db")
# corsor = con.cursor()
# corsor.execute("""
#         INSERT INTO user(Ism,Familiya,Yosh)
#         VALUES (?,?,?)""",("Ibrahim","Atabekov",12))
# con.commit()
# con.close()
# print("Malumot qoshildi")

# import sqlite3

# con = sqlite3.connect("database.db")
# cursor = con.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS odamlar (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Ism TEXT,
#     Familiya TEXT,
#     Yosh INTEGER,
#     Pasport TEXT,
#     Tel TEXT,
#     Manzil TEXT
# )
# """)

# cursor.executemany("""
# INSERT INTO odamlar (Ism, Familiya, Yosh, Pasport, Tel, Manzil)
# VALUES (?, ?, ?, ?, ?, ?)
# """, [
#     ("John", "Smith", 25, "TEST0001", "+1-202-555-0101", "New York"),
#     ("Michael", "Johnson", 30, "TEST0002", "+1-202-555-0102", "Los Angeles"),
#     ("Emily", "Williams", 22, "TEST0003", "+1-202-555-0103", "Chicago"),
#     ("James", "Brown", 28, "TEST0004", "+1-202-555-0104", "Houston"),
#     ("Olivia", "Davis", 24, "TEST0005", "+1-202-555-0105", "Miami")
# ])

# import sqlite3

# con = sqlite3.connect("database.db")

# corsor = con.cursor()

# corsor.execute("""
# INSERT INTO user (Ism, Familiya, Yosh)
# VALUES (?, ?, ?)
# """, ("Mark", "Jones", 30))

# con.commit()
# con.close()

# print("Malumot qoshildi")



# import sqlite3

# con = sqlite3.connect("database.db", timeout=10)

# corsor = con.cursor()

# corsor.execute("""DELETE FROM user WHERE id BETWEEN 6 AND 25""")

# con.commit()

# con.close()

# print("Malumot ochirildi")


import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mashhurlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ism TEXT NOT NULL,
    familiya TEXT NOT NULL,
    tugilgan_sana TEXT,
    tugilgan_joy TEXT,
    davlat TEXT,
    kasbi TEXT
)
""")

mashhurlar = [
    ("Taylor", "Swift", "1989-12-13", "West Reading, Pennsylvania", "USA", "Singer"),
    ("Michael", "Jackson", "1958-08-29", "Gary, Indiana", "USA", "Singer"),
    ("Albert", "Einstein", "1879-03-14", "Ulm", "Germany", "Physicist"),
    ("Barack", "Obama", "1961-08-04", "Honolulu, Hawaii", "USA", "Politician"),
    ("Steve", "Jobs", "1955-02-24", "San Francisco, California", "USA", "Entrepreneur"),
    ("Bill", "Gates", "1955-10-28", "Seattle, Washington", "USA", "Businessman"),
    ("Tom", "Cruise", "1962-07-03", "Syracuse, New York", "USA", "Actor"),
    ("Beyonce", "Knowles", "1981-09-04", "Houston, Texas", "USA", "Singer"),
    ("Mark", "Zuckerberg", "1984-05-14", "White Plains, New York", "USA", "Programmer"),
    ("Serena", "Williams", "1981-09-26", "Saginaw, Michigan", "USA", "Tennis player")
]

cursor.executemany("""
INSERT INTO mashhurlar
(ism, familiya, tugilgan_sana, tugilgan_joy, davlat, kasbi)
VALUES (?, ?, ?, ?, ?, ?)
""", mashhurlar)

con.commit()
con.close()

print("Ma'lumotlar qo'shildi!")






































































