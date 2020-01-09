import unittest
from functions import *
import student
import io
import sys


class Test(unittest.TestCase):

    def testR4(self):
        students = student.parseStudents()
        self.assertEqual(R4(students, "HAVIR"), "HAVIR,BOBBIE,2,108,HAMER,GAVIN")
    def testR5(self):
        students = student.parseStudents()
        self.assertEqual(R5(students, "HAVIR"), "HAVIR,BOBBIE,0")
    def test3(self):
        pass

if __name__ == '__main__':
    unittest.main()
