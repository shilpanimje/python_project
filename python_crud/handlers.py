"""Application Handlers.

Requests are redirected to handlers, which are responsible for getting
information from the URL and passing it down to the logic layer. The way
each layer talks to each other is through Response objects which defines the
type status of the data and the data itself.

Please note: the Orchard uses the term handlers over views as convention
for clarity

See:
    oto.response for more details.
"""


from flask import g
from flask import jsonify
from flask import request

from oto import response
from oto.adaptors.flask import flaskify

from python_crud import config
from python_crud.api import app
from python_crud.logic import hello
from python_crud.logic import vectorapi_users_logic


@app.route('/', methods=['GET'])
def hello_world():
    """Hello World with an optional GET param "name"."""
    name = request.args.get('name', '')
    return flaskify(hello.say_hello(name))


@app.route('/<username>', methods=['GET'])
def hello_world_username(username):
    """Hello World on /<username>.

    Args:
        username (str): the user's username.
    """
    return flaskify(hello.say_hello(username))


@app.route(config.HEALTH_CHECK, methods=['GET'])
def health():
    """Check the health of the application."""
    return jsonify({'status': 'ok'})


@app.errorhandler(500)
def exception_handler(error):
    """Default handler when uncaught exception is raised.

    Note: Exception will also be sent to Sentry if config.SENTRY is set.

    Returns:
        flask.Response: A 500 response with JSON 'code' & 'message' payload.
    """
    message = (
        'The server encountered an internal error '
        'and was unable to complete your request.')
    g.log.exception(error)
    return flaskify(response.create_fatal_response(message))


@app.route('/vectorapi_users/<int:user_id>', methods=['GET'])
def get_vectorapi_users(user_id):
    response_obj = vectorapi_users_logic.get_vectorapi_user_by_id(user_id)
    return flaskify(response_obj)


@app.route('/vectorapi_users', methods=['POST'])
def create_vectorapi_users():
    response_obj = vectorapi_users_logic.create_user(request.get_json())
    return flaskify(response_obj)


@app.route('/vectorapi_users/<int:user_id>', methods=['PUT'])
def update_vectorapi_users(user_id):
    localize_data = vectorapi_users_logic.update_user(
        user_id, request.get_json())

    return flaskify(localize_data)
