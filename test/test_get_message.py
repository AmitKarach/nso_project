from http import HTTPStatus

import requests

import test_utils


def test_get_message_with_application_id_without_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: applicationId
    THEN status code should be 404 because there is no POST message
    """
    response = test_utils.get_message({'applicationId': 1})
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_message_with_session_id_without_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: sessionId
    THEN status code should be 404 because there is no POST message
    """
    response = test_utils.get_message({'sessionId': 'aaaa'})
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_message_with_message_id_without_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: messageId
    THEN status code should be 404 because there is no POST message
    """
    response = test_utils.get_message({'messageId': 'bbbb'})
    assert response.status_code == HTTPStatus.NOT_FOUND


# ***********************************************************************************************************************


def test_get_message_with_application_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: applicationId
    THEN status code should be 200 and te return data should be equal to the posted data
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'applicationId': 1})
    assert response.status_code == HTTPStatus.OK
    assert response.json()[0] == data


def test_get_message_with_session_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: sessionId
    THEN status code should be 200 and te return data should be equal to the posted data
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'sessionId': 'aaaa'})
    assert response.status_code == HTTPStatus.OK
    assert response.json()[0] == data


def test_get_message_with_message_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: messageId
    THEN status code should be 200 and te return data should be equal to the posted data
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'messageId': 'bbbb'})
    assert response.status_code == HTTPStatus.OK
    assert response.json()[0] == data


# **********************************************************************************************************************

def test_get_message_with_worng_application_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the worng params: applicationId
    THEN status code should be 404
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'applicationId': 2})
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_message_with_worng_session_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the worng params: sessionId
    THEN status code should be 404
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'sessionId': 'bbbb'})
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_message_with_worng_message_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the worng params: messageId
    THEN status code should be 404
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    test_utils.post_message(data)
    response = test_utils.get_message({'messageId': 'aaaa'})
    assert response.status_code == HTTPStatus.NOT_FOUND


# **********************************************************************************************************************


def test_get_all_messages_with_application_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: applicationId
    THEN status code should be 200 and te return data should be equal to the posted data
    """
    entered_data = test_utils.enter_data_to_db('application_id', 5)
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    entered_data.append(data)
    test_utils.post_message(data)
    response = test_utils.get_message({'applicationId': 1})
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == len(entered_data)


def test_get_all_messages_with_session_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/GetMessage' url is requested (GET) with the params: sessionId
    THEN status code should be 200 and te return data should be equal to the posted data
    """
    entered_data = test_utils.enter_data_to_db('session_id', 5)
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    entered_data.append(data)
    test_utils.post_message(data)
    response = test_utils.get_message({'sessionId': 'aaaa'})
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == len(entered_data)


# ***********************************************************************************************************************

def test_get_with_two_params():
    """
        GIVEN a Flask application configured for testing
        WHEN the '/DeleteMessage' url is requested (DELETE) with the params: sessionId and applicationID
        THEN delete the message with the same sessionId and applicationID and leave the one with different messageId
    """
    data_equal_seesion_and_app = test_utils.create_message_object(1, 'bbbb', 'a', ['avi aviv', 'moshe cohen'],
                                                                  'Hi, how are you today?')
    data_equal_seesion_and_app2 = test_utils.create_message_object(1, 'bbbb', 'b', ['avi aviv', 'moshe cohen'],
                                                                   'Hi, how are you today?')
    data_equal_seesion = test_utils.create_message_object(2, 'bbbb', 'c', ['avi aviv', 'moshe cohen'],
                                                          'Hi, how are you today?')
    data_equal_app = test_utils.create_message_object(1, 'aaaa', 'd', ['avi aviv', 'moshe cohen'],
                                                      'Hi, how are you today?')
    data = [data_equal_seesion_and_app, data_equal_seesion_and_app2, data_equal_app, data_equal_seesion]
    for d in data:
        test_utils.post_message(d)
    params = {'applicationId': 1, 'sessionId': 'bbbb'}
    response = test_utils.get_message(params)
    get_all_response = requests.get(test_utils.URL_SERVICE_TEST)
    test_utils.delete_message({'messageId': 'c'})
    test_utils.delete_message({'messageId': 'd'})
    assert response.status_code == HTTPStatus.OK
    assert data_equal_seesion_and_app in response.json() and data_equal_seesion_and_app2 in response.json()
    assert data_equal_app in get_all_response.json() and data_equal_seesion in get_all_response.json()
