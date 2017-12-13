"""Test for vendor model."""

from python_crud.models import vendor
from tests.testutils import db


@db.test_schema
def test_get_all_vendors():
    """Test get all vendors."""
    expected_response = [{'vendor_id': 4, 'vendor_name': 'janata', 'vendor_company': 'sts'}]

    db.insert_vendor()
    response = vendor.get_all_vendors()

    assert response
    assert response.message == expected_response


@db.test_schema
def test_get_vendor_by_id():
    """Test get_vendor_by_id."""
    expected_response = {'vendor_id': 4, 'vendor_name': 'janata', 'vendor_company': 'sts'}

    db.insert_vendor()
    response = vendor.get_vendor_by_id(4)

    assert response
    assert response.message == expected_response


@db.test_schema
def test_get_vendor_by_id_not_available():
    """Test get vendor by id not found."""
    expected_response = "14 record id not available."

    response = vendor.get_vendor_by_id(14)

    assert response
    assert response.message == expected_response


@db.test_schema
def test_save_vendor_data():
    """Test save vendor data."""

    expected_response = {'name': 'shilpa', 'company': 'sts'}

    db.insert_vendor()
    response = vendor.save_vendor_data(expected_response)

    assert response
    assert response.message == expected_response


@db.test_schema
def test_delete_vendor():
    """Test delete_vendor."""

    expected_response = "4 vendor deleted successfully."

    db.insert_vendor()
    response = vendor.delete_vendor(4)

    assert response
    assert response.message == expected_response


@db.test_schema
def test_delete_vendor_failed():
    """Test delete_vendor failed."""

    expected_response = "4 record id not found."

    response = vendor.delete_vendor(4)

    assert response
    assert response.message == expected_response

@db.test_schema
def test_update_vendor_by_id_invalid_data():
    """Test update vendor for blanck data."""

    expected_response = "Invalid data."

    data = {}
    response = vendor.update_vendor_by_id(data)

    assert response
    assert response.message == expected_response


@db.test_schema
def test_update_vendor_by_id_not_found():
    """Test update vendor for invalid id."""

    expected_response = "1 record id not found."

    data = {'vendor_id':1,'name':'shilpa','company':'sts'}
    response = vendor.update_vendor_by_id(data)

    assert response
    assert response.message == expected_response


@db.test_schema
def test_update_vendor_by_id():
    """Test update vendor for invalid id."""

    expected_response = "data updated successfully"

    data = {'vendor_id':4,'name':'janata','company':'sts'}
    db.insert_vendor()
    response = vendor.update_vendor_by_id(data)

    assert response
    assert response.message == expected_response

