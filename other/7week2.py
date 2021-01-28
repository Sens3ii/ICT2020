import sys
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if i == 1:
        print("HARD")
        sys.exit()
print("EASY")
