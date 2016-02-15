__author__ = "Lukas Sprung"
import csv, sys
"""
    Diese Klasse enthält Methoden um ein CSV-File:
        - einzulesen und auszugeben
        - Ein neues Csv File zu erstellen und in dieses etwas hinein zu speichern
"""
def writeinCSV(filename):
    #Das File wird geoeffnet
    with open(filename+'.csv', 'w') as csvfile:
        fieldnames = ['T', 'WV', 'WK','BZ','SPR','WBER','ABG','UNG','SPOE',
                      'FPOE','OEVP','GRUE','NEOS','WWW','ANDAS','GFW','SLP','WIFF','M','FREIE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'T': '1', 'WV':'1', 'WK':'0','BZ':'0','SPR':'0','WBER':'1234556','ABG':'366656','UNG':'23459',
                         'SPOE':'236663','FPOE':'5751','OEVP':'56789','GRUE':'345666','NEOS':'346567',
                         'WWW':'3409','ANDAS':'3467','GFW':'7765','SLP':'2','WIFF':'136','M':'12','FREIE':'7'})
"""
    Diese Methode schreibt den Inhalt eines Files in ein anderes, sprich das File wird kopiert.
    Außerdem kann extra Content an das File gefuegt werden
"""
def newfile(filename):
    #Ausgangsdaten
    ifile  = open(filename+'.csv', "r")
    reader = csv.reader(ifile)
    #Exportfile
    ofile  = open(filename+'NEW.csv', "w")
    writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    #Zuerst werden die alten Daten in das File drangehaengt
    for row in reader:
     writer.writerow(row)
    #Danach wird der writer neu konfiguriert und extra Content wird in das File geschrieben
    fieldnames = ['T', 'WV', 'WK','BZ','SPR','WBER','ABG','UNG','SPOE',
                      'FPOE','OEVP','GRUE','NEOS','WWW','ANDAS','GFW','SLP','WIFF','M','FREIE']
    writer = csv.DictWriter(ofile, fieldnames=fieldnames)

    writer.writerow({'T': '1', 'WV':'1', 'WK':'0','BZ':'0','SPR':'0','WBER':'1234556','ABG':'366656','UNG':'23459',
                    'SPOE':'236663','FPOE':'5751','OEVP':'56789','GRUE':'345666','NEOS':'346567',
                    'WWW':'3409','ANDAS':'3467','GFW':'7765','SLP':'2','WIFF':'136','M':'12','FREIE':'7'})

    ifile.close()
    ofile.close()
"""
    Diese Methode ist dazu dar um ein CSV-File zu lesen und in der Konsole auszugeben
    Es ist wichtig, dass alle verschiedenen Dialekte ausgegeben werden können
    Dialekte: ['unix', 'excel-tab', 'excel']
    Ich habe die Methode mit allen  verschiedenen Dialekten getestet und alle konnten gleichermassen ausgelesen werden
"""
def readCSV(filename):
    filename = filename+'.csv'
    out = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, sniffer(filename))
        try:
           for row in reader:
              print(row)
              out.append(row)
        except csv.Error as e:
           sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
    return out
"""
    Diese Methode ermittelt den Dialekt anhand der Trennzeichen und gibt diesen dann zurueck
"""
def sniffer(filename):
    #Alle moeglichen Trennzeichen verpacke ich in eine Liste
    moegliche_Trennzeichen = [',', ';', '\t', ' ', '|', ':']
    try:
        #Es wird ueberprueft ob eines der oben angefuehrten Trennzeichen vorhanden ist
        dialect = csv.Sniffer().sniff(filename+'.csv', moegliche_Trennzeichen)
    except:
        #Wenn nicht gibt es keinen Dialekt
        dialect = None
    return dialect

#Der Dateipfad wird abgefragt
#pfad= "C:\\Users\\lspru\\Desktop\\ergebnissems"
    #input('Bitte geben sie den Pfad zur CSV Datei an. (Ohne Dateiendung)-> Beispiel->C:\\Users\\lspru\\Desktop\\ergebnisse: ')
#print(sniffer(pfad))
#Der Dialekt eines CSV-Files wird ueberprueft und das File wird in der Konsole ausgegeben
#readCSV(pfad)
#print("Speicherung in ein neues File "+pfad+"NEU.csv")
#Ein neues CSV File mit validen Header wird erstellt
#writeinCSV(pfad+'NEU')
#Ein Csv File wird kopiert und extra Content wird angehaengt
#newfile(pfad)
#print("Speicherung in ein neues File "+pfad+"NEW.csv")


#def read_file_test(self):
    #   test = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissems")
    #  self.assertFalse(test.readCSV(),[])

    #def read_new_file_test(self):
     #   test = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissems")
      #  test.newfile()
       # test2 = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissemsNEW")
        #self.assertFalse(test2.readCSV(),[])

    #def read_new_file_test2(self):
     #   test = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissems")
      #  test.writeinCSV()
       # test2 = Sprung_CSV("C:\\Users\\lspru\\Desktop\\ergebnissemsNEU")
        #self.assertFalse(test2.readCSV(),[])
