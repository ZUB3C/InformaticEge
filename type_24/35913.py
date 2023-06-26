# Надо выяснить, верно ли что needed_str будет первой среди всех
# подходящих строк и что выводиться будет последняя буква из подходящих в алфавитном порядке
with open("files/35913.txt", 'rt') as file:
    words = [i for i in file.read().split('\n') if len(i) != 0]
needed_str = min(words, key=lambda x: x.count("N"))
print(max(needed_str, key=lambda x: needed_str.count(x)))