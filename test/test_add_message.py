import requests


def post_message(data):
    return requests.post('http://127.0.0.1:5000/AddMessage', json=data)


def test_add_message_with_currect_data():
    data = {
        'application_id': 1,
        'session_id': 'aaaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    response = post_message(data)
    assert response.status_code == 201
    assert response.json() == {'status': 'success'}
    requests.delete('http://127.0.0.1:5000/DeleteMessage?applicationId=1')

# **********************************************************************************************************************
# invalid data:


def test_add_message_with_invalid_application_id():
    data = {
        'application_id': 'invalid',
        'session_id': 'aaaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    response = post_message(data)
    assert response.status_code == 400


def test_add_message_with_invalid_session_id():
    data = {
        'application_id': 1,
        'session_id': 1231,
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    response = post_message(data)
    assert response.status_code == 400


def test_add_message_with_invalid_message_id():
    data = {
        'application_id': 1,
        'session_id': 'bbbb',
        'message_id': 123,
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    response = post_message(data)
    assert response.status_code == 400


def test_add_message_with_invalid_participants():
    data = {
        'application_id': 1,
        'session_id': 'aaa',
        'message_id': 'bbbb',
        'participants': 123,
        'content': 'Hi, how are you today?'
    }
    response = post_message(data)
    assert response.status_code == 400


def test_add_message_with_invalid_content():
    data = {
        'application_id': 1,
        'session_id': 'aaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 1323
    }
    response = post_message(data)
    assert response.status_code == 400


# **********************************************************************************************************************
# missing data:

def test_add_message_with_missing_application_id():
    data = {
        'session_id': 'aaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    response = post_message(data)
    assert response.status_code == 400


def test_add_message_with_missing_session_id():
    data = {
        'application_id': 1,
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    response = post_message(data)
    assert response.status_code == 400


def test_add_message_with_missing_message_id():
    data = {
        'application_id': 1,
        'session_id': 'aaa',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    response = post_message(data)
    assert response.status_code == 400


def test_add_message_with_missing_participants():
    data = {
        'application_id': 1,
        'session_id': 'aaa',
        'message_id': 'bbbb',
        'content': 'Hi, how are you today?'
    }
    response = post_message(data)
    assert response.status_code == 400


def test_add_message_with_missing_content():
    data = {
        'application_id': 1,
        'session_id': 'aaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
    }
    response = post_message(data)
    assert response.status_code == 400
