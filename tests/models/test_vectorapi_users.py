from python_crud.models import vectorapi_users
from tests.factories.vectorapi_users import VectorapiUsersFactory
from tests.testutils import db


@db.test_schema
def test_get_all_users():
    db.seed_models(VectorapiUsersFactory.build(user_id=12))
    actual_result = vectorapi_users.get_all_users(12)
    assert len(actual_result.message) == 1

