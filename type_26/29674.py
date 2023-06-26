# https://inf-ege.sdamgia.ru/problem?id=29674
from math import ceil


with open('files/29674.txt', 'rt', encoding='utf-8') as file:
    prices = [i for i in file.read().split('\n') if len(i) != 0]
prices = list(map(int, prices))
n = prices[0]
del prices[0]
total_sum = 0
max_price_with_discount = 0
discount_list = []
for price in prices:
    if price <= 50:
        total_sum += price
    else:
        discount_list.append(price)

discount_list.sort()  # Потому что © "порядок товаров в списке определяет продавец и делает это так, чтобы общая сумма скидки была наименьшей"
for i, price in enumerate(discount_list):
    if i < len(discount_list) // 2:
        total_sum += price * 0.75
        max_price_with_discount = price
    else:
        total_sum += price
# max_price_with_discount = discount_list[:len(discount_list)//2][-1]
print(ceil(total_sum), max_price_with_discount)
