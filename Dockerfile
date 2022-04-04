FROM python:3.9-slim

LABEL author='m.p.allahverdi@gmail.com'

RUN mkdir /flask_app /inventory /config

COPY app /flask_app/app
COPY config.py run.py requirements.txt agent.sh /flask_app/
COPY config/hostname_pattern.conf /config/

WORKDIR /flask_app/

RUN pip install -r requirements.txt && \
    chmod +x /flask_app/agent.sh

ENV PATTERN_CONFIG_FILE=/config/hostname_pattern.yml INVENTORY_FILE=/inventory/hosts.ini

EXPOSE $HTTP_PORT

CMD ["/usr/local/bin/python", "-u", "run.py"]