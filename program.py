# creating a dictionary
dict1 = {
    "Name": "Ananya",
    "Age": 13,
    "GPA": 10
}

print(dict1)
print(dict1["Name"])

dict1["City"] = "Austin"
print(dict1)

dict1["Name"] = "Aynana"
print(dict1)
del dict1["Age"]
print(dict1)

dict1.clear()
print(dict1)