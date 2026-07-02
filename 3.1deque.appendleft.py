#using list.append
# students = ['Mike', 'Jacob', 'Emma', 'Albert']
# students.insert(0,'Sam')
# print(students)

#using Deque.appendleft
from collections import deque
students = ['Mike', 'Jacob', 'Emma', 'Albert']
new_deque = deque(students)
new_deque.appendleft('Max')
print(new_deque)
