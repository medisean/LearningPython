from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404, 'File not found')

def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print('welcome to machine')
        print('press ^C to quit')
        server.serve_forever()
    except KeyboardInterrupt:
        print('interrupt')
        server.socket.close()

if __name__ == '__main__':
    main()