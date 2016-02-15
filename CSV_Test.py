import unittest
from csv_class import Sprung_CSV


class TestMyFunctions(unittest.TestCase):
    def setUp(self):
        self.test = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissems")
        pass
    def testread(self):
        self.test.readCSV()

if __name__ == '__main__':
    unittest.main()


