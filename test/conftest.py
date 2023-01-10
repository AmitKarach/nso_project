import subprocess
import threading
from http import HTTPStatus

import requests
from retry import retry

import db.db as db
from src.config import HOST, PORT
from src.server import app

URL_SERVICE_TEST = 'http://{}:{}'.format(HOST, PORT)


def pytest_sessionstart(session):
    subprocess.run(["docker-compose", "up", "-d", "-f", "../db/docker-compose.yml"])
    # app.run()
    global test_app_thread
    test_app_thread = threading.Thread(target=run_server)
    test_app_thread.start()
    server_is_up()


def pytest_runtest_setup():
    # code to run before each test
    db.delete_messages_from_db()


def run_server():
    app.run()


@retry(exceptions=Exception, tries=5, delay=2)
def server_is_up():
    response = requests.get(URL_SERVICE_TEST + '/Status')
    assert response.status_code == HTTPStatus.OK
