
from pymongo_get_database import get_database

dbname = get_database()
users = dbname["users"]

chycho = {}
chycho['id'] = 1
chycho['name'] = "chycho"
chycho['role'] = "admin"
chycho['password'] = "b87@mop$%1119"
users.insert_one(chycho)


