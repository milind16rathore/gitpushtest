import pymongo
client = pymongo.MongoClient("mongodb+srv://laxtak:milind1698@clusterm.nm0am8t.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "milind",
    "surname" : "rathore",
    "email": "milindrathore109@gmail.com"
}
db1 =client["mongotest"]
coll = db1["test"]
coll.insert_one(d)

