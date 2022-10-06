import os
import RulesManagement
import Scanner
import yara
#prototype main, just for testing
def main():
    rmng = RulesManagement.RulesManagement(os.getcwd())
    scan = Scanner.Scanner(rmng,False)
    print("MultiVXRemover : Wipe evil software off your computer!")
    op = "none"
    while True:
            try :
                operation = str(input("Please choose de options Below:\n1) scan <directory>\n2) addRule <directory>\n3) exit\n"))
                args = list(operation.split(" "))
                if args[0] == "scan":
                    fileMatches = scan.scanDirectory(args[1])
                    if len(fileMatches) != 0:
                        print("Threats Detected!")
                        for key, value in fileMatches.items():
                            print(f"{key} is {value}")
                    else:
                        print("No threats found")
                elif args[0] == "addRule":
                    rmng.addRules(args[1])
                elif args[0] == "exit":
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