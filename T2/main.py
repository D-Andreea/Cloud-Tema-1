import http.server
from server import API
import database

Handler = API

database.db_main()

with http.server.HTTPServer(("", 8888), Handler) as httpd:
    print("serving at port", 8888)
    httpd.serve_forever()





