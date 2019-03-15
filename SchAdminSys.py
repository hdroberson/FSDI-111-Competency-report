class Class:
    
    Students = []

    def __init__(self, name, professor):
        self.name = name 
        self.Professor = professor 

    def addProfessor(self, professor):
        self.Professor = professor
    
    def addStudent(self, student):
        self.Students.append(student)

class Professor:

    def __init__(self, name):
        self.name = name
       
class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade 


# add students       
Std_1 = Student('Harold', 99)
Std_2 = Student('Tyrone', 76)
Std_3 = Student('Billy', 88) 

# add professor
P_1 = Professor('Mike')

Chemistry = Class('Chemistry', P_1)
Chemistry.addStudent(Std_1)
Chemistry.addStudent(Std_2)
Chemistry.addStudent(Std_3)


print('The following students and their grades are from ' + Chemistry.Professor.name + "'s" ' Chemistry Class:')

# print method
for x in Chemistry.Students:
    print(x.name,x.grade)



































'''

class Class:
    Professor = Professor
    Students = []

    __init__(self, name, professor):
        self.Professor = professor
        self.name = name
    
    def addStudent(self, student):
        self.Students.append(student)

    def removeStudent(self, student):
        self.Students.remove(student)

    def addProfessor(self, school, index):
        self.Prof = school.Faculty[index]

class Professor:

    __init__(self, name, id):
        self.name = name
        self.id = id

    def setName(self, name):
        self.name = name

class Student:

    __init__(self, name, id):
        self.name = name
        self.id = id

    def setName(self, name):
        self.name = name

class School:
    Faculty = []

    def addProfessor(self, professor):
        self.Faculty.append(professor)

    def removeProfessor(self, professor):
        self.Faculty.remove(professor)

'''