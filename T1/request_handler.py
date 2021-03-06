import datetime

import requests
from http.server import BaseHTTPRequestHandler
from urllib import parse
import database


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

        if rpath == '/metrics':
            answer = database.select_metrics()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(answer.encode())
            return

        answer, status_code = handle(int(args["cifra"][0]))

        self.send_response(status_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(answer.encode())


def handle(request):
    if request == 1:
        return get_fengshui()
    elif request == 2:
        return get_cat_fact()
    elif request == 3:
        return get_date_fact()
    else:
        return "correct request", 200


def get_cat_fact():
    URL = "https://cat-fact.herokuapp.com/facts/random"
    PARAMS = {'animal': 'cat', 'amount': 1}
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        database.insert_metrics('cat fact', 'smth went wrong', '400', str(r.elapsed.total_seconds()))
        return 'something went wrong', 400
    data = r.json()
    # print(data)
    database.insert_metrics('cat fact', data['text'], '200', str(r.elapsed.total_seconds()))
    return data['text'], 200


def get_fengshui():
    URL = "https://fengshui-api.com/api/v1/findChineseSignOfYear"
    PARAMS = {'token': 'Y2fW484NC0F8J141Fdbj60ae5FD05502E7AgCc55', 'year': 1998, 'month': 8, 'day': 2, 'gender': 0}
    r = requests.get(url=URL, params=PARAMS, verify=False)
    print(r.content)
    if r.status_code != 200:
        database.insert_metrics('fengshui', 'smth went wrong', '400', str(r.elapsed.total_seconds()))
        return 'something went wrong', 400
    data = r.json()
    # print(data)

    database.insert_metrics('fengshui', data['result'], '200', str(r.elapsed.total_seconds()))

    return data['result'], 200


def get_date_fact():
    now = datetime.datetime.now()
    URL = "http://numbersapi.com/" + str(now.month) + "/" + str(now.day) + "/date"
    r = requests.get(url=URL)
    data = r.content.decode('utf8').replace("'", '"')
    if r.status_code != 200:
        database.insert_metrics('date fact', 'smth went wrong', '400', str(r.elapsed.total_seconds()))
        return "something went wrong", 400
    database.insert_metrics('date fact', data, '200', str(r.elapsed.total_seconds()))
    return data, 200
