
def f(n):
    cnt = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            cnt -= i
        else:
            cnt += i
    return cnt


n = int(input())
print(f(n))
