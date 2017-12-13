"""Test Cases for Test model."""
from python_crud.models import testmodel
from tests.testutils import db


@db.test_schema
def test_get_by_id():
    """Test for the specified test_id is returned."""
    expected_response = {
        'id': 100, 'name': 'test1'}

    db.insert_test_data()
    response = testmodel.get_by_id(100)

    assert response.status == 200
    assert response.message == expected_response


@db.test_schema
def test_get_by_id_not_found():
    """Test for the specified test_id not found."""
    response = testmodel.get_by_id(103)
    assert response.message == '103 test id not available.'


@db.test_schema
def test_get_all_tests():
    """Test get_all_tests."""
    expected_response = [
        {'id': 100, 'name': 'test1'},
        {'id': 101, 'name': 'test2'}]

    db.insert_test_alldata()
    response = testmodel.get_all_tests()

    assert response.status == 200
    assert response.message == expected_response


@db.test_schema
def test_get_all_tests_not_found():
    """Test get all tests not found."""
    response = testmodel.get_all_tests()
    assert response.message == 'test data not available.'


@db.test_schema
def test_add_test_data():
    """Test add_test_data."""
    expected_response = {
        'id': None, 'name': 'test2'}

    response = testmodel.add_test_data('test2')

    assert response.status == 200
    assert response.message == expected_response


@db.test_schema
def test_add_test_data_valid_data():
    """Test get all tests not found."""
    data = {}
    response = testmodel.add_test_data(data)
    assert response.message == 'data is invalid.'


@db.test_schema
def test_update_test_data():
    """Test update_test_data."""
    expected_response = {
        'id': 100, 'name': 'test2'}

    data = {
        'id': 100, 'name': 'test2'}
    db.insert_test_data()
    response = testmodel.update_test_data(data)

    assert response.status == 200
    assert response.message == expected_response


@db.test_schema
def test_update_test_data_valid_data():
    """Test for valid data not found."""
    data = {}
    response = testmodel.update_test_data(data)
    assert response.message == 'Invalid data.'


@db.test_schema
def test_update_test_data_not_found():
    """Test for specified test_id not found."""
    data = {'id': 103, 'name': 'test3'}
    response = testmodel.update_test_data(data)
    assert response.message == '103 test id not found.'


@db.test_schema
def test_delete_test_data():
    """Test delete_test_data."""
    expected_response = '100 test deleted successfully.'

    db.insert_test_data()
    response = testmodel.delete_test_data(100)

    assert response.status == 200
    assert response.message == expected_response


@db.test_schema
def test_delete_test_data_not_found():
    """Test for the specified test_id not found."""
    response = testmodel.delete_test_data(103)
    assert response.message == '103 record id not found.'
