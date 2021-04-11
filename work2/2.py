from collections import Counter


string = "DuMaMay"

result = Counter(string)


for element in result:
    if result[element] == 1:
        print(element, result[element])

