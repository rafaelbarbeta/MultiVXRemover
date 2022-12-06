import os
import base64
import hashlib

class Quarantine:

    def __init__(self,cwd):
        self.cwd = cwd
        self.quarantineDir = os.path.join(cwd,"Quarantine")
        if not os.path.isdir(self.quarantineDir):
            os.mkdir(self.quarantineDir)

    def quarantineFile(self,file):
        """
        Encode 'file' in base64 and write it to the quarantine directory along with its original location and name
        The quarantined file will be named by its hash
        Example of quarantined file:

        WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCoK:C:/Users/username/Desktop/infected.exe
        """
        filePath = os.path.join(self.cwd,file)
        with open(filePath,"rb") as target:
            encodedFile = base64.b64encode(target.read())
        fileHash = hashlib.md5(encodedFile).hexdigest()
        with open(os.path.join(self.quarantineDir,fileHash),"wb") as target:
            target.write(encodedFile)
        with open(os.path.join(self.quarantineDir,fileHash),"a") as target:
            target.write(":" + filePath + ":" + file)
        
    def quarantineList(self,files):
        """
        Quarantine a list of files
        """
        for file in files:
            self.quarantineFile(file)

    def restoreFile(self,file):
        """
        Decode 'file' from base64 and write it to its original location
        The quarantined file will be named by the third field of the quarantined file
        """
        filePath = os.path.join(self.quarantineDir,file)
        with open(filePath,"rb") as target:
            fileFields = target.read().split(b":")
            decodedFile = base64.b64decode(fileFields[0])
            originalPath = fileFields[1].decode("utf-8")
            originalName = fileFields[2].decode("utf-8")
        with open(os.path.join(originalPath,originalName),"wb") as target:
            target.write(decodedFile)
    
    def destroyFile(self,file):
        """
        Delete a quarantined file
        """
        filePath = os.path.join(self.quarantineDir,file)
        os.remove(filePath)
    
    def getQuarantinedFiles(self):
        """
        Return a list of quarantined files
        """
        return os.listdir(self.quarantineDir)