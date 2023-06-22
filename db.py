from tinydb import TinyDB, Query
import random

db = TinyDB("facts.json")

def insert():
    db.insert({'n': 0, 'fact': "I can see you"})

def random():
    n = random.randint(0, 1)
    Fact = Query()
    db.search(Fact.n == n)


# db.truncate()
# insert()

print(db.all())
random()