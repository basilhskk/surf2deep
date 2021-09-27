import surface2deep

client = surface2deep.surf2deep()


client.session.get("http://blackmax7su6mbwtcyo3xwtpfxpm356jjqrs34y4crcytpw7mifuedyd.onion/").content


# import http.server
# import socketserver
# from http import HTTPStatus


# class Handler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(HTTPStatus.OK)
#         self.end_headers()

#         self.wfile.write()


# httpd = socketserver.TCPServer(('', 8000), Handler)
# httpd.serve_forever()


