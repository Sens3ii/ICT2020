n = int(input())

cnt = 0
# 100, 20, 10, 5, 1
cnt += n//100
n = n % 100
cnt += n//20
n = n % 20
cnt += n//10
n = n % 10
cnt += n//5
n = n % 5
cnt += n//1
print(cnt)
