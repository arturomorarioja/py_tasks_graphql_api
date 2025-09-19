from flask import Blueprint, request, jsonify
from ..schema import schema


tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')


@tasks_bp.post('')
def graphql_tasks():
    # Parse incoming JSON body
    payload = request.get_json(silent=True) or {}
    query = payload.get('query')
    variables = payload.get('variables')
    operation_name = payload.get('operationName')

    if not query:
        return jsonify({'errors': [{'message': 'No GraphQL query provided'}]}), 400

    # Execute GraphQL query using Graphene
    result = schema.execute(query, variable_values=variables, operation_name=operation_name)

    response = {}
    if result.errors:
        response['errors'] = [{'message': str(e)} for e in result.errors]
    if result.data is not None:
        response['data'] = result.data

    return jsonify(response), 200