import json
from http.server import BaseHTTPRequestHandler

import database
import helper_get


class API(BaseHTTPRequestHandler):
    def do_GET(self):
        parameters = self.path.split('/')
        parameters = list(filter(lambda a: a != "", parameters))

        query, table = helper_get.build_get_select(parameters)
        if query == 0:
            status_code = 404
            answer = 'Could not find what you requested'
        else:
            answer_array = database.interogate_database(query)
            answer = list()
            for line in answer_array:
                answer_dict = helper_get.transform_array_to_dict(line, table)
                answer.append(answer_dict)
            status_code = 200

        self.send_response(status_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(answer).encode())

    def do_POST(self):
        parameters = self.path.split('/')
        parameters = list(filter(lambda a: a != "", parameters))

        query, table = helper_get.ostbuild_get_select(parameters)
        if query == 0:
            status_code = 404
            answer = 'Could not find what you requested'
        else:
            answer_array = database.interogate_database(query)
            answer = list()
            for line in answer_array:
                answer_dict = helper_get.transform_array_to_dict(line, table)
                answer.append(answer_dict)
            status_code = 200

        self.send_response(status_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(answer).encode())


