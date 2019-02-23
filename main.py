import socketserver
from request_handler import HttpHandler

Handler = HttpHandler

with socketserver.ThreadingTCPServer(("", 8888), Handler) as httpd:
    print("serving at port", 8888)
    httpd.serve_forever()




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