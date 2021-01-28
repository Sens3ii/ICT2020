n = int(input())
mx = 1
i = 1
while True:
    sm = 0
    sm += i-1  # edges between components
    k = 1
    for j in range(i, 0, -1):
        sm += (k*j)  # sum of component
        sm += (k-1)  # edges between vertex
        k += 1
    if(sm > n):
        print(i-1)
        break
    i += 1
