""" ALLEN ZHAI, WEI LIN, STEVEN GANDHAM """
from functions import *
import student
import sys
import os

def printOutput(output):
    for entry in output:
        print(",".join(entry))

def printInfo(output):
    for entry in output:
        print(": ".join(entry))

def checkLoadFile(students):
    if students == []:
        print("Couldn't Load Students")
        return False
    else:
        print("Loaded Student Information")
        print("Commands Available:\n    S[tudent]: <lastname> [B[us]]\n" +
                "    T[eacher]: <lastname>\n    B[us]: <number>\n    G[rade]: <number> [H[igh]|L[ow]]\n " +
                "   A[verage]: <number>\n    I[nfo]\n    Q[uit]")
        return True
     
def main():
    students = student.parseStudents("students.txt")
    not_quit = checkLoadFile(students)

    while not_quit:
        user_in = input().split(" ")
        if user_in[0][0] == 'S':
            if len(user_in) == 3 and user_in[2][0] == 'B':
                output = R5(students, user_in[1])
                printOutput(output)
            elif len(user_in) == 2:
                output = R4(students, user_in[1])
                printOutput(output)
            else:
                print("Invalid number of arguments")
                print("Usage: S[tudent]: <lastname> [B[us]]")
        elif user_in[0][0] == 'T':
            if len(user_in) == 2:
                output = R6(students, user_in[1])
                printOutput(output)
            else:
                print("Invalid number of arguments")
                print("Usage: T[eacher]: <lastname>")
        elif user_in[0][0] == 'B':
            if len(user_in) == 2:
                output = R8(students, user_in[1])
                printOutput(output)
            else:
                print("Invalid number of arguments")
                print("Usage: B[us]: <number>")
        elif user_in[0][0] == 'G':
            if len(user_in) == 3:
                output = R9(students, " ".join(user_in[1:]))
                printOutput(output)
            elif len(user_in) == 2:
                output = R7(students, user_in[1])
                printOutput(output)
            else:
                print("Invalid number of arguments")
                print("Usage: G[rade]: <number> [H[igh]|L[ow]]")
        elif user_in[0][0] == 'A':
            if len(user_in) == 2:
                output = R10(students, user_in[1])
                printOutput(output)
            else:
                print("Invalid number of arguments")
                print("Usage: A[verage]: <number>")
        elif len(user_in) == 1 and user_in[0][0] == 'I':
            output = R11(students)
            printInfo(output)
        elif user_in[0][0] == 'Q':
            not_quit = False
        else:
            print("Invalid command")

if __name__ == '__main__':
    main()
