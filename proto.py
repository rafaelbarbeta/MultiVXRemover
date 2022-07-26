from ast import walk
import yara
import os

def malwareFound(data):
    print("Malware encontrado!: "+ data.get("rule"))
    return yara.CALLBACK_ABORT

def main():
    filesToScan = []
    #anda no diretorio especificado
    for root,dirs,filenames in os.walk("./teste",topdown=True):
        for files in filenames:
            filesToScan.append(os.path.join(root,files))
    # regra para compilar (podem ser mais que 1)
    regraNome = input("Digite o nome do arquivo de regra para compilar:")
    regra = yara.compile(filepath=os.path.join(os.getcwd(),regraNome))
    regra.save(os.path.join(os.getcwd(),"regraCompilada"))
    alvoScan = input("Digite o nome do arquivo para escanear:")
    alvoResult = regra.match(os.path.join(os.getcwd(),alvoScan),callback=malwareFound,which_callbacks=yara.CALLBACK_MATCHES)
    print("Scan Terminado!")
    print(alvoResult) #para debug

if __name__ == '__main__':
    main()