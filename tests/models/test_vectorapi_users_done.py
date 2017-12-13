"""Test for vectorapi_users_done."""
from python_crud.models import vectorapi_users_done
from tests.factories.vectorapi_users_done import VectorapiUsersFactory
from tests.testutils import db


@db.test_schema
def test_get_all_vectorapi_users():
    """Test get_all_vectorapi_users when it succeeds."""
    # db.seed_models(VectorapiUsersFactory.build())
    # or you do
    db.seed_models(VectorapiUsersFactory.build(
        api_key='test1', user_id=20, name='test1'))

    response = vectorapi_users_done.get_all_vectorapi_users()

    assert response.status == 200
    assert response.message == [{
        'api_key': 'test1',
        'user_id': 20,
        'user_name': 'test1'
    }]
    
    # or you do 
    assert 'api_key' in response.message[0]


@db.test_schema
def test_get_all_vectorapi_users_multiple():
    """Test get_all_vectorapi_users with multiple records."""
    db.seed_models(VectorapiUsersFactory.build_batch(15))

    response = vectorapi_users_done.get_all_vectorapi_users()

    assert response.status == 200
    assert len(response.message) == 15
    for each_user in response.message:
        assert 'user_id' in each_user
        assert 'api_key' in each_user
        assert 'user_name' in each_user
        assert 'api_secret' not in each_user
