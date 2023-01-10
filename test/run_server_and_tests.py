import json
import sys

from flask import request

from src.server import app
import threading
import pytest
from retry import retry
import requests
from src.config import HOST, PORT

URL_SERVICE_TEST = 'http://{}:{}'.format(HOST, PORT)

import yaml
import subprocess

subprocess.run(["docker-compose", "up", "-d", "-f", "../db/docker-compose.yml"])

@retry(exceptions=Exception, tries=5, delay=2)
def server_is_up():
    requests.get(URL_SERVICE_TEST + '/Status')

def run_tests():
     app.run()

test_app_thread = threading.Thread(target=run_tests)
test_app_thread.start()

server_is_up()
pytest.main(["../test"])

sys.exit()