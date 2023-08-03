import os
import HashScan
import RulesManagement
import Scanner
import Quarantine
import yara

def main():
    rmng = RulesManagement.RulesManagement(os.getcwd())
    hashScan = HashScan.HashScan(os.getcwd())
    quar = Quarantine.Quarantine(os.getcwd())
    scan = Scanner.Scanner(rmng,quar)
    print("MultiVXRemover : Wipe evil software off your computer!")
    while True:
            try :
                print("Please choose an option below:")
                print("1) scan <directory>")
                print("2) addRules <directory>")
                print("3) hashScan <directory>")
                print("4) viewQuarantine")
                print("5) restore <file>")
                print("6) remove <file>")
                print("7) exit")
                operation = str(input())
                args = list(operation.split(" "))
                if args[0] == "scan" or args[0] == "1":
                    fileMatches = scan.scanDirectory(args[1])
                    if len(fileMatches) != 0:
                        print("Threats Detected!")
                        for key, value in fileMatches.items():
                            print(f"{key} is {value}")
                            quar.quarantineFile(key)
                        print("All detected threats have been quarantined")
                    else:
                        print("No threats found")
                elif args[0] == "addRules" or args[0] == "2":
                    rmng.addRules(args[1])
                elif args[0] == "hashScan" or args[0] == "3":
                    filesInfected = hashScan.scanDir(args[1])
                    for file in filesInfected:
                        print(file + " : Malware")
                        quar.quarantineFile(file)
                    totalDetected = len(filesInfected)
                    totalChecked = hashScan.getFilesChecked()
                    percentOfDetection = (totalDetected / totalChecked) * 100
                    print("Results : ")
                    print("Detected " + str(totalDetected) + " out of " + str(totalChecked) + " as malware")
                    print(str(percentOfDetection) + "%")
                    print("All detected threats have been quarantined")
                elif args[0] == "viewQuarantine" or args[0] == "4":
                    quarantinedFiles = quar.getQuarantinedFiles()
                    if len(quarantinedFiles) == 0:
                        print("No files in quarantine")
                    else:
                        for file in quarantinedFiles:
                            print(file)
                elif args[0] == "restore" or args[0] == "5":
                    quar.restoreFile(args[1])
                    print("File restored")
                elif args[0] == "remove" or args[0] == "6":
                    quar.removeFile(args[1])
                    print("File removed")
                elif args[0] == "exit" or args[0] == "7":
                    print("Bye")
                    return 
                else:
                    print("Error! option does not exist")
            except IndexError:
                print("Error! Not enough arguments for selected option")
            except yara.Error:
                print("Error! MultiVXRemoverCompiled directory not found!")
                exit()
            except FileNotFoundError:
                print("Error! Directory or file not found!")

if __name__ == '__main__':
    main()