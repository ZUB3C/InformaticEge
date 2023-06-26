with open('files/38960.txt', 'rt', encoding='utf-8') as file:
    data = [i for i in file.read().split('\n') if len(i) != 0]
n, money = map(int, data[0].split())
del data[0]
arr_AB, arr_A = [[0, 0] for i in range(n)], [[0, 0] for i in range(n)]
for i, line in enumerate(data):
    price, type = line.split()
    arr_AB[i][0] = int(price)
    if type == "A":
        arr_AB[i][1] = 0
    elif type == "B":
        arr_AB[i][1] = 1
arr_AB.sort()

count = 0
spent = 0
i = 0
while money >= arr_AB[i][0] + spent:
    if (spent + arr_AB[i][0]) <= money:
        spent += arr_AB[i][0]
        count += 1
    i += 1
x = 1
for i in range(count, n):
    if arr_AB[i][1] == 0:
        arr_A[x][0] = arr_AB[i][0]
        arr_A[x][1] = arr_AB[i][1]
        x += 1
x = 1
for i in range(count - 1, -1, -1):
    if arr_AB[i][1] == 1:
        if (spent - arr_AB[i][0] + arr_A[x][0]) > money:
            break
        spent = spent - arr_AB[i][0] + arr_A[x][0]
        arr_AB[i][0] = arr_A[x][0]
        arr_AB[i][1] = arr_A[x][1]
        x += 1
count_A = 0
for i in range(count):
    if arr_AB[i][1] == 0:
        count_A = count_A + 1
print(count_A, money - spent)