# import http.server
# import socketserver
# from request_handler import HttpHandler
#
# Handler = HttpHandler
#
# with http.server.ThreadingHTTPServer(("", 8888), Handler) as httpd:
#     print("serving at port", 8888)
#     httpd.serve_forever()


import database


database.db_main()
