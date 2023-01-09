import numbers


def message_is_valid(message):
    application_id = message['application_id']
    session_id = message['session_id']
    message_id = message['message_id']
    participants = message['participants']
    content = message['content']
    return application_id and isinstance(application_id, numbers.Number) and \
        session_id and isinstance(session_id, str) and \
        message_id and isinstance(message_id, str) and \
        participants and isinstance(participants, list) and \
        content and isinstance(content, str)
