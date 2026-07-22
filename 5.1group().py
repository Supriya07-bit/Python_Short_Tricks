#group() in python

from itertools import groupby

# employee = [
#     'Mike','Sam', 'Max', 'Jacob',
#     'Mark', 'Leo', 'Jack', 'Sage'
# ]
#
# employee.sort()
# emp_grouped = groupby(employee, key=lambda i: i[0])
# for key, group in emp_grouped:
#     print(key, list(group))

#groupby numbers into even and odd
# nums = [1,3,5,2,4,6]
# for key, group in groupby(nums, key=lambda x: x % 2):
#     print(key, list(group))

#group words by length
words = ['cat', 'dog', 'apple', 'ball', 'sun']

words.sort(key=len)

for key, group in groupby(words, key=len):
    print(key, list(group))