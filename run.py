from gevent.pywsgi import WSGIServer
from app import app
import socket

## --------------------------------------------------------------------- ##

host = app.config['HTTP_HOST']
port = app.config['HTTP_PORT']
protocol = app.config['HTTP_PROTOCOL']

hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)

if __name__ == '__main__':
    print(f"TMWAY is available on {protocol}://{server_ip}:{port}\n")
    WSGIServer(('0.0.0.0', port), app).serve_forever()
