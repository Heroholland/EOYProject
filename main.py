from database import Database
db = Database()
print(db.insert("test", "hi"))
print(db.read("test"))