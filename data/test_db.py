from tinydb import TinyDB, Query
db = TinyDB("testdb.json")
db.insert(
    {'wioski' : 'john'}
)
print(db.all())