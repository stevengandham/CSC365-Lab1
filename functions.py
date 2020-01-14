""" ALLEN ZHAI, WEI LIN, STEVEN GANDHAM """
from decimal import Decimal

#  S[tudent]: <lastname>
def R4(students, user_in):
    """ Search the contents of the students.txt file for the entry (or entries) for students with
    the given last name. For each entry found, print the last name, first name, grade and classroom
    assignment for each student found and the name of their teacher (last and first name). """
    output = []
    for student in students:
        if user_in == student.StLastName:
            output.append([student.StLastName, student.StFirstName,
                           str(student.Grade), str(student.Classroom), student.TLastName,
                           student.TFirstName])
            #print(student.StLastName + "," + student.StFirstName + "," + student.Grade +
            #","  + student.Classroom + "," + student.TLastName + "," +  student.TFirstName)
    return output

# S[tudent]: <lastname> B[us]
def R5(students, user_in):
    """ Search the contents of the students.txt file for the entry (or entries) for students with
        the given last name. For each entry found, print the last name, first name and the bus
        route the student takes. """
    output = []
    for student in students:
        if user_in == student.StLastName:
            output.append([student.StLastName,student.StFirstName,str(student.Bus)])
            #print(student.StLastName + "," +student.StFirstName + "," + student.Bus)
    return output

# T[eacher]: <lastname>
def R6(students, user_in):
   """ Search the contents of the students.txt file for the entries where the last name of the
       teacher matches the name provided in the instruction. For each entry found, print the
       last and the first name of the student. """
   output = []
   for student in students:
      if user_in == student.TLastName:
         output.append([student.StLastName, student.StFirstName])
         #print(student.StLastName + "," + student.StFirstName)
   return output

# G[rade]: <Number>
def R7(students, user_in):
   """ Search the contents of the students.txt file for the entries where the student's grade
       matches the number provided in the instruction. For each entry, output the name (last and first)
       of the student. """
   output = []
   for student in students:
      if user_in == str(student.Grade):
         output.append([student.StLastName, student.StFirstName])
         #print(student.StLastName + "," + student.StFirstName)
   return output

# B[us]: <Number>
def R8(students, user_in):
   """ Search the contents of the students.txt file for the entries where the bus route number
       matches the number provided in the instruction. For each such entry, output the first and
       the last name of the student and their grade and classroom."""
   output = []
   for student in students:
      if user_in == str(student.Bus):
         output.append([student.StLastName, student.StFirstName, str(student.Grade),
                   str(student.Classroom)])
         #print(student.StLastName + "," + student.StFirstName + "," +
         #      student.Grade + "," + student.Classroom)
   return output

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
    studentList = [student for student in students if user_in[0] == str(student.Grade)]
    if len(studentList) == 0:
        return []
    elif user_in[1].strip('igh') == "H":
        maxGPA = max(student.GPA for student in studentList)
        maxGPAStudent = [student for student in studentList if student.GPA == maxGPA][0]
        #print(maxGPAStudent.StLastName + "," + maxGPAStudent.StFirstName + "," +
        #      maxGPAStudent.GPA + "," + maxGPAStudent.TLastName + "," +
        #      maxGPAStudent.TFirstName + "," + maxGPAStudent.Bus)
        return [[maxGPAStudent.StLastName, maxGPAStudent.StFirstName,
                 str(maxGPAStudent.GPA), maxGPAStudent.TLastName,
                 maxGPAStudent.TFirstName, str(maxGPAStudent.Bus)]]
    elif user_in[1].strip('ow') == "L":
        minGPA = min(student.GPA for student in studentList)
        minGPAStudent = [student for student in studentList if student.GPA == minGPA][0]
        #print(minGPAStudent.StLastName + "," + minGPAStudent.StFirstName + "," +
        #    minGPAStudent.GPA + "," + minGPAStudent.TLastName + "," +
        #    minGPAStudent.TFirstName + "," +  minGPAStudent.Bus)
        return [[minGPAStudent.StLastName, minGPAStudent.StFirstName,
                 str(minGPAStudent.GPA), minGPAStudent.TLastName,
                 minGPAStudent.TFirstName,str(minGPAStudent.Bus)]]


# A[verage]: <Number>
def R10(students, user_in):
    """ Search the contents of the students.txt file for the entries where the student's grade
        matches the number provided in the instruction.Compute the average GPA score for
        the entries found. Output the grade level (the number provided in command) and the
        average GPA score computed."""
    studentList = [student for student in students if user_in == str(student.Grade)]
    if len(studentList) == 0:
        return []
    else:

        #GPAList = [Decimal(student.GPA) for student in studentList]
        GPAList = [student.GPA for student in studentList]
        GPAAvg = 0
        if (len(GPAList) != 0):
            GPAAvg = sum(GPAList)/len(GPAList)


        #print(user_in + "," + str(round(GPAAvg, 2)))
        return [[user_in + "," + str(round(GPAAvg, 2))]]

# I[nfo]
def R11(students):
    """ For each grade (from 0 to 6) compute the total number of students in that grade.
        Report the number of students in each grade in the format

            <Grade>: <Number of Students>

        sorted in ascending order by grade."""

    gradeList = [str(student.Grade) for student in students]
    output = []
    classCount = []
    for i in range(0,7):
        classCount.append(str(gradeList.count(str(i))))
        output.append(["Grade " + str(i), str(gradeList.count(str(i)))])
    #print("Grade 0: " + classCount[0] +
    #      "\nGrade 1: " + classCount[1] +
    #      "\nGrade 2: " + classCount[2] +
    #      "\nGrade 3: " + classCount[3] +
    #      "\nGrade 4: " + classCount[4] +
    #     "\nGrade 5: " + classCount[5] +
    #      "\nGrade 6: " + classCount[6])
    return output

# Given a classroom number, list all students assigned to it
def NR1(students, user_in):
    """ Given a classroom number, list all students assigned to it. """

    lst = [[student.StLastName, student.StFirstName] for student in students if user_in == str(student.Classroom)]
    return lst
# Given a classroom number, find the teacher (or teachers) teaching in it
def NR2(students, user_in):
    lst = []
    for student in students:
        if int(user_in) == student.Classroom:
            if [student.TLastName, student.TFirstName] not in lst:
                lst.append([student.TLastName, student.TFirstName])
    return lst

# Given a grade, find all teachers who teach it
def NR3(students, user_in):
    lst = []
    for student in students:
        if int(user_in) == student.Grade:
            if [student.TLastName, student.TFirstName] not in lst:
                lst.append([student.TLastName, student.TFirstName])
    return lst

# Report the enrollments broken down by classroom (i.e., ouput a list of
# classrooms ordered by classroom number, with a total number of students
# in each of the classrooms).
def NR4():
    pass

# Add to your program the commands that allow a data analyst to extract
# appropriate data to be able to analyze whether student GPAs are affected by
# the student's grades, student's teachers or the bus routes the students are on
def NR5():
    pass
