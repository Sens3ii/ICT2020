sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
mn = min(sampleDict.values())
for subj, grade in sampleDict.items():
    if grade == mn:
        print(subj)
