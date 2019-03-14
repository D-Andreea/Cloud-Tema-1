import json
from http.server import BaseHTTPRequestHandler

import database
import helper_delete
import helper_get
import helper_post
import helper_put


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
            if answer_array == 400:
                self.send_response(400)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'Bad request')
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

    def do_DELETE(self):
        parameters = self.path.split('/')
        parameters = list(filter(lambda a: a != "", parameters))

        query, value = helper_delete.build_delete_select(parameters)
        check_query, table = helper_get.build_get_select(parameters)
        if query == 0:
            status_code = 405
            answer = 'Bad request'
        else:
            print(query)
            check = database.interogate_database(check_query)
            print(check)
            if check == 400:
                status_code = 400
                answer = 'Bad request'
            elif len(check) < 1:
                status_code = 404
                answer = 'Record not found'
            else:
                status_code = database.delete_record(query, value)
                answer = 'Record deleted'

        self.send_response(status_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(answer.encode())

    def do_PUT(self):
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
        query, table = helper_put.build_put_select(parameters)
        if query == 0:
            self.send_response(404)
            self.wfile.write(b'Not found')
        else:
            query = helper_put.build_update_query(arguments, table, parameters[1])
            print(query)
            status_code = database.update_record(query)
            if status_code == 200:
                message = 'Updated'
            else:
                message = 'Bad request'
        self.send_response(status_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(message.encode())

