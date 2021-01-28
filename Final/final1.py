# 1.Little girl Tanya climbs the stairs inside a multi-store building. Every time Tanya climbs a stairway,
n = int(input())
a = list(map(int, input().split()))
a.append(0)
b = []
for i in range(0, len(a)-1):
    if a[i] >= a[i+1]:
        b.append(a[i])
print(len(b))
for i in b:
    print(i, end=" ")


1 2 3 1 2 3 4