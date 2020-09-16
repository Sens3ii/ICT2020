a, b, c = map(int, input().split())
print(min(min(a, b), c), ((a + b + c) - max(max(a, b), c) -
                          min(min(a, b), c)), max(max(a, b), c))
