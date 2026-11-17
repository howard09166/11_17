stock = {"珍奶": 5, "紅茶": 3, "冬瓜茶": 6} #冰箱庫存
price = {"珍奶": 60, "紅茶": 30, "冬瓜茶": 25} #單價
orders = {
    1: ["小美", "珍奶", 2],
    2: ["阿明", "紅茶", 2],
    3: ["小華", "珍奶", 3],
    4: ["小美", "紅茶", 2],
    5: ["阿明", "冬瓜茶", 4],
    6: ["小華", "紅茶", 1],
    7: ["小美", "珍奶", 1],
}

money = 0
spent = {}
rejected = []
for no in orders:
    name, drink, cup = orders[no]
    if stock[drink] >= cup:
        stock[drink] = stock[drink] - cup
        cost = price[drink] * cup
        money = money + cost
        if name in spent:
            spent[name] = spent[name] + cost
        else:
            spent[name] = cost
    else:
        rejected.append(name + "-" + drink)

best_name = ""
best_money = 0
for name in spent:
    if spent[name] > best_money:
        best_name = name
        best_money = spent[name]

print(stock)
print(money)
print(rejected)
print(best_name)