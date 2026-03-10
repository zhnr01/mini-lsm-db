from db import MiniLSM

db = MiniLSM()

db.put("user1", "Alice")
db.put("user2", "Bob")
db.put("user3", "Charlie")

print(db.get("user2"))