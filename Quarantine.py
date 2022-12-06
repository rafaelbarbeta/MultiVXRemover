import os
import base64
import hashlib

class Quarantine:

    def __init__(self,cwd):
        self.cwd = cwd
        self.quarantineDir = os.path.join(cwd,"Quarantine")
        if not os.path.isdir(self.quarantineDir):
            os.mkdir(self.quarantineDir)

    def quarantineFile(self,filePath):
        """
        Encode 'file' in base64 and write it to the quarantine directory along with its original location and md5 hash
        Original file is deleted
        """
        with open(filePath,"rb") as target:
            encodedFile = base64.b64encode(target.read())
        filePathQuarantine = os.path.join(self.cwd,self.quarantineDir,os.path.basename(filePath))
        with open(os.path.join(filePathQuarantine),"wb") as target:
            target.write(encodedFile)
        fileHash = hashlib.md5(encodedFile).hexdigest()
        with open(os.path.join(filePathQuarantine),"a") as target:
            target.write(":" + filePath + ":" + fileHash)
        os.remove(filePath)
        
    def quarantineList(self,files):
        """
        Quarantine a list of files
        'files' is a list of file paths
        """
        for file in files:
            self.quarantineFile(file)

    def restoreFile(self,file):
        """
        Decode 'file' from base64 and write it to its original location
        Remove the quarantined file from directory
        'file' is a filename 
        """
        filePathQuarantine = os.path.join(self.cwd,self.quarantineDir,file)
        with open(filePathQuarantine,"rb") as target:
            fileFields = target.read().split(b":")
            decodedFile = base64.b64decode(fileFields[0])
            originalPath = fileFields[1].decode("utf-8")
        if os.path.exists(os.path.split(originalPath)[0]):
            with open(originalPath,"wb") as target:
                target.write(decodedFile)
            os.remove(filePathQuarantine)
        else:
            with open(filePathQuarantine,"wb") as target:
                target.write(decodedFile)
    
    def removeFile(self,file):
        """
        Delete a quarantined file
        'file' is a file name
        """
        os.remove(os.path.join(self.cwd,self.quarantineDir,file))
    
    def getQuarantinedFiles(self):
        """
        Return a list of quarantined files
        This list is composed of file names
        """
        return os.listdir(self.quarantineDir)