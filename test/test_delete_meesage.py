import requests


def delete_message(params):
    return requests.delete('http://127.0.0.1:5000/DeleteMessage', params=params)


def post_message(data):
    return requests.post('http://127.0.0.1:5000/AddMessage', json=data)


"""
enters a large number of data (the size of how_many) where all the params are different except for key
"""


def enter_data_to_db(key, how_many):
    data = {
        'application_id': 1,
        'session_id': 'aaaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    post_message(data)
    for i in range(how_many):
        for val in data:
            if val == 'participants' or val == 'content':
                break;
            elif val != key:
                data[val] = data[val] + type(data[val])(i + 1)

        post_message(data)


"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: applicationId
    THEN delete all instances (in this case there is only one) of messages with the same applicationId
"""


def test_delete_one_message_with_applicationId():
    data = {
        'application_id': 1,
        'session_id': 'aaaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    post_message(data)
    response = delete_message({'applicationId': 1})
    assert response.status_code == 200


"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: sessionId
    THEN delete all instances (in this case there is only one) of messages with the same sessionId
"""


def test_delete_one_message_with_sessionId():
    data = {
        'application_id': 1,
        'session_id': 'aaaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    post_message(data)
    response = delete_message({'sessionId': 'aaaa'})
    assert response.status_code == 200


"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: messageId
    THEN delete all instances (in this case there is only one) of messages with the same messageId
"""


def test_delete_one_message_with_messageId():
    data = {
        'application_id': 1,
        'session_id': 'aaaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    post_message(data)
    response = delete_message({'messageId': 'bbbb'})
    assert response.status_code == 200


# **********************************************************************************************************************
# not found in data base:

"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: applicationId that are not in the db
    THEN return status 404- not found
"""


def test_delete_message_with_applicationId_not_in_db():
    data = {
        'application_id': 1,
        'session_id': 'aaaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    post_message(data)
    response = delete_message({'applicationId': 2})
    delete_message({'applicationId': 1})
    assert response.status_code == 404


"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: sessionId that are not in the db
    THEN return status 404- not found
"""


def test_delete_message_with_sessionId_not_in_db():
    data = {
        'application_id': 1,
        'session_id': 'aaaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    post_message(data)
    response = delete_message({'sessionId': 'bbbb'})
    delete_message({'sessionId': 'aaaa'})
    assert response.status_code == 404


"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: messageId that are not in the db
    THEN return status 404- not found
"""


def test_delete_message_with_messageId_not_in_db():
    data = {
        'application_id': 1,
        'session_id': 'aaaa',
        'message_id': 'bbbb',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    post_message(data)
    response = delete_message({'messageId': 'aaaa'})
    delete_message({'messageId': 'bbbb'})
    assert response.status_code == 404


# **********************************************************************************************************************
# delete all instances


"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: applicationId
    THEN delete all instances of the messages with the same applicationId
"""


def test_delete_all_messages_with_applicationId():
    enter_data_to_db('application_id', 5)
    params = {'applicationId': 1}
    response = delete_message(params)
    get_response = requests.get('http://127.0.0.1:5000/GetMessage', params=params)
    assert response.status_code == 200
    assert get_response.status_code == 404


"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: sessionId
    THEN delete all instances of the messages with the same sessionId
"""


def test_delete_all_messages_with_sessionId():
    enter_data_to_db('session_id', 5)
    params = {'sessionId': 'aaaa'}
    response = delete_message(params)
    get_response = requests.get('http://127.0.0.1:5000/GetMessage', params=params)
    assert response.status_code == 200
    assert get_response.status_code == 404


# **********************************************************************************************************************


"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: applicationId
    THEN delete all instances of the messages with the same applicationId and leave the one with different applicationId
"""


def test_delete_only_messages_with_applicationId():
    enter_data_to_db('application_id', 5)
    data = {
        'application_id': 2,
        'session_id': 'aaaa',
        'message_id': 'cccc',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    post_message(data)
    params = {'applicationId': 1}
    response = delete_message(params)
    get_response = requests.get('http://127.0.0.1:5000/')
    delete_message({'applicationId': 2})
    assert response.status_code == 200
    assert get_response.json()[0] == data

"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: sessionId
    THEN delete all instances of the messages with the same sessionId and leave the one with different sessionId
"""


def test_delete_only_messages_with_sessionId():
    enter_data_to_db('application_id', 5)
    data = {
        'application_id': 1,
        'session_id': 'bbbb',
        'message_id': 'cccc',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    post_message(data)
    params = {'sessionId': 'aaaa'}
    response = delete_message(params)
    get_response = requests.get('http://127.0.0.1:5000/')
    delete_message({'applicationId': 2})
    assert response.status_code == 200
    assert get_response.json()[0] == data

"""
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' page is requested (DELETE) with the params: sessionId
    THEN delete the message with the same messageId and leave the one with different messageId
"""


def test_delete_only_messages_with_messageId():
    data1 = {
        'application_id': 1,
        'session_id': 'bbbb',
        'message_id': 'a',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    data2 = {
        'application_id': 1,
        'session_id': 'bbbb',
        'message_id': 'b',
        'participants': ['avi aviv', 'moshe cohen'],
        'content': 'Hi, how are you today?'
    }
    post_message(data1)
    post_message(data1)
    params = {'message_id': 'a'}
    response = delete_message(params)
    get_response = requests.get('http://127.0.0.1:5000/')
    delete_message({'applicationId': 2})
    assert response.status_code == 200
    assert get_response.json()[0] == data2
