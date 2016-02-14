from Sprung_CSV import readCSV, writeinCSV, sniffer, newfile
import unittest

class TestMyFunctions(unittest.TestCase):
    def read_file(self):
        pfad = "C:\\Users\\lspru\\Desktop\\ergebnissems"
        self.assertFalse(readCSV(pfad),[])

if __name__ == '__main__':
    unittest.main()
