""" ALLEN ZHAI, WEI LIN, STEVEN GANDHAM """
from functions import *
import student
import sys
import os

def main():
    students = student.parseStudents()
    if students == None:
        print("Couldn't Load Students")
        not_quit = False
    else:
        print("Loaded Student Information")
        not_quit = True
        print("Commands Available:\n    S[tudent]: <lastname> [B[us]]\n" +
                "    T[eacher]: <lastname>\n    B[us]: <number>\n    G[rade]: <number> [H[igh]|L[ow]]\n " +
                "   A[verage]: <number>\n    I[nfo]\n    Q[uit]")



    while not_quit:
        user_in = input().split(" ")
        if user_in[0][0] == 'S':
            if len(user_in) == 3 and user_in[2][0] == 'B':
                R5(students, user_in[1])
            elif len(user_in) == 2:
                R4(students, user_in[1])
            else:
                print("Invalid number of arguments")
                print("Usage: S[tudent]: <lastname> [B[us]]")
        elif user_in[0][0] == 'T':
            if len(user_in) == 2:
               R6(students, user_in[1])
            else:
                print("Invalid number of arguments")
                print("Usage: T[eacher]: <lastname>")
        elif user_in[0][0] == 'B':
            if len(user_in) == 2:
               R8(students, user_in[1])
            else:
                print("Invalid number of arguments")
                print("Usage: B[us]: <number>")
        elif user_in[0][0] == 'G':
            if len(user_in) == 3:
                R9(students, " ".join(user_in[1:]))
            elif len(user_in) == 2:
                R7(students, user_in[1])
            else:
                print("Invalid number of arguments")
                print("Usage: G[rade]: <number> [H[igh]|L[ow]]")
        elif user_in[0][0] == 'A':
            if len(user_in) == 2:
               R10(students, user_in[1])
            else:
                print("Invalid number of arguments")
                print("Usage: A[verage]: <number>")
        elif len(user_in) == 1 and user_in[0][0] == 'I':
            R11(students)
        elif user_in[0][0] == 'Q':
            not_quit = False
        else:
            print("Invalid command")


if __name__ == '__main__':
    main()
