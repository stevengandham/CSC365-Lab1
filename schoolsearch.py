""" ALLEN ZHAI, WEI LIN, STEVEN GANDHAM """
from functions import *
import student
import sys
import os

def printPrompt():
    print("Commands Available:\n    S[tudent]: <lastname> [B[us]]\n" +
          "    T[eacher]: <lastname>\n    B[us]: <number>\n"+
          "    G[rade]: <number> [H[igh]|L[ow]][T[eacher]]\n" +
          "    C[lass]: <number> [S[tudent]] [T[eacher]]\n" +
          "    A[verage]: <number>\n    I[nfo]\n    E[nrollment]\n" +
          "    D[ata]\n    Q[uit]")

def printOutput(output):
    for entry in output:
        print(",".join(entry))
    print()

def printInfo(output):
    for entry in output:
        print(": ".join(entry))
    print()

def checkLoadFile(students):
    if students == []:
        print("Couldn't Load Students")
        return False
    else:
        print("Loaded Student Information")
        printPrompt()
        return True

def DataPrompt(grade, teacher, bus):
    print("Average GPA sorted by:\n    G[rade]\n    T[eacher]\n    B[us]\n"
          + "    R[eturn] to main prompt")
    while True:
      user_in = input().split(" ")
      if user_in[0][0] == 'G':
          printInfo(grade)
      elif user_in[0][0] == 'T':
          printInfo(teacher)
      elif user_in[0][0] == 'B':
          printInfo(bus)
      elif user_in[0][0] == 'R':
          return;
      else:
         print("Invalid option")
         print("Options: G[rade] | T[eacher] | B[us] | R[eturn]\n")


def main():
    students = student.parseStudents("list.txt", "teachers.txt")
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
                print("Usage: S[tudent]: <lastname> [B[us]]\n")
        elif user_in[0][0] == 'T':
            if len(user_in) == 2:
                output = R6(students, user_in[1])
                printOutput(output)
            else:
                print("Invalid number of arguments")
                print("Usage: T[eacher]: <lastname>\n")
        elif user_in[0][0] == 'B':
            if len(user_in) == 2:
                output = R8(students, user_in[1])
                printOutput(output)
            else:
                print("Invalid number of arguments")
                print("Usage: B[us]: <number>\n")
        elif user_in[0][0] == 'G':
            if len(user_in) == 3:
                if user_in[2][0] == 'T':
                    output = NR3(students, user_in[1])
                    printOutput(output)
                elif user_in[2][0]=='H' or user_in[2][0]=='L':
                    output = R9(students, " ".join(user_in[1:]))
                    printOutput(output)
                else:
                    print("Invalid argument")
                    print("Usage: G[rade]: <number> [H[igh]|L[ow]][T[eacher]]\n")
            elif len(user_in) == 2:
                output = R7(students, user_in[1])
                printOutput(output)
            else:
                print("Invalid number of arguments")
                print("Usage: G[rade]: <number> [H[igh]|L[ow]][T[eacher]]\n")
        elif user_in[0][0] == 'C':
            if len(user_in) == 3:
                if user_in[2][0] == 'S':
                    output = NR1(students, user_in[1])
                elif user_in[2][0] == 'T':
                    output = NR2(students, user_in[1])
                printOutput(output)
            else:
                print("Invalid number of arguments")
                print("Usage:  C[lass]: <number> [S[tudent]] [T[eacher]]\n")
        elif user_in[0][0] == 'A':
            if len(user_in) == 2:
                output = R10(students, user_in[1])
                printOutput(output)
            else:
                print("Invalid number of arguments")
                print("Usage: A[verage]: <number>\n")
        elif len(user_in) == 1 and user_in[0][0] == 'I':
            output = R11(students)
            printInfo(output)
        elif len(user_in) == 1 and user_in[0][0] == 'E':
            output = NR4(students)
            printInfo(output)
        elif len(user_in) == 1 and user_in[0][0] == 'D':
            print("Computing Data...")
            grade, teacher, bus = NR5(students)
            d = DataPrompt(grade, teacher, bus)
            print()
            printPrompt()
        elif user_in[0][0] == 'Q':
            not_quit = False
        else:
            print("Invalid command\n")

if __name__ == '__main__':
    main()
