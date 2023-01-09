from http import HTTPStatus

import requests

import test_utils

def test_get_message_with_message_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: applicationId
    THEN status code should be 200 and te return data should be equal to the posted data
    """
    data = test_utils.get_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'applicationId': 1})
    assert response.status_code == HTTPStatus.OK
    assert response.json()[0] == data
    test_utils.delete_message({'applicationId': 1})

def test_get_message_with_session_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: sessionId
    THEN status code should be 200 and te return data should be equal to the posted data
    """
    data = test_utils.get_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'sessionId': 'aaaa'})
    assert response.status_code == HTTPStatus.OK
    assert response.json()[0] == data
    test_utils.delete_message({'sessionId': 'aaaa'})

def test_get_message_with_message_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: messageId
    THEN status code should be 200 and te return data should be equal to the posted data
    """
    data = test_utils.get_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'messageId': 'bbbb'})
    assert response.status_code == HTTPStatus.OK
    assert response.json()[0] == data
    test_utils.delete_message({'messageId': 'bbbb'})


#**********************************************************************************************************************

def test_get_message_with_worng_application_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the worng params: applicationId
    THEN status code should be 404
    """
    data = test_utils.get_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'applicationId': 2})
    assert response.status_code == HTTPStatus.NOT_FOUND
    test_utils.delete_message({'applicationId': 1})


def test_get_message_with_worng_session_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the worng params: sessionId
    THEN status code should be 404
    """
    data = test_utils.get_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'sessionId': 'bbbb'})
    assert response.status_code == HTTPStatus.NOT_FOUND
    test_utils.delete_message({'sessionId': 'aaaa'})


def test_get_message_with_worng_message_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the worng params: messageId
    THEN status code should be 404
    """
    data = test_utils.get_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'messageId': 'aaaa'})
    assert response.status_code == HTTPStatus.NOT_FOUND
    test_utils.delete_message({'messageId': 'bbbb'})


#**********************************************************************************************************************


def test_get_all_messages_with_application_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: applicationId
    THEN status code should be 200 and te return data should be equal to the posted data
    """
    entered_data=test_utils.enter_data_to_db('application_id', 5)
    data = test_utils.get_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    entered_data.append(data)
    test_utils.post_message(data)
    response = test_utils.get_message({'applicationId': 1})
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == len(entered_data)
    test_utils.delete_message({'applicationId': 1})

def test_get_all_messages_with_session_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: sessionId
    THEN status code should be 200 and te return data should be equal to the posted data
    """
    entered_data=test_utils.enter_data_to_db('session_id', 5)
    data = test_utils.get_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    entered_data.append(data)
    test_utils.post_message(data)
    response = test_utils.get_message({'sessionId': 'aaaa'})
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == len(entered_data)
    test_utils.delete_message({'sessionId': 'aaaa'})