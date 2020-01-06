import schoolSearch
import student
import sys
import os

def main():
    student.parseStudents(os.path.join(sys.path[0], "students.txt"))


if __name__ == '__main__':
    main()
