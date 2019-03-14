import json
from http.server import BaseHTTPRequestHandler

import database
import helper_get
import helper_post


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

        try:
            arguments = json.loads(self.rfile.read(int(self.headers['content-length'])).decode())
        except Exception as e:
            print(e)
            self.send_response(400)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'Bad request')

        query, table = helper_post.build_post_select(parameters)
        if query == 0:
            self.send_response(404)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'Could not find what you requested')
        else:
            print(query)
            answer_array = database.interogate_database(query)
            print(answer_array)
            if answer_array == 409 or answer_array == 400:
                self.send_response(answer_array)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                if answer_array == 409:
                    self.wfile.write(b'Conflict')
                else:
                    self.wfile.write(b'Bad request')
            else:
                if len(answer_array) >= 1:
                    self.send_response(400)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(b'Bad request')
                else:
                    query, values = helper_post.build_post_insert_query(arguments, table)
                    database.insert_record(query, values)
                    answer = 'Ok'
                    status_code = 201
                    self.send_response(status_code)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(answer.encode())
