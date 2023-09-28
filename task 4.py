my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
keysWithMinValue = []
i = 0
while i != 3:
    minKey = min(my_dict, key=my_dict.get) 
    keysWithMinValue.append(minKey)
    del my_dict[minKey]
    i += 1
print(keysWithMinValue)
