# Exercise128: Reverse Lookup
def reverseLookup(myDict, target):
    ans = []
    for key in myDict:
        if myDict[key] == target:
            ans.append(key)
    return ans


sameNames = {
    "Alex": 1,
    "Daniil": 3,
    "Ivan": 2,
    "Yato": 3,
    "Magatsukami": 3,
}

print(reverseLookup(sameNames, 5))
print(reverseLookup(sameNames, 2))
print(reverseLookup(sameNames, 3))
