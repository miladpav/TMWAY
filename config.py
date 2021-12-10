import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

## --------------------------------------------------------------------- ##

app_dir = os.path.abspath(os.path.dirname(__file__))


PATTERN_CONFIG_FILE = os.environ.get('PATTERN_CONFIG_FILE') or 'config/hostname_pattern.conf'
INVENTORY_FILE = os.environ.get('INVENTORY_FILE') or 'inventory/hosts.ini'

HTTP_PORT = os.environ.get('HTTP_PORT') or 5000
HTTP_PROTOCOL = os.environ.get('HTTP_PROTOCOL') or 'http'

TMWAY_PREFIX = os.environ.get('TMWAY_PREFIX') or 'tmway'