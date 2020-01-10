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
        self.assertEqual(R6(students, "ZHAI"), [])

    def testR7(self):
        students = student.parseStudents()
        self.assertEqual(R7(students, "1"), [["SAELEE", "DANILO"],
                                             ["GARTH", "JOHN"]])
        self.assertEqual(R7(students, "99"), [])

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
        self.assertEqual(R8(students, "1000"), [])
if __name__ == "__main__":
    unittest.main()
