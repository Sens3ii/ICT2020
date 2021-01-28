n = int(input())
names = []
names2 = []
for i in range(n):
    name = input()
    names.append(name)
    names2.append(name)

exists = False
print("NO")
for i in range(1, n):
    for j in range(0, i):
        if(names[i] == names2[j]):
            exists = True
            break
    if exists:
        print("YES")
    else:
        print("NO")
    exists = False
