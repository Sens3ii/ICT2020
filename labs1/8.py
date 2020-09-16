w, g = map(int, input().split())
res = w * 75 + g * 112
if res > 1000:
    print("Total weight:", f'{res/1000:.3f}', "kg")
else:
    print("Total weight:", res, "g")
