""" ALLEN ZHAI, WEI LIN, STEVEN GANDHAM """
import unittest
from functions import *
import student
import io
import sys


class Test(unittest.TestCase):

    def testR4(self):
        students = student.parseStudents()
        self.assertEqual(R4(students, "HAVIR"), [["HAVIR","BOBBIE","2","108",
                                                  "HAMER","GAVIN"]])

    def testR5(self):
        students = student.parseStudents()
        self.assertEqual(R5(students, "HAVIR"), [["HAVIR","BOBBIE","0"]])

    def testR6(self):
        students = student.parseStudents()
        self.assertEqual(R6(students, "HAMER"), [["LIBRANDI", "TODD"],
                                                 ["HAVIR", "BOBBIE"],
                                                 ["SARAO", "DIEDRA"],
                                                 ["VANCOTT", "MIKE"],
                                                 ["WICINSKY", "TERESE"],
                                                 ["KOZOLA", "BUSTER"],
                                                 ["MULLINGS", "LEIGHANN"],
                                                 ["BUSSMANN", "BILLY"],
                                                 ["BERBES", "DICK"],
                                                 ["MULGREW", "RANDELL"],
                                                 ["TOWLEY", "LANE"]])

    def testR7(self):
        students = student.parseStudents()
        self.assertEqual(R7(students, "1"), [["SAELEE", "DANILO"],
                                             ["GARTH", "JOHN"]])

    def testR8(self):
        students = student.parseStudents()
        self.assertEqual(R8(students, "51"), [["WOOLERY", "NOLAN", "2", "104"],
                                              ["STERBACK", "PETER", "6", "111"],
                                              ["LIBRANDI", "TODD", "2", "108"],
                                              ["RAPOSE", "ALONZO", "4", "105"],
                                              ["COVINGTON", "TOMAS", "3", "107"],
                                              ["MULLINGS", "LEIGHANN", "2", "108"],
                                              ["DURAND", "CARLEE", "4", "101"],
                                              ["FRIEDSTROM", "REED", "6", "106"]])

    def testR9(self):
        students = student.parseStudents()
        self.assertEqual(R9(students, "3 H"),
                        [["SWEDLUND","SHARRI","3.24","FAFARD","ROCIO","55"]])
        self.assertEqual(R9(students, "3 Low"),
                        [["CIGANEK","MANIE","2.79","FAFARD","ROCIO", "53"]])
    def testR10(self):
        students = student.parseStudents()
        self.assertEqual(R10(students, "3"), [["3,3.05"]])
        self.assertEqual(R10(students, "0"), [["0,0.0"]])
    def testR11(self):
        students = student.parseStudents()
        self.assertEqual(R11(students), [['Grade 0', '0'],
                                        ['Grade 1', '2'],
                                        ['Grade 2', '13'],
                                        ['Grade 3', '9'],
                                        ['Grade 4', '15'],
                                        ['Grade 5', '0'],
                                        ['Grade 6', '21']])
                                        

if __name__ == "__main__":
    unittest.main()
