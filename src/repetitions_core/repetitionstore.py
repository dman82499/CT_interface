import os
import pickle
import sqlite3
import sys

'''
A collection of methods for storing repetitions in a database, non-neuromorphic, basic.

Essentially serilizes objects and puts them in a database.

'''
class Repetitionsdatabase:

    def __init__(self, path=""):
        if path != "":
            if os.path.isfile(path):
                self.path = path
            else:
                print("this is not a valid path!")
                sys.exit()
        else:
            Repetitionsdatabase.manualsetup()
            path = input("please select a relative path/name to install the repetitions database file")
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
                sys.exit()
            else:
                print("Successfully created the directory %s " % path)
                self.path = path

        self.conn = sqlite3.connect(self.path)
        print(sqlite3.version)
        self.cursor = self.conn.cursor()
        # from self.cursor, you can use the .execute statement to write SQLite statements into the db file

    @staticmethod
    def manualsetup():
        path = input("please select a path to place the repetitions database directory")
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

        return path

    def setdirectory(self, path):
        self.path = path

    def createchceckrepetitionlfile(self):
        text = "ABCD"
        # The first step before doing this is to encypt the new file
        f = open(self.path + "checkrepfile", "wb")
        # instead of wrapping it in a Buffered Stream, could a custom encoding text stream be created to do this?
        # For Example: byte[] data = "ABCD".getBytes(StandardCharsets.UTF_8);
        # (Self note: The only difference between between a Buffered and non buffered is that buffered is encoded
        # where as non is still binary.)
        # DataOutputStream dos = new DataOutputStream(bos);
        first_vari = str(int(True))
        false_vari = str(0).encode(encoding='UTF-8', errors='strict')
        first_vari.encode(encoding='UTF-8', errors='strict')
        f.write(first_vari)
        f.write(false_vari)
        f.write(false_vari)
        f.write(first_vari)
        print("Successfully written data to the file")

    @staticmethod
    def checkrepetitionfile(self, nam2):
        #for (root, dirs, files in os.walk()):
            #if name in files:
                #return os.path.join(root, name)

    def updatedatabase(self, repetitions):
        # the repetitions could all be stored as a single file, however we use a database for security, and for specific use later
        for x in repetitions:
            repetit = pickle.dumps(x)

        # storing it as an induvidual file
        # because this is a temporary option, we do not end up creating an actual attribute.
        filf = open(self.path + "repe.ctsl")
        pickle.dump(repetitions, filf)
        filf.close() 

    def getdatabase(self):
        filef2 = open(self.path + "repe.ctsl")
        repet = pickle.load(filef2)
        return repet
