""" ALLEN ZHAI, WEI LIN, STEVEN GANDHAM """
from decimal import Decimal

#  S[tudent]: <lastname>
def R4(students, user_in):
    """ Search the contents of the students.txt file for the entry (or entries) for students with
    the given last name. For each entry found, print the last name, first name, grade and classroom
    assignment for each student found and the name of their teacher (last and first name). """
    for student in students:
        if user_in == student.StLastName:
            output = [student.StLastName, student.StFirstName, student.Grade, student.Classroom, student.TLastName, student.TFirstName]
            print(student.StLastName + "," + student.StFirstName + "," + student.Grade +
            ","  + student.Classroom + "," + student.TLastName + "," +  student.TFirstName)

            return ",".join(output)

# S[tudent]: <lastname> B[us]
def R5(students, user_in):
    """ Search the contents of the students.txt file for the entry (or entries) for students with
        the given last name. For each entry found, print the last name, first name and the bus
        route the student takes. """
    for student in students:
        if user_in == student.StLastName:
            output = [student.StLastName,student.StFirstName,student.Bus]
            print(student.StLastName + "," +student.StFirstName + "," + student.Bus)
    return ",".join(output)
# T[eacher]: <lastname>
def R6(students, user_in):
   """ Search the contents of the students.txt file for the entries where the last name of the
       teacher matches the name provided in the instruction. For each entry found, print the
       last and the first name of the student. """
   for student in students:
      if user_in == student.TLastName:
         print(student.StLastName + "," + student.StFirstName)

# G[rade]: <Number>
def R7(students, user_in):
   """ Search the contents of the students.txt file for the entries where the student's grade
       matches the number provided in the instruction. For each entry, output the name (last and first)
       of the student. """
   for student in students:
      if user_in == student.Grade:
         print(student.StLastName + "," + student.StFirstName)

# B[us]: <Number>
def R8(students, user_in):
   """ Search the contents of the students.txt file for the entries where the bus route number
       matches the number provided in the instruction. For each such entry, output the first and
       the last name of the student and their grade and classroom."""
   for student in students:
      if user_in == student.Bus:
         print(student.StLastName + "," + student.StFirstName + "," +
               student.Grade + "," + student.Classroom)

#G[rade]: <Number> H[igh]
#                   or
#G[rade]: <Number> L[ow]
def R9(students, user_in):
    """ Search the contents of the students.txt file for the entries where the student's grade
        matches the number provided in the instruction.

        If the H[igh] keyword is used in the command, find the entry in the students.txt file
        for the given grade with the highest GPA. Report the contents of this entry (name of the
        student, GPA, teacher, bus route).

        If the L[ow] keyword is used in the command, find the entry in the students.txt file
        for the given grade with the lowest GPA. Report the contents of this entry (name of the
        student, GPA, teacher, bus route)."""
    user_in = user_in.split();
    studentList = [student for student in students if user_in[0] == student.Grade]

    if user_in[1].strip('igh') == "H":
        maxGPA = max(student.GPA for student in studentList)
        maxGPAStudent = [student for student in studentList if student.GPA == maxGPA][0]
        print(maxGPAStudent.StLastName + "," + maxGPAStudent.StFirstName + "," +
              maxGPAStudent.GPA + "," + maxGPAStudent.TLastName + "," +
              maxGPAStudent.TFirstName + "," + maxGPAStudent.Bus)
    if user_in[1].strip('ow') == "L":
        minGPA = min(student.GPA for student in studentList)
        minGPAStudent = [student for student in studentList if student.GPA == minGPA][0]
        print(minGPAStudent.StLastName + "," + minGPAStudent.StFirstName + "," +
            minGPAStudent.GPA + "," + minGPAStudent.TLastName + "," +
            minGPAStudent.TFirstName + "," +  minGPAStudent.Bus)


# A[verage]: <Number>
def R10(students, user_in):
    """ Search the contents of the students.txt file for the entries where the student's grade
        matches the number provided in the instruction.Compute the average GPA score for
        the entries found. Output the grade level (the number provided in command) and the
        average GPA score computed."""
    studentList = [student for student in students if user_in == student.Grade]

    GPAList = [Decimal(student.GPA) for student in studentList]
    GPAAvg = sum(GPAList)/len(GPAList);

    print(user_in + "," + str(round(GPAAvg, 2)))


# I[nfo]
def R11(students):
    """ For each grade (from 0 to 6) compute the total number of students in that grade.
        Report the number of students in each grade in the format

            <Grade>: <Number of Students>

        sorted in ascending order by grade."""

    gradeList = [student.Grade for student in students]
    classCount = []
    for i in range(0,7):
        classCount.append(str(gradeList.count(str(i))))
    print("Grade 0: " + classCount[0] +
          "\nGrade 1: " + classCount[1] +
          "\nGrade 2: " + classCount[2] +
          "\nGrade 3: " + classCount[3] +
          "\nGrade 4: " + classCount[4] +
          "\nGrade 5: " + classCount[5] +
          "\nGrade 6: " + classCount[6])
