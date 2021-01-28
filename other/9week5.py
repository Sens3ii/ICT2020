sampleDict = {
    "name": "Kelly",

    "age": 25,

    "salary": 8000,

    "city": "New york"
}
keys = ["name", "salary"]

newDict = dict()
for key in keys:
    newDict[key] = sampleDict[key]
print(newDict)
