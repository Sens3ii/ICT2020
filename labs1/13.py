my_money = int(input())
coins = {'Toonies': 200, 'Loonies': 100,
         'Quarter': 25, 'Dime': 10, 'Nickel': 5, 'Penny': 1}
for m in coins:
    print('Number of', m + ':', my_money // coins[m])
    my_money %= coins[m]
