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

        answer, status_code = handle(int(args["cifra"][0]))

        self.send_response(status_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(answer.encode())


def handle(request):
    print("Client request: ", request)
    if request == 1:
        return get_fengshui()
    elif request == 2:
        return get_cat_fact()
    elif request == 3:
        return "MARIA IOANA TU ESTI CAMPIOANA", 200
    else:
        return "correct request", 200


def get_cat_fact():
    URL = "https://cat-fact.herokuapp.com/facts/random"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'animal': 'cat', 'amount': 1}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    #print(r)
    if r.status_code != 200:
        print(r.content)
    data = r.json()
    print(data)
    return data['text'], 200


def get_fengshui():
    URL = "https://fengshui-api.com/api/v1/findChineseSignOfYear"
    PARAMS = {'token': 'Y2fW484NC0F8J141Fdbj60ae5FD05502E7AgCc55', 'year': 2013, 'month': 8, 'day': 2, 'gender': 0}
    r = requests.get(url=URL, params=PARAMS)
    print(r.content)
    if r.status_code != 200:
        return 'something went wrong', 400
    data = r.json()
    print(data)
    return 'fengshui', 200
    #return data['text'], 200


