"""Logic for Hello.

Hello World is one of the most complex operations in the world. It requires all
the robots and nanotechnology from Terminator to define whether or not our
future will survive an apocalypse.

In other words: always make sure that whenever you add a description it's
something meaningful that you will enjoy reading days, months, or years later.
One more thing: you will automatically be associated with those, and some of us
really enjoy “git blame”.
"""

from oto import response
from python_crud.models import vectorapi_users_done
from python_crud.models import vectorapi_users


def say_hello(name=None):
    """Logic handlers.

    Args:
        name (str): the name to display alongside the Hello.

    Returns:
        Response: the hello message.
    """
    # if not name or isinstance(name, str) and not name.strip():
    #     return response.Response('Hello')
    #
    # return response.Response('Hello {}!'.format(name))

    # for model testing without logic or handler

    # return vectorapi_users_done.get_all_vectorapi_users()

    # data = {'user_name': 'test1', 'api_key': 'test1', 'api_secret': 'test1'}
    # return vectorapi_users_done.insert_user(data)

    # result = vectorapi_users.get_all_users(17)
    data = {'name': 'test now again', 'api_key': 'test1', 'api_secret':
        'test1'}
    result = vectorapi_users.insert_users(data)
    return result
