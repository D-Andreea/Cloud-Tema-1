from http.server import BaseHTTPRequestHandler
from urllib import parse


class API(BaseHTTPRequestHandler):
    def get_path(self):
        args = {}
        idx = self.path.find('?')
        if idx >= 0:
            rpath = self.path[:idx]
            args = parse.parse_qs(self.path[idx + 1:])
        else:
            rpath = self.path
        return rpath, args


    def do_GET(self):  # do shit here
        rpath, args = self.get_path()

        print(args)
        if rpath == '/test':
            print(args["cifra"])

        answer, status_code = ()

        self.send_response(status_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(answer.encode())


    def do_POST(self): # do shit here
        return 0


