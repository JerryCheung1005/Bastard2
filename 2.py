from collections import Counter


string = "fuckyoumothereveryday"

result = Counter(string)


for element in result:
    if result[element] == 1:
        print(element, result[element])

