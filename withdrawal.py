from database import data

def withdraw(data, user, amount):
    for i in data:
        if i["user"] == user:
            if i["balance"] >= amount:
                i["balance"] -= amount
                return i
            else:
                return "Insufficient balance"