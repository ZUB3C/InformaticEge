# import re
# import string
# with open("files/33526.txt", 'rt') as file:
#     text = file.read()
# matches = re.findall(r'(([A-Z])\w)\1', text)
# print(matches)
# most_common_character = ""
# char_count = 0
# line_of_second_letters = ''.join([i[0][1] for i in matches])
# for i in string.ascii_uppercase:
#     if line_of_second_letters.count(i) > char_count:
#         char_count = line_of_second_letters.count(i)
#         most_common_character = i
#         print(most_common_character, char_count)
#
# print(most_common_character)


#  ИЛИ:
with open("files/33526.txt", 'rt') as file:
    text = file.read()
data = {}
for i in range(1, len(text) - 1):
    if text[i - 1] == text[i + 1]:
        current_letter = text[i]
        if current_letter not in data.keys():
            data[current_letter] = 1
        else:
            data[current_letter] += 1
most_common_character = max(data, key=lambda x: data[x])
print(most_common_character)