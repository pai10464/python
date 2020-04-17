a = input()
b = input()
c = input()
courses = open(a, 'r')
dict_courses = {}
for e in courses:
    x = e.strip('\n').split(',')
    dict_courses[x[0]] = x[1]
teachers = open(b, 'r')
dict_teachers = {}
for e in teachers:
    x = e.strip('\n').split(',')
    dict_teachers[x[0]] = x[1]
database = open(c, 'r')
for e in database:
    x = e.strip('\n').split(',')
    if x[0] in dict_courses and x[1] in dict_teachers:
        print(dict_courses[x[0]] + ',' + dict_teachers[x[1]])
    else:
        print('record error')
