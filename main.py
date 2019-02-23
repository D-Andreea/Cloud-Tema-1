import socket
import requests
import json

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response.encode())
    client_connection.close()



# # api-endpoint
# URL = "https://cat-fact.herokuapp.com/facts/random"
#
# #/facts/random?animal=cat&amount=2
#
# # location given here
#
# # defining a params dict for the parameters to be sent to the API
# PARAMS = {'animal': 'cat', 'amount': 2}
#
# # sending get request and saving the response as response object
# r = requests.get(url=URL, params=PARAMS)
#
# # extracting data in json format
# print(r)
# if r.status_code != 200:
#     print(r.content)
# data = r.json()
#
# # extracting latitude, longitude and formatted address
# # of the first matching location
#
#
# # printing the output
# # print(data)
# print(data)
# #print(data["quota_remaining"])
#
#
# #fengshui api key: Y2fW484NC0F8J141Fdbj60ae5FD05502E7AgCc55