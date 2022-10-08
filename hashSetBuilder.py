import pickle
import sys
import os

def main():
    #build the md5 malware hashes in memory
    hashSet = set()
    hashSetNumber = 1
    hashesdir = os.path.join(os.getcwd(),"VirusShareHashes")
    for file in os.listdir(hashesdir):
        with open(os.path.join(hashesdir,file),"r") as hashFile:
            hashesOfFile = hashFile.readlines()
            for hash in hashesOfFile[6:] :
                hashSet.add(hash[:32])
            # separes hashes sets in diferrent objects
            if sys.getsizeof(hashSet) >= 209715200 :
                #serialize the hashSet to disk 
                with open("hashSet" + str(hashSetNumber),"wb") as dump:
                    pickle.dump(hashSet,dump)
                hashSetNumber += 1
                hashSet = set()
    
    if len(hashSet) != 0:
        with open("hashSet" + str(hashSetNumber),"wb") as dump:
            pickle.dump(hashSet,dump)
             
if __name__ == '__main__':
    main()