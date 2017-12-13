import pytest

from oto import response

from python_crud.models import vectorapi_users
from python_crud.logic import vectorapi_users_logic


def test_get_vectorapi_user_by_id_success(fixture_all_users, mocker):
    """Test response contents upon success."""
    mocker.patch.object(
        vectorapi_users, 'get_all_users',
        return_value=response.Response(message=fixture_all_users))

    result = vectorapi_users_logic.get_vectorapi_user_by_id(123)
    assert result
    assert 'items' in result.message
    assert result.message == fixture_all_users


@pytest.fixture
def fixture_all_users():
    return {
        'pagination': {
            'type': 'none',
            'total_records': 2
        },
        'items': [
            {
                'user_id': 1,
                'name': 'Aaa'
            },
            {
                'user_id': 2,
                'name': 'Arabic'
            },
        ]
    }
