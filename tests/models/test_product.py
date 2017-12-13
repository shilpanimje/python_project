"""Test for vendor model."""
from python_crud.models import product
from tests.testutils import db


# test get all product
@db.test_schema
def test_get_all_products():
    """Test get all products."""
    expected_response = [{'product_id': 4, 'product_name': 'itunes'}]
    db.insert_product()

    response = product.get_all_product()
    assert response
    assert response.message == expected_response


# test get product by id
@db.test_schema
def test_get_product_by_id():
    """Test get_product_by_id."""
    expected_response = {'product_id': 4, 'product_name': 'itunes'}
    db.insert_product()

    response = product.get_product_by_id(4)
    assert response
    assert response.message == expected_response


# test get product by id not found
@db.test_schema
def test_get_product_by_id_not_found():
    """Test get product by id not found."""
    expected_response = "product id:20 not found."

    response = product.get_product_by_id(20)
    assert not response
    assert response.errors['message'] == expected_response


# test update product by id invalid data
@db.test_schema
def test_update_product_by_id_invalid_data():
    """Test update product for blanck data."""
    expected_response = "Invalid data sent for update product."
    data = {}

    response = product.update_product_by_id(data)
    assert not response
    assert response.errors['message'] == expected_response


# test update product by id not found
@db.test_schema
def test_update_product_by_id_not_found():
    """Test get product by id not found."""
    expected_response = "product id:20 not found."
    data = {'product_id': 20, 'product_name': 'playstation'}

    response = product.update_product_by_id(data)
    assert not response
    assert response.errors['message'] == expected_response


# test update product by id
@db.test_schema
def test_update_product_by_id():
    """Test update product for invalid id."""
    expected_response = {'product_id': 4, 'product_name': 'playstation'}
    db.insert_product()

    response = product.update_product_by_id(expected_response)
    assert response
    assert response.message == expected_response


# test add new product data
@db.test_schema
def test_save_product_data():
    """Test save product data."""
    expected_response = "{'product_name': 'amazon'} successfully added"
    data = {'product_name': 'amazon'}
    db.insert_product()

    response = product.add_product(data)
    assert response
    assert response.message == expected_response


# test delete product
@db.test_schema
def test_delete_product():
    """Test delete_product."""
    expected_response = "{'product_id': 4, 'product_name': 'itunes'} successfully deleted."
    db.insert_product()

    response = product.delete_product_by_id(4)
    assert response
    assert response.message == expected_response


# test delete product by id not found
@db.test_schema
def test_delete_product_failed():
    """Test delete_product failed."""
    expected_response = "product id:20 not found."

    response = product.delete_product_by_id(20)
    assert not response
    assert response.errors['message'] == expected_response