from gevent.pywsgi import WSGIServer
from app import app
import socket

## --------------------------------------------------------------------- ##

port = app.config['HTTP_PORT']
protocol = app.config['HTTP_PROTOCOL']
prefix = app.config['TMWAY_PREFIX']

hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)


if __name__ == '__main__':
    print(f"PATTERN_CONFIG_FILE = {app.config['PATTERN_CONFIG_FILE']}")
    print(f"INVENTORY_FILE = {app.config['INVENTORY_FILE']}")
    print(f"TMWAY is available on {protocol}://{server_ip}:{port}/{prefix}\n")
    WSGIServer(('0.0.0.0', port), app).serve_forever()
