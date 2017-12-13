"""Tests for Handlers."""

import json
from unittest.mock import MagicMock
from unittest.mock import patch
from pytest_mock import mocker

from oto import response

import application
from python_crud import handlers
from python_crud.logic import vectorapi_users_logic


@patch('python_crud.handlers.g')
def test_exception_handler(mock_g):
    """Verify exception_Handler returns 500 status code and json payload."""
    message = (
        'The server encountered an internal error '
        'and was unable to complete your request.')
    mock_error = MagicMock()
    server_response = handlers.exception_handler(mock_error)
    mock_g.log.exception.assert_called_with(mock_error)

    # assert status code is 500
    assert server_response.status_code == 500

    # assert json payload
    response_message = json.loads(server_response.data.decode())
    assert response_message['message'] == message
    assert response_message['code'] == response.error.ERROR_CODE_INTERNAL_ERROR


def test_create_vectorapi_users(mocker):
    data = {"name": "new name 1", "api_key": "new key 1", "api_secret": "new secret 1"}
    mocker.patch.object(
        vectorapi_users_logic, 'create_user',
        return_value=response.Response(message='success'))

    with application.app.test_request_context(
            data=json.dumps(data),
            content_type='application/json'):
        handler_response = handlers.create_vectorapi_users()

        assert handler_response.status_code == 200
        vectorapi_users_logic.create_user.assert_called_once_with(data)

