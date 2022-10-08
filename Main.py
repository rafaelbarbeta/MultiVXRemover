import os
import HashScan
import RulesManagement
import Scanner
import yara

def main():
    rmng = RulesManagement.RulesManagement(os.getcwd())
    scan = Scanner.Scanner(rmng,False)
    hashScan = HashScan.HashScan(os.getcwd())
    print("MultiVXRemover : Wipe evil software off your computer!")
    op = "none"
    while True:
            try :
                print("Please choose de options Below:")
                print("1) scan <directory>")
                print("2) addRules <directory>")
                print("3) hashScan <directory>")
                print("4) exit")
                operation = str(input())
                args = list(operation.split(" "))
                if args[0] == "scan" or args[0] == "1":
                    fileMatches = scan.scanDirectory(args[1])
                    if len(fileMatches) != 0:
                        print("Threats Detected!")
                        for key, value in fileMatches.items():
                            print(f"{key} is {value}")
                    else:
                        print("No threats found")
                elif args[0] == "addRules" or args[0] == "2":
                    rmng.addRules(args[1])
                elif args[0] == "hashScan" or args[0] == "3":
                    filesInfected = hashScan.scanDir(args[1])
                    for file in filesInfected:
                        print(file + " : Malware")
                    totalDetected = len(filesInfected)
                    totalChecked = hashScan.getFilesChecked()
                    percentOfDetection = totalDetected / totalChecked
                    print("Results : ")
                    print("Detected " + str(totalDetected) + " out of " + str(totalChecked) + " as malware")
                    print(str(percentOfDetection) + "%")
                elif args[0] == "exit" or args[0] == "4":
                    print("Bye")
                    return 
                else:
                    print("Error! option does not exist")
            except IndexError:
                print("Error! Not enough arguments for selected option")
            except yara.Error:
                print("Error! MultiVXRemoverCompiled directory not found!")
                exit()



if __name__ == '__main__':
    main()