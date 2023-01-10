import requests

from src.config import HOST, PORT

URL_SERVICE_TEST = 'http://{}:{}'.format(HOST, PORT)


def delete_message(params):
    return requests.delete(URL_SERVICE_TEST + '/DeleteMessage', params=params)


def get_message(params):
    return requests.get(URL_SERVICE_TEST + '/GetMessage', params=params)


def post_message(data):
    return requests.post(URL_SERVICE_TEST + '/AddMessage', json=data)


def create_message_object(application_id=None, session_id=None, message_id=None, participants=None, content=None):
    return {
        'application_id': application_id,
        'session_id': session_id,
        'message_id': message_id,
        'participants': participants,
        'content': content
    }


def enter_data_to_db(key, how_many):
    """enters a large number of data (the size of how_many) where all the params are different except for key
    """
    entered_data = []
    data = create_message_object(1, 'aaaa', 'bbbb', ['avi aviv', 'moshe cohen'], 'Hi, how are you today?')

    post_message(data)
    for i in range(how_many):
        for val in data:
            if val == 'participants' or val == 'content':
                break
            elif val != key:
                data[val] = data[val] + type(data[val])(i + 1)
        entered_data.append(data)
        post_message(data)
    return entered_data
