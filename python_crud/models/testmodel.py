"""Model Sample.

This is just a model sample. It depends on which database you want to use but
basically make sure this file only contains methods and classes that are
related to this model.
"""

from oto import response
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from python_crud.connectors import mysql


class Test(mysql.BaseModel):
    """Test Model.

    Represents python_test_omkar CRUD opearation.

    """

    __tablename__ = 'python_test_omkar'

    test_id = Column(
        'id', Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)

    def to_dict(self):
        """to_dict Method.

        Represents to_dict method to convert object into dictionary.

        """
        return {
            'id': self.test_id,
            'name': self.name
        }


def get_by_id(tid):
    """Get a test by its id.

    Note:
        This method will return test by its id.

    Args:
        tid (int): test id.

    Returns:
        test data.
    """
    with mysql.db_session() as session:
        test_data = session.query(Test).get(tid)

        if not test_data:
            return response.Response('{} test id not available.'.format(tid))

        return response.Response(test_data.to_dict())


def get_all_tests():
    """Get all test list.

    Returns:
        list of tests.
    """
    with mysql.db_session() as session:
        result_set = session.query(Test).all()

        if not result_set:
            return response.Response('test data not available.')

        total_records = [r.to_dict() for r in result_set]
        return response.Response(message=total_records)


def add_test_data(data):
    """Add test data.

    Args:
        data contains: name(varchar)

    Returns:
        saved records.
    """
    # validate data sent are valid or non empty (this is optional case).
    if not data:
        return response.Response('data is invalid.')

    with mysql.db_session() as session:
        new_test = Test(name=data)
        session.add(new_test)

        return response.Response(new_test.to_dict())


def delete_test_data(tid):
    """Delete test by its id.

    Note:
        This method will delete test by id.

    Args:
        tid (int): test id.

    Returns:
        delete message with test id.
    """
    with mysql.db_session() as session:
        delete_test = session.query(Test).get(tid)

        if not delete_test:
            return response.Response('{} record id not found.'.format(tid))

        session.delete(delete_test)

    return response.Response('{} test deleted successfully.'.format(tid))


def update_test_data(data):
    """Update test by its id.

    Note:
        This method will update name of test by id.

    Args:
        data contains: id (int), name(varchar)

    Returns:
        response.Response: update message.
    """
    if data == {}:
        return response.Response('Invalid data.')

    with mysql.db_session() as session:
        update_test = session.query(Test) \
            .filter_by(test_id=data['id']) \
            .one_or_none()

        if not update_test:
            return response.Response(
                '{} test id not found.'.format(data['id']))
        else:
            update_test.name = data['name']

            session.merge(update_test)

        return response.Response(message=update_test.to_dict())
