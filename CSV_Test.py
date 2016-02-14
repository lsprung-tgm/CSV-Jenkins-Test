import unittest
from csv_class import Sprung_CSV


class TestMyFunctions(unittest.TestCase):
    def read_file_test(self):
        test = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissems")
        self.assertFalse(test.readCSV(),[])

    def read_new_file_test(self):
        test = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissems")
        test.newfile()
        test2 = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissemsNEW")
        self.assertFalse(test2.readCSV(),[])

    def read_new_file_test2(self):
        test = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissems")
        test.writeinCSV()
        test2 = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissemsNEU")
        self.assertFalse(test2.readCSV(),[])

if __name__ == '__main__':
    unittest.main()


