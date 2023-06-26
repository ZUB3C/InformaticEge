with open('files/33771.txt', 'rt', encoding='utf-8') as file:
    data = [i for i in file.read().split('\n') if len(i) != 0]
n, money = list(map(int, data[0].split()))
del data[0]
a_prices, b_prices = {}, {}
for line in data:
    single_price, count, type = line.split()
    single_price, count = int(single_price), int(count)
    if type == "A":
        if single_price not in a_prices.keys():
            a_prices[single_price] = count
        else:
            a_prices[single_price] += count
    elif type == "B":
        if single_price not in b_prices.keys():
            b_prices[single_price] = count
        else:
            b_prices[single_price] += count

for price in sorted(b_prices.keys()):
    count = b_prices[price]
    for j in range(count):
        if money - price < 0:
            print(0, money)
            exit()
        money -= price

current_a_products_price = 0
a_products_count = 0
for price in sorted(a_prices.keys()):
    count = a_prices[price]
    for j in range(count):
        if money - price < 0:
            print(a_products_count, money)
            exit()
        current_a_products_price += price
        a_products_count += 1
        money -= price