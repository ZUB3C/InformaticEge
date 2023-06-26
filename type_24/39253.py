with open("files/39253.txt", 'rt') as file:
    text = file.read()
s = text.split('D')
mx = 0
for i in range(len(s) - 1):
    mx = max(len(s[i]) + len(s[i + 1]) + 1, mx)
print(mx)


#  Obfuscated solution:
#
# with open("files/39253.txt", 'rt') as file:
#     text = file.read()
# max_from_all_lens, count, count_old = 0, 0, 0
# for symbol in  symbols:
#     if symbol == "D":
#         max_from_all_lens = max(max_from_all_lens, count_old + count + 1)
#         count_old = count
#         count = 0
#     else:
#         count += 1
# max_from_all_lens = max(max_from_all_lens, count_old + count + 1)
# print(max_from_all_lens)
