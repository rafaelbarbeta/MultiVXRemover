import os
import RulesManagement
import Scanner
#prototype main, just for testing
def main():
    rmng = RulesManagement.RulesManagement(os.getcwd())
    scan = Scanner.Scanner(rmng,False)
    print("MultiVXRemover : Wipe evil software off your computer!")
    op = "none"
    while op != "exit":
        operation = str(input("Please choose de options Below:\n1) scan <directory>\n2) addRule <directory>\n3) exit\n"))
        selection, directory = tuple(operation.split(" "))
        if selection == "scan":
            fileMatches = scan.scanDirectory(directory)
            if len(fileMatches) != 0:
                print("Threats Detected!")
                for key, value in fileMatches.items():
                    print(f"{key} is {value}")
            else:
                print("No virus found")
        elif selection == "addRule":
            rmng.addRules(directory)
        elif selection == "exit":
            print("Bye")
            return 
        else:
            print("Error! option does not exist")
        
if __name__ == '__main__':
    main()