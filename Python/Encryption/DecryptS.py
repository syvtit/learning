from cryptography.fernet import Fernet
import os

def decfile(decfile):
    with open('C://Users//sy_vutien//Desktop//Samples//filekey.key','rb') as filekey:
        key = filekey.read()

    #using the generated key
    fernet = Fernet(key)

    #opening the original file to encrypt
    with open (decfile,'rb') as file:
        encrypted = file.read()
    #decrypting the file
    decrypted = fernet.decrypt(encrypted)
    #writing the decrypted data
    with open (decfile,'wb') as dec_file:
        dec_file.write(decrypted)

    #rename file
    newfile = decfile.replace(".syvtit","")
    os.renames(decfile,newfile)
def decS(path):
    for (root, dirs, file) in os.walk(path):
        for f in file:
            fpath = ""
            if (str(root).endswith("//")):
                fpath = str(root) + str(f)
            else:
                fpath = (str(root) + "//" + str(f)).replace("\\", "//")
            if(fpath.endswith(".syvtit")):
                print(fpath)
                decfile(fpath)

decS("S://")
#decfile("S://test//file-sample_100kB.docx.syvtit")
#decfile('Book 1.xlsx.syvtit')