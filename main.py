import schoolSearch
import student
import sys
import os

def main():
    students = student.parseStudents()
    schoolSearch.R6(students, "GAMBREL")
    schoolSearch.R7(students, "2")
    schoolSearch.R8(students,"52")
    schoolSearch.R9(students,"3 Low")
    schoolSearch.R9(students,"3 High")




if __name__ == '__main__':
    main()
