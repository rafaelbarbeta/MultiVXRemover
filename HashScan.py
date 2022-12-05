import hashlib
import sqlite3
import os

class HashScan:
    def __init__(self,cwd):
        self.cwd = cwd
        self.hashDB = os.path.join(cwd,"hashDB.db")
        self.conn = sqlite3.connect(f"file:{self.hashDB}?mode=ro",uri=True)
        self.cursor = self.conn.cursor()
        self.filesChecked = 0
    
    def scanFile(self,filePath):
        """
        Hash a file and search for it in the hashDB
        If the hash is present in the hashDB, return True
        Else, return False
        """
        fileHash = ""
        with open(filePath,"rb") as target:
            fileHash = hashlib.md5(target.read()).hexdigest()
        res = self.cursor.execute("SELECT hash_text FROM hashDB WHERE hash_text = ?",(fileHash,))
        if res.fetchone() is None:
            return False
        else:
            return True
    
    def scanDir(self,dir):
        """
        Hash all files in a directory and search for them in the hashDB
        Return a list of paths to infected files
        Use scanFile() to hash and search for each file
        """
        dirPath = os.path.join(self.cwd,dir)
        files2Scan = list()
        filesInfected = list()
        for root,dirs,files in os.walk(dirPath,topdown=True):
            for fileNames in files:
                files2Scan.append(os.path.join(root,fileNames))
        self.filesChecked = len(files2Scan)
        for filePath in files2Scan:
            if self.scanFile(filePath):
                filesInfected.append(filePath)
        return filesInfected
    
    def getFilesChecked(self):
        return self.filesChecked