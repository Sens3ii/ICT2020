# Exercise 129: Two Dice Simulation
import random


def rollDices():
    return random.randint(1, 6) + random.randint(1, 6)


def getFormat(word):
    return " " * (12 - len(word)) + word


def getTableRow(v1, v2, v3):
    return getFormat(v1) + getFormat(v2) + getFormat(v3)


def printAsTable(myDict):
    print(getTableRow('Total', 'Simulated', 'Expected'))
    print(getTableRow('', 'Percent', 'Percent'))

    for i in myDict:
        print(getTableRow(str(i), str(myDict[i][0] / 10), str(myDict[i][1])))


def fillDict(myDict):
    for i in range(11):
        if (i < 5):
            myDict[i + 2] = [0, round((i + 1) * 2.78, 2)]
        else:
            myDict[i + 2] = [0, round((11 - i) * 2.78, 4)]


myDict = {}
fillDict(myDict)
for i in range(1000):
    myDict[rollDices()][0] += 1

printAsTable(myDict)
