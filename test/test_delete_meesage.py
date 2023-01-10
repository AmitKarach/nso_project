from http import HTTPStatus

import requests

import test_utils


def test_delete_message_with_application_id_without_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' url is requested (DELETE) with the params: applicationId
    THEN status code should be 404 because there is no POST message
    """
    response = test_utils.delete_message({'applicationId': 1})
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_message_with_session_id_without_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' url is requested (DELETE) with the params: sessionId
    THEN status code should be 404 because there is no POST message
    """
    response = test_utils.delete_message({'sessionId': 'aaaa'})
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_message_with_message_id_without_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/DeleteMessage' url is requested (DELETE) with the params: messageId
    THEN status code should be 404 because there is no POST message
    """
    response = test_utils.delete_message({'messageId': 'bbbb'})
    assert response.status_code == HTTPStatus.NOT_FOUND


# ***********************************************************************************************************************


def test_delete_one_message_with_application_id():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: applicationId
        THEN delete all instances (in this case there is only one) of messages with the same applicationId
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.delete_message({'applicationId': 1})
    assert response.status_code == HTTPStatus.OK


def test_delete_one_message_with_session_id():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: sessionId
        THEN delete all instances (in this case there is only one) of messages with the same sessionId
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.delete_message({'sessionId': 'aaaa'})
    assert response.status_code == HTTPStatus.OK


def test_delete_one_message_with_message_id():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: messageId
        THEN delete all instances (in this case there is only one) of messages with the same messageId
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.delete_message({'messageId': 'bbbb'})
    assert response.status_code == HTTPStatus.OK


# **********************************************************************************************************************
# not found in data base:


def test_delete_message_with_application_id_not_in_db():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: applicationId that are not in the db
        THEN return status 404- not found
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.delete_message({'applicationId': 2})
    test_utils.delete_message({'applicationId': 1})
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_message_with_session_id_not_in_db():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: sessionId that are not in the db
        THEN return status 404- not found
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.delete_message({'sessionId': 'bbbb'})
    test_utils.delete_message({'sessionId': 'aaaa'})
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_message_with_message_id_not_in_db():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: messageId that are not in the db
        THEN return status 404- not found
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.delete_message({'messageId': 'aaaa'})
    test_utils.delete_message({'messageId': 'bbbb'})
    assert response.status_code == HTTPStatus.NOT_FOUND


# **********************************************************************************************************************
# delete all instances


def test_delete_all_messages_with_application_id():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: applicationId
        THEN delete all instances of the messages with the same applicationId
    """
    test_utils.enter_data_to_db('application_id', 5)
    params = {'applicationId': 1}
    response = test_utils.delete_message(params)
    get_response = requests.get(test_utils.URL_SERVICE_TEST + '/GetMessage', params=params)
    assert response.status_code == HTTPStatus.OK
    assert get_response.status_code == HTTPStatus.NOT_FOUND


def test_delete_all_messages_with_session_id():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: sessionId
        THEN delete all instances of the messages with the same sessionId
    """
    test_utils.enter_data_to_db('session_id', 5)
    params = {'sessionId': 'aaaa'}
    response = test_utils.delete_message(params)
    get_response = requests.get(test_utils.URL_SERVICE_TEST + '/GetMessage', params=params)
    assert response.status_code == HTTPStatus.OK
    assert get_response.status_code == HTTPStatus.NOT_FOUND


# **********************************************************************************************************************


def test_delete_only_messages_with_application_id():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: applicationId
        THEN delete all instances of the messages with the same applicationId and leave the one with different applicationId
    """
    test_utils.enter_data_to_db('application_id', 5)
    data = test_utils.create_message_object(2, 'aaaa', 'cccc', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    params = {'applicationId': 1}
    response = test_utils.delete_message(params)
    get_response = requests.get(test_utils.URL_SERVICE_TEST + '/GetMessage', params={'applicationId': 2})
    test_utils.delete_message({'applicationId': 2})
    assert response.status_code == HTTPStatus.OK
    assert get_response.json()[0] == data


def test_delete_only_messages_with_session_id():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: sessionId
        THEN delete all instances of the messages with the same sessionId and leave the one with different sessionId
    """
    test_utils.enter_data_to_db('session_id', 5)
    data = test_utils.create_message_object(1, 'bbbb', 'cccc', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    params = {'sessionId': 'aaaa'}
    response = test_utils.delete_message(params)
    get_response = requests.get(test_utils.URL_SERVICE_TEST + '/GetMessage', params={'sessionId': 'bbbb'})
    test_utils.delete_message({'sessionId': 'bbbb'})
    assert response.status_code == HTTPStatus.OK
    assert get_response.json()[0] == data


def test_delete_only_messages_with_message_id():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: messageId
        THEN delete the message with the same messageId and leave the one with different messageId
    """
    data1 = test_utils.create_message_object(1, 'bbbb', 'a', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    data2 = test_utils.create_message_object(1, 'bbbb', 'b', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data1)
    test_utils.post_message(data2)
    params = {'messageId': 'a'}
    response = test_utils.delete_message(params)
    get_response = requests.get(test_utils.URL_SERVICE_TEST + '/GetMessage', params={'messageId': 'b'})
    test_utils.delete_message({'messageId': 'b'})
    assert response.status_code == HTTPStatus.OK
    assert get_response.json()[0] == data2


# ******************************************************************************************************************

def test_delete_with_two_params():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: sessionId and applicationID
        THEN delete the message with the same sessionId and applicationID and leave the one with different messageId
    """
    content = 'Hi, how are you today?'
    data_equal_seesion_and_app = test_utils.create_message_object(1, 'bbbb', 'a', ['avi aviv', 'moshe cohen'], content)
    data_equal_seesion_and_app2 = test_utils.create_message_object(1, 'bbbb', 'b', ['avi aviv', 'moshe cohen'], content)
    data_equal_seesion = test_utils.create_message_object(2, 'bbbb', 'c', ['avi aviv', 'moshe cohen'], content)
    data_equal_app = test_utils.create_message_object(1, 'aaaa', 'd', ['avi aviv', 'moshe cohen'], content)
    data =[data_equal_seesion_and_app,data_equal_seesion_and_app2,data_equal_app,data_equal_seesion]
    for d in data:
        test_utils.post_message(d)
    params = {'applicationId': 1, 'sessionId': 'bbbb'}
    response = test_utils.delete_message(params)
    get_response = requests.get(test_utils.URL_SERVICE_TEST)
    test_utils.delete_message({'messageId': 'c'})
    test_utils.delete_message({'messageId': 'd'})
    assert response.status_code == HTTPStatus.OK
    assert data_equal_app in get_response.json() and data_equal_seesion in get_response.json()
