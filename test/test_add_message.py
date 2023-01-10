from http import HTTPStatus

import requests

import test_utils




def test_add_message_with_currect_data():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with all the right parameters
    THEN add the message to the DB
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    response = test_utils.post_message(data)
    assert response.status_code == 201

def test_add_messages_with_currect_data():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with all the right parameters
    THEN add the message to the DB
    """
    data = test_utils.enter_data_to_db('',10)
    for d in data:
        response = test_utils.get_message({'messageId' :d['message_id']})
        assert response.status_code == 200
# **********************************************************************************************************************
# invalid data:


def test_add_message_with_invalid_application_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with invalid application_id
    THEN return status code 400
    """
    data = test_utils.create_message_object('invalid', 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    response = test_utils.post_message(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_add_message_with_invalid_session_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with invalid session_id
    THEN return status code 400
    """
    data = test_utils.create_message_object(1, 1231, 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    response = test_utils.post_message(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_add_message_with_invalid_message_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with invalid message_id
    THEN return status code 400
    """
    data = test_utils.create_message_object(1, 'aaaa', 123, ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    response = test_utils.post_message(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_add_message_with_invalid_participants():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with invalid participants
    THEN return status code 400
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', 123, 'Hi, how are you today?')
    response = test_utils.post_message(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_add_message_with_invalid_content():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with invalid content
    THEN return status code 400
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 1323)
    response = test_utils.post_message(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


# **********************************************************************************************************************
# missing data:

def test_add_message_with_missing_application_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with missing application_id
    THEN return status code 400
    """
    data = test_utils.create_message_object('aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    response = test_utils.post_message(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_add_message_with_missing_session_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with missing session_id
    THEN return status code 400
    """
    data = test_utils.create_message_object(1, 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    response = test_utils.post_message(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_add_message_with_missing_message_id():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with missing message_id
    THEN return status code 400
    """
    data = test_utils.create_message_object(1, 'aaaa', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')
    response = test_utils.post_message(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_add_message_with_missing_participants():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with missing participants
    THEN return status code 400
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', 'Hi, how are you today?')
    response = test_utils.post_message(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_add_message_with_missing_content():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/AddMessage' url is requested (POST) with the body containing a message with missing content
    THEN return status code 400
    """
    data = test_utils.create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'])
    response = test_utils.post_message(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
