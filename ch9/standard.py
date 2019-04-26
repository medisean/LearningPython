from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        response = {
            "status": "success",
            "data": "hello from server"
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))

def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print('press ^C to quit')
        server.serve_forever()
    except KeyboardInterrupt:
        print('interrupt')
        server.socket.close()

if __name__ == '__main__':
    main()
