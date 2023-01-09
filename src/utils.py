import numbers


def message_is_valid(message):
    application_id = message.get('application_id', None)
    session_id = message.get('session_id', None)
    message_id = message.get('message_id', None)
    participants = message.get('participants', None)
    content = message.get('content', None)
    return application_id and isinstance(application_id, numbers.Number) and \
        session_id and isinstance(session_id, str) and \
        message_id and isinstance(message_id, str) and \
        participants and isinstance(participants, list) and \
        content and isinstance(content, str)
