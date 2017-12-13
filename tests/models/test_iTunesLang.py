"""Test for ItunesLanguages model."""
from ows_asset.models import iTunesLang
from tests.testutils import db


#test get_language_by_id
@db.test_schema
def test_get_language_by_id():
    """Test get_language_by_id."""
    expected_response = {
        'language': 'Test Language', 'language_code': 'test', 'language_id': 1}

    db.insert_itunes_languages()
    response = iTunesLang.get_language_by_id(1)

    assert response
    assert response.message == expected_response


#test get_language_by_id for no record found
@db.test_schema
def test_get_language_by_id_not_found():
    """Test get_language_by_id failure."""
    response = iTunesLang.get_language_by_id(12)
    assert not response
    assert response.errors['message'] == '12 record id not available.'


#test get_all_language
@db.test_schema
def test_get_all_language():
    """Test get_all_language."""
    expected_response = [{
        'language': 'Test Language', 'language_code': 'test', 'language_id': 1},
        {'language': 'Test Language2', 'language_code': 'test2', 'language_id': 2}]

    db.insert_itunes_alllanguages()
    response = iTunesLang.get_all_language()

    assert response
    assert response.message == expected_response


#test add_language
@db.test_schema
def test_add_language():
    """Test add_language."""
    expected_response = {
        'language': 'Test Language', 'language_code': 'test', 'language_id': None}

    response = iTunesLang.add_language('Test Language', 'test')

    assert response
    assert response.message == expected_response


#test update_language
@db.test_schema
def test_update_language():
    """Test update_language."""
    expected_response = 'Data updated!!!'

    data = {
        'language': 'Test', 'language_code': 'test1', 'language_id': 1}
    db.insert_itunes_languages()
    response = iTunesLang.update_language(data)

    assert response
    assert response.message == expected_response


#test update_language for record not found
@db.test_schema
def test_update_language_not_found():
    """Test update_language for record not found."""
    expected_response = '2 record id not found.'

    data = {
        'language': 'Test', 'language_code': 'test1', 'language_id': 2}
    db.insert_itunes_languages()
    response = iTunesLang.update_language(data)

    assert not response
    assert response.errors['message'] == expected_response


#test update_language for invalid record
@db.test_schema
def test_update_language_invalid():
    """Test update_language for invalid record."""
    expected_response = 'Invalid data sent for save language.'

    data = ['Test', 'test1', 1]
    db.insert_itunes_languages()
    response = iTunesLang.update_language(data)

    assert not response
    assert response.errors['message'] == expected_response


#test update_language for empty
@db.test_schema
def test_update_language_empty():
    """Test update_language for empty"""
    expected_response = 'Invalid data sent for save language.'

    data = {}
    db.insert_itunes_languages()
    response = iTunesLang.update_language(data)

    assert not response
    assert response.errors['message'] == expected_response


#test delete_by_id
@db.test_schema
def test_delete_by_id():
    """Test delete_by_id."""
    expected_response = {
        'language': 'Test Language', 'language_code': 'test', 'language_id': 1}

    db.insert_itunes_languages()
    response = iTunesLang.delete_by_id(1)

    assert response
    assert response.message == expected_response


#test delete_by_id for record already deleted
@db.test_schema
def test_delete_by_id_already_deleted():
    """Test delete_by_id for record already deleted."""
    expected_response = '2 record id already deleted!!!'

    db.insert_itunes_languages()
    response = iTunesLang.delete_by_id(2)

    assert not response
    assert response.errors['message'] == expected_response