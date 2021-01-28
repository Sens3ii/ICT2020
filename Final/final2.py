for i in range(int(input())):
    n, m = map(int, input().split())
    print('YES' if n % m == 0 and m >= 3 else 'NO')
