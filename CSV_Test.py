import unittest
from csv_class import Sprung_CSV


class TestMyFunctions(unittest.TestCase):
    def setUp(self):
        self.test = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissems")
        pass
    def testread(self):
        self.test.readCSV()

    def testwrite(self):
        self.test.writeinCSV()

    def testwrite2(self):
        self.test.newfile()

    def testsniffer(self):
        self.testsniffer()

if __name__ == '__main__':
    unittest.main()


