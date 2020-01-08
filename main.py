import schoolSearch
import student
import sys
import os

def main():
    students = student.parseStudents()
    not_quit = True

    while not_quit:
        user_in = input().split(" ")
        if user_in[0][0] == 'S':
            if len(user_in) == 3 and user_in[2][0] == 'B':
                schoolSearch.R5(students, user_in[1])
            else:
                schoolSearch.R4(students, user_in[1])
        elif user_in[0][0] == 'T':
            schoolSearch.R6(students, user_in[1])
        elif user_in[0][0] == 'B':
            schoolSearch.R8(students, user_in[1])
        elif user_in[0][0] == 'G':
            if len(user_in) == 3:
                schoolSearch.R9(students, " ".join(user_in[1:]))
            else:
                schoolSearch.R7(students, user_in[1])
        elif user_in[0][0] == 'A':
            schoolSearch.R10(students, user_in[1])
        elif user_in[0][0] == 'I':
            schoolSearch.R11(students)
        if user_in[0][0] == 'Q':
            not_quit = False


if __name__ == '__main__':
    main()
