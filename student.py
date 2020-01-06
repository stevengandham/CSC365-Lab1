
class Student:
    def __init__(self, StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName):
        self.StLastName = StLastName
        self.StFirstName = StFirstName
        self.Grade = Grade
        self.Classroom = Classroom
        self.Bus = Bus
        self.GPA = GPA
        self.TLastName = TLastName
        self.TFirstName = TFirstName

    def __repr__(self):
        return "Last Name: {}\nFirst Name: {}\nGrade: {}\nClassroom: {}\nBus: {}\nGPA: {}\nTeacher Last Name: {}\nTeacher First Name: {}\n".format(self.StLastName, self.StFirstName, self.Grade, self.Classroom, self.Bus, self.GPA, self.TLastName, self.TFirstName)

def parseStudents(filename):
    Students = []
    with open(filename, "r") as studentsFile:
        for line in studentsFile:
            info = line.strip("\n").split(",")
            s = Student(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7])
            Students.append(s)
            print(s)
