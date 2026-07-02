#using zip()
# students = ['Mike', 'Sam', 'Emma', 'John']
# course = ['DS', 'AI/ML', 'Full Stack']
# students_info = zip(students, course)
# print(list(students_info))

#using zip_longest()
from itertools import zip_longest
students = ['Mike', 'Sam', 'Emma', 'John']
course = ['DS', 'AI/ML', 'Full Stack']
students_info = zip_longest(students, course)
print(list(students_info)) 