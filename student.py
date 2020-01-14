""" ALLEN ZHAI, WEI LIN, STEVEN GANDHAM """

class Student:
    def __init__(self, StLastName, StFirstName, Grade, Classroom, Bus, GPA):
        self.StLastName = StLastName
        self.StFirstName = StFirstName
        self.Grade = Grade
        self.Classroom = Classroom
        self.Bus = Bus
        self.GPA = GPA
        self.TLastName = None
        self.TFirstName = None

    def __repr__(self):
        return "Last Name: {}\nFirst Name: {}\nGrade: {}\nClassroom: {}\nBus: {}\nGPA: {}\nTeacher Last Name: {}\nTeacher First Name: {}\n".format(self.StLastName, self.StFirstName, self.Grade, self.Classroom, self.Bus, self.GPA, self.TLastName, self.TFirstName)


def parseStudents(studentFilename, teacherFilename):
    Students = []
    try:
        with open(studentFilename, "r") as studentsFile:
            for line in studentsFile:
                info = line.strip(" \n").split(",")
                if len(info) == 6:
                    s = Student(info[0], info[1], int(info[2]), int(info[3]), int(info[4]), float(info[5]))
                    Students.append(s)
    except:
        return []

    try:
        with open(teacherFilename, "r") as teacherFile:
            for line in teacherFile:
                info = line.strip("\n").split(", ")
                if len(info) == 3:
                        for student in Students:
                            if student.Classroom ==int(info[2]):
                                student.TLastName = info[0]
                                student.TFirstName = info[1]
    except:
        return []
        
    return Students
