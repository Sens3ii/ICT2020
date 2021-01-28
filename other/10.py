a = int(input())
b = int(input())
c = int(input())

results = []

results.append(a+b+c)
results.append(a*b*c)
results.append((a+b)*c)
results.append(a*(b+c))

print(max(results))
