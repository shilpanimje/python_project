from python_crud.models import vectorapi_users


def get_vectorapi_user_by_id(user_id):
    user_obj = vectorapi_users.get_all_users(user_id)
    return user_obj


def create_user(data):
    return vectorapi_users.insert_users(data)


def update_user(user_id, data):
    return vectorapi_users.update_users(user_id, data)
