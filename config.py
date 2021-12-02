import os


## --------------------------------------------------------------------- ##

app_dir = os.path.abspath(os.path.dirname(__file__))


PATTERN_CONFIG_FILE = 'config/hostname_pattern.conf' or os.environ.get('PATTERN_CONFIG_FILE')
INVENTORY_FILE = 'inventory/hosts.ini' or os.environ.get('INVENTORY_FILE')

HTTP_HOST = os.environ.get('HTTP_HOST')
HTTP_PORT = 5000 or os.environ.get('HTTP_PORT')
HTTP_PROTOCOL = 'http' or os.environ.get('HTTP_PROTOCOL')