from database import data

def deposit(data, user, amount):
    for i in data:
        if i["user"] == user:
            i["balance"] += amount
            return i