import os
import yara

class Scanner:

    def __init__(self,rulesM,quarantine):
        self.rulesM = rulesM
        self.quarantine = quarantine
        self.dictMatches = {}
        #reminder: counter for files scanned and actual threats detected!

    def malwareFound(self,data):
        return yara.CALLBACK_ABORT
        
    def scanFile(self,file):
        filePath = os.path.join(self.rulesM.getCurrentDirectory(),file)
        cRulesList = self.rulesM.getCRulesList()
        for i in range(0,len(cRulesList)):
            singleRuleFile = yara.load(cRulesList[i])
            match = singleRuleFile.match(filePath,callback=self.malwareFound,which_callbacks=yara.CALLBACK_MATCHES)
            if len(match) != 0:
                self.dictMatches.update({file : match[0]}) #not sure 0 is the field of match
                self.quarantineFile(file)
                return (file,match[0]) # returns a tupple with the file and 
        return

    def scanDirectory(self,dir):
        targetDir = os.path.join(self.rulesM.getCurrentDirectory(),dir)
        for root,dirs,files in os.walk(targetDir,topdown=True):
            for fileNames in files:
                self.scanFile(os.path.join(root,fileNames))
        return self.getMatches()
                

    def quarantineFile(self,file):
        pass

    def getMatches(self):
        # returns the matches dictionary and destroys the original
        matches = self.dictMatches.copy()
        self.dictMatches = {}
        return matches




