#enumerate function in python
#whenever you need both the index and the value while looping through lists,tuples,strings,any iterable

#without enumerate
# songs = ["Calm Down", "Blinding Lights", "Peaches"]
# index = 0
# for song in songs:
#     print(index, song)
#     index += 1

#with enumerate
songs = ["Calm Down", "Blinding Lights", "Peaches"]
for index, song in enumerate(songs, start=1):
    print(index, song)

word = "Python"
for index, letter in enumerate(word):
    print(index, letter)

colors = ("Red", "Green", "Blue")
for i, color in enumerate(colors):
    print(i, color)

students = ["Ram", "Sam", "John"]
for roll, student in enumerate(students, start=101):
    print(roll, student)