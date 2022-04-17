import os


## --------------------------------------------------------------------- ##

app_dir = os.path.abspath(os.path.dirname(__file__))


PATTERN_CONFIG_FILE = os.getenv('PATTERN_CONFIG_FILE', 'config/hostname_pattern.yml')
INVENTORY_PATH = os.getenv('INVENTORY_PATH', 'inventory')
INVENTORY_FILE = os.getenv('INVENTORY_FILE', f'{INVENTORY_PATH}/hosts.ini')

HTTP_PORT = os.getenv('HTTP_PORT', 5000)
HTTP_PROTOCOL = os.getenv('HTTP_PROTOCOL', 'http')

TMWAY_PREFIX = os.getenv('TMWAY_PREFIX', 'tmway')