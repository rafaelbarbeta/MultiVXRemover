import os
import yara
import datetime
from shutil import rmtree
# This class main job is to manage yara rules and compiled rules
class RulesManagement:
    CRULES = "MultiVXRemoverCompiled" #directory of compiled rules
    def __init__(self,cwd):
        self.cRulesList = [] #list of path to the compiled rules
        self.currentDirectory = cwd
        self.cRulesDir = os.path.join(self.currentDirectory,RulesManagement.CRULES)
        if not os.path.exists(self.cRulesDir):
            os.mkdir(RulesManagement.CRULES)
        for root,dir,files in os.walk(self.cRulesDir,topdown=True): #load all already compiled rules to memory
            for fileNames in files:
                self.cRulesList.append(os.path.join(root,fileNames))

    #gets a folder name and add all rules in there, if they are yara rules
    def addRules(self,dirName):
        day = datetime.datetime.now()
        dirIndentifier = day.strftime("UP_%d-%m-%Y-%M")
        newCrulesDir = os.path.join(self.cRulesDir,dirIndentifier)
        os.mkdir(newCrulesDir)
        for root,dir,files in os.walk(dirName,topdown=True):
            for fileNames in files:
                newRawRule = os.path.join(root,fileNames)
                newCrule = self.addSingleRule(newRawRule,newCrulesDir)
                if newCrule != None: 
                    self.cRulesList.append(newCrule)
        return

    #add a single rule
    def addSingleRule(self,rulePath,newCrulesDir):
        try:
            newCruleObj = yara.compile(filepath=rulePath)
        except Exception:
            return
        newCrulesName = os.path.basename(rulePath)
        newCrules = os.path.join(newCrulesDir,newCrulesName)
        newCruleObj.save(newCrules)
        return newCrules
    #remove a "pack" of rules
    def removeRules(self,dirID):
        try:
            rmtree(os.path.join(self.cRulesDir,dirID))
        except Exception:
            return
        return
    def getCRulesList(self):
        return self.cRulesList
    # getter for current directory
    def getCurrentDirectory(self):
        return self.currentDirectory