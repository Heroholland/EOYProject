from databasewrapper import Database
db = Database()
print(db.insert("test", "testing123"))
print(db.read("test"))
print(db.replace("test", "testing1234"))
print(db.read("test"))
print(db.delete("test"))
print(db.read("test"))