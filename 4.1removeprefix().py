student_record = ("CSE.Mike", "CSE.Jacob", "CSE.Alice", "CSE.Emily", "CSE.Micheal",
                  "CSE.Emma")

for name in student_record:
    #print(name.lstrip('CSE.'))
    print(name.removeprefix('CSE.'))
