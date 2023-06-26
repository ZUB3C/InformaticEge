with open('files/27888.txt', 'rt') as file:
    lines = [i for i in file.read().split('\n') if len(i) != 0]
mem_size, user_count = list(map(int, lines[0].split()))
del lines[0]
user_file_sizes = sorted(list(map(int, lines)))
current_sum = 0
total_user_count = 0
max_file_size = 0
for i in user_file_sizes:
    if current_sum + i <= mem_size:
        total_user_count += 1
        current_sum += i
        if i > max_file_size:
            max_file_size = i
    else:
        break

difference = mem_size - current_sum
for i in range(0, len(lines)):
    if user_file_sizes[i] - user_file_sizes[total_user_count - 1] <= difference:
        max_file_size = user_file_sizes[i]
print(total_user_count, max_file_size)
