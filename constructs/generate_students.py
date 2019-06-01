import random
import names

def getSQL(mask, vals):
    # Builds format line
    fmt="("
    for i in range(len(mask)):
        if(i>0):
            fmt += ","
        if(mask[i]):
            fmt+="'"
        fmt += "{}"
        if(mask[i]):
            fmt+="'"
    fmt += ")"

    # Prints output with vals list
    for val in vals:
        print(fmt.format(*val)+",")

departments = [('Biology'),
                ('EECS'),
                ('Finance'),
                ('History'),
                ('Music'),
                ('Physics')]

classes = [('BIO-MB', 'Molecular Bio.'),
            ('BIO-HB', 'Human Bio.'),
            ('CS-01', 'Comp. Sci.'),
            ('EE-01', 'Elec. Eng.'),
            ('FIN-01', 'Finance'),
            ('HIS-01', 'History'),
            ('MU-01', 'Music'),
            ('PHY-01', 'Physics'),]

courses = [('BIO-101', 'Intro. to Biology', 1, 4),
            ('BIO-301', 'Genetics', 2, 4),
            ('BIO-399', 'Computational Biology', 3, 3),
            ('CS-101', 'Intro. to Computer Science', 1, 4),
            ('CS-190', 'Game Design', 2, 4),
            ('CS-315', 'Robotics', 3, 3),
            ('CS-319', 'Image Processing', 2, 3),
            ('CS-347', 'Database System Concepts', 3, 3),
            ('EE-181', 'Intro. to Digital Systems', 1, 3),
            ('FIN-201', 'Investment Banking', 2, 3),
            ('HIS-351', 'World History', 1, 3),
            ('MU-199', 'Music Video Production', 3, 3),
            ('PHY-101', 'Physical Principles', 1, 4)]

genders = ["M", "F"]
terms = ["1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B"]

#%%
students = []
for id in range(10000,10020):
    student = (id, 
            names.get_last_name(), 
            random.choice(genders), 
            random.choice(terms),
            random.randrange(0, 30),
            random.randrange(0, 10),
            random.randrange(0, 10),
            random.choice(classes)[0])
    students.append(student)

getSQL((1,1,1,1,0,0,0,1), students)

#%%
takes = []
for student in students:
    take = (student[0], random.choice(courses)[0], random.randrange(45, 100), random.choice(terms))
    takes.append(take)
getSQL((1,1,0,1), takes)

#%%
teachers = []
for id in range(10000,10010):
    teacher = (id, 
        names.get_last_name(), 
        random.choice(departments))
    teachers.append(teacher)
getSQL((1,1,1), teachers)
