money = 1260
change = 0
coins = [500, 100, 50, 10]
for i in coins:
    change += money//i
    money %=i
print(change)