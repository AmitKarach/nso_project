import json
import response_texts
import config
from flask import Flask, request
from http import HTTPStatus
from db.db import create_messages_table, insert_message, get_all_messages_from_db, get_messages_from_db, \
    db_search_parameters, delete_messages_from_db
from src.utils import message_is_valid

app = Flask('Messages Manager App')

create_messages_table()


@app.route('/', methods=['GET'])
def get_all_messages():
    return json.dumps(get_all_messages_from_db())


@app.route('/GetMessage', methods=['GET'])
def get_messages():
    args = request.args
    args_as_set = set(args)
    intersection_args = args_as_set.intersection(db_search_parameters)

    if len(intersection_args) == 0:
        return response_texts.QUERY_PARAMETER_NAME_WAS_NOT_FOUND, HTTPStatus.BAD_REQUEST

    query_result = get_messages_from_db(args, intersection_args)

    if len(query_result) == 0:
        return '', HTTPStatus.NOT_FOUND

    return json.dumps(query_result)


@app.route('/AddMessage', methods=['POST'])
def add_message():
    body_data = request.get_json()
    if len(body_data) <5:
        return response_texts.CHECK_YOUR_PARAMETERS, HTTPStatus.BAD_REQUEST
    if not message_is_valid(body_data):
        return response_texts.CHECK_YOUR_PARAMETERS, HTTPStatus.BAD_REQUEST
    response = insert_message(
        body_data['application_id'],
        body_data['session_id'],
        body_data['message_id'],
        json.dumps(body_data['participants']),
        body_data['content'])
    if response.get('status_code') == 0:
        return {'status': 'success'}, HTTPStatus.CREATED
    return response.get('error_message'), HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/DeleteMessage', methods=['DELETE'])
def delete_messages():
    args = request.args
    args_as_set = set(args)
    intersection_args = args_as_set.intersection(db_search_parameters)

    if len(intersection_args) == 0:
        return response_texts.QUERY_PARAMETER_NAME_WAS_NOT_FOUND, HTTPStatus.BAD_REQUEST

    query_result = get_messages_from_db(args, intersection_args)

    if len(query_result) == 0:
        return '', HTTPStatus.NOT_FOUND

    delete_messages_from_db(args, intersection_args)
    return '', HTTPStatus.OK


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
