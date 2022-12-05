from operator import indexOf
import pickle
import hashlib
import os

class HashScan:

    def __init__(self,cwd):
        self.cwd = cwd
        self.hashSetDir = os.path.join(cwd,"hashSets")
        self.numberOfHashSets = 0
        filesInDir = os.listdir(self.hashSetDir)
        for file in filesInDir:
            if file.startswith("hashSet") and file[7:].isdigit():
                self.numberOfHashSets += 1
        self.filesChecked = 0
        if self.numberOfHashSets == 0:
            raise Exception("Cannot perfom hashScan without any hashes")

    # scan a file selected by the user.
    def scanFile(self,file):
        filePath = os.path.join(self.cwd,file)
        fileHash = ""
        # open the selected file and hashes it.
        with open(filePath,"rb") as target:
            fileHash = hashlib.md5(target).hexdigest()
        
        # compares the file hash against each "block" of hash sets
        for hashSetNumber in range(1,self.numberOfHashSets+1):
            with open("hashSet"+str(hashSetNumber),"rb") as hashSetRaw:
                hashSet = set(pickle.load(hashSetRaw))
                if fileHash in hashSet:
                    return True
        
        return False

    def scanDir(self,dir):
        dirPath = os.path.join(self.cwd,dir)
        # creates a list with the paths to all files in selected directory
        files2Scan = list()
        filesHash = list()
        filesInfected = list()
        for root,dirs,files in os.walk(dirPath,topdown=True):
            for fileNames in files:
                files2Scan.append(os.path.join(root,fileNames))

        self.filesChecked = len(files2Scan)

        # calculates all files hashes and appends then to filesHash list
        for filePath in files2Scan:
            with open(filePath,"rb") as openFile:
                filesHash.append(hashlib.md5(openFile.read()).hexdigest())
        
        # scans files present in directory, appends file in filesInfected list if it's hash matches any hashSet
        for hashSetNumber in range(1,self.numberOfHashSets+1):
            with open(os.path.join(self.cwd,"hashSets","hashSet") + str(hashSetNumber),"rb") as hashSetRaw:
                if files2Scan == 0:
                    break
                hashSet = set(pickle.load(hashSetRaw))

            for hash in filesHash:
                if hash in hashSet:
                    filesInfected.append(files2Scan[indexOf(filesHash,hash)])
                    files2Scan.pop(indexOf(filesHash,hash))
                    filesHash.remove(hash)
        
        return filesInfected
    
    def getFilesChecked(self):
        return self.filesChecked
                    
        
