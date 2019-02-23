import requests
from http.server import BaseHTTPRequestHandler
from urllib import parse


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):  # do shit here
        args = {}
        idx = self.path.find('?')
        if idx >= 0:
            rpath = self.path[:idx]
            args = parse.parse_qs(self.path[idx + 1:])
        else:
            rpath = self.path
        print(args)

        if rpath == '/test':
            print(args["cifra"])

        # self.send_response(r.status_code)
        # self.send_header('Content-type', 'text-html')
        # self.end_headers()
        self.wfile.write(b"great job!")


def handle(request):
    print("Client request: ", request)
    get_cat_fact()
    return "correct request"


def get_cat_fact(self):
    URL = "https://cat-fact.herokuapp.com/facts/random"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'animal': 'cat', 'amount': 1}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    print(r)
    if r.status_code != 200:
        print(r.content)
    data = r.json()
    print(data)
