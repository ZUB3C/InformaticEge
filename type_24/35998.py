with open("files/35998.txt", 'rt') as file:
    words = [i for i in file.read().split('\n') if len(i) != 0]
good_lines = [i for i in words if i.count('A') < 25]
max_len_from_all = 0
for line in good_lines:
    current_max_len = 0
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if line.rfind(letter) - line.find(letter) > max_len_from_all:
            max_len_from_all = line.rfind(letter) - line.find(letter)
    max_len_from_all = max(max_len_from_all, current_max_len)
print(max_len_from_all)