n = int(input())
ans = ""
for i in range(1, n+1):
    if(i % 2 == 1):
        ans += "I hate"
    elif(i % 2 == 0):
        ans += "I love"
    if(i != n):
        ans += " that "
ans += " it"
print(ans)
