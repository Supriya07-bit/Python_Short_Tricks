items = ['Charger', 'Headphones', 'Notebook', 'Pen', 'Snacks']
#first, second, *rest = items
# *first, rest = items
first, *middle, rest = items
print(first)
print(middle)
# print(second)
print(rest)