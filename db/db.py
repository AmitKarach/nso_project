import json
import sqlite3

from src.response_texts import INSERT_MESSAGE_ERROR

db_search_parameters = {'applicationId': 'application_id', 'sessionId': 'session_id', 'messageId': 'message_id'}


def get_connection():
    return sqlite3.connect('Messages.db')


def create_messages_table():
    conn = get_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS Messages 
        (  application_id   INT     NOT NULL, 
           session_id       TEXT    NOT NULL, 
           message_id       TEXT    NOT NULL UNIQUE, 
           participants     TEXT    NOT NULL, 
           content          TEXT    NOT NULL);''')
    conn.close()


def get_messages_by_query(query):
    cur = get_connection().cursor()
    cur.execute(query)
    r = [dict((cur.description[i][0], json.loads(value) if cur.description[i][0] == 'participants' else value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return r


def get_all_messages_from_db():
    return get_messages_by_query('SELECT * from Messages')


def get_condition_query(query_parameters, intersection_parameters):
    condition = []
    for parameter in intersection_parameters:
        if parameter == 'applicationId':
            condition.append(db_search_parameters[parameter] + '=' + query_parameters[parameter])
        else:
            condition.append(db_search_parameters[parameter] + "='" + query_parameters[parameter] + "'")

    return ' WHERE ' + ' and '.join(condition)


def get_messages_from_db(query_parameters, intersection_parameters):
    query = 'SELECT * from Messages '
    query += get_condition_query(query_parameters, intersection_parameters)
    return get_messages_by_query(query)


def insert_message(application_id, session_id, message_id, participants, content):
    conn = get_connection()
    sql = '''INSERT INTO Messages (application_id, session_id, message_id, participants, content) 
          VALUES ({}, '{}', '{}', '{}', '{}' )'''.format(
        application_id,
        session_id,
        message_id,
        participants,
        content)
    status_code = 0
    error_message = ''
    try:
        conn.execute(sql)
        conn.commit()
    except sqlite3.Error as er:
        status_code = 1
        error_message = er.args[0] if er.args[0] else INSERT_MESSAGE_ERROR
    conn.close()
    return {'status_code': status_code, 'error_message': error_message}


def delete_messages_from_db(query_parameters, intersection_parameters):
    query = 'DELETE from Messages '
    query += get_condition_query(query_parameters, intersection_parameters)
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()
