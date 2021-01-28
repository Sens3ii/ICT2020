n = int(input())
a = list(map(int, input().split()))

mx = max(a)
mn = min(a)
print(mx-mn-len(a)+1)
