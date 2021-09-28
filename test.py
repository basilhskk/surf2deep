import surface2deep

client = surface2deep.surf2deep()




## testing





#


import http.server
import socketserver
from http import HTTPStatus


# url = "http://blackmax7su6mbwtcyo3xwtpfxpm356jjqrs34y4crcytpw7mifuedyd.onion/"

# with open("ASD.html","w")as f:
#     f.write(client.get(url))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        url = "http://blackmax7su6mbwtcyo3xwtpfxpm356jjqrs34y4crcytpw7mifuedyd.onion/"
        self.wfile.write(client.get(url).encode())


httpd = socketserver.TCPServer(('', 8001), Handler)
httpd.serve_forever()


