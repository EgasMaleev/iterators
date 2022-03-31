def MyGenerator(listik):
    for item in listik:
        for el in item:
            yield el

nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
for item in MyGenerator(nested_list):
    print(item)
flat_list = [item for item in MyGenerator(nested_list)]
print(flat_list)