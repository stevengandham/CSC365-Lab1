import schoolSearch
import student
import sys
import os

def main():
    students = student.parseStudents(os.path.join(sys.path[0], "students.txt"))
    print(students)


if __name__ == '__main__':
    main()
