"""Product Model."""

from oto import response
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from env.Lib.sre_constants import error
from python_crud.config import DB_URL
from python_crud import config
from python_crud.connectors import mysql
from python_crud.constants import error


class Product(mysql.BaseModel):
    """

    Product Model.

    """
    __tablename__ = 'product'

    product_id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False)
    product_name = Column(String)

    def to_dict(self):
        """Return a dictionary of a product's properties."""

        return {
            'product_id': self.product_id,
            'product_name': self.product_name
        }


def get_product_by_id(product_id):
    """Get product information by product id.

    Args:
        product_id (int): unique identifier for the product (product_id).
    Returns:
        response.Response: containing dict of product or error.
    """

    with mysql.db_session() as session:
        product = session.query(Product).get(product_id)

        if not product:
            return response.create_not_found_response('product id:{} not found.'.format(product_id))

        return response.Response(message=product.to_dict())


def get_all_product():
    """Get all the products.
    Returns:
        response.Response: containing dict of product or error.
    """

    with mysql.db_session() as session:
        product = session.query(Product).all()

        if not product:
            return response.create_not_found_response()

        response_data = [each.to_dict() for each in product]

    return response.Response(message=response_data)


def add_product(data):
    """Add new product data for the given data.
    Args:
        product_name (string): product name.
        data (dict): dict containing product data.
        e.g; [{product_name : product_name}]
    Returns:
        response.Response: response object containing dict of product or error.
    """

    with mysql.db_session() as session:
        new_product = Product(product_name=data.get('product_name'))
        session.add(new_product)

    return response.Response(message='{} successfully added'.format(data))


def update_product_by_id(data):
    """Update product data for the given product_id.
    Args:
        product_id (int): id product.
        data (dict): dict containing product data.
        e.g; {product_id : product_id, product_name : product_name, ..}
        session (object): db session object, to make it transactional.
    Returns:
        response.Response: response object containing dict of product or error.
    """

    if data == {}:
        return response.create_error_response(
            error.ERROR_CODE_NOT_FOUND,
            'Invalid data sent for update product.')

    with mysql.db_session() as session:
            update_product = session.query(Product) \
                .get(data.get('product_id'))
            if not update_product:
                return response.create_not_found_response('product id:{} not found.'.format(data['product_id']))
            else:
                update_product.product_name = data.get('product_name')
                session.merge(update_product)

            return response.Response(message=update_product.to_dict())


def delete_product_by_id(data):
    """Delete product with data provided.
    Args:
        product_id (int): primary key product_id.
        data (dict): additional translations for fields.
    Returns:
        Response: A Response obj with message
    """

    with mysql.db_session() as session:
        saved_artist = session.query(Product).get(data)

        if not saved_artist:
            return response.create_not_found_response('product id:{} not found.'.format(data))

        product = saved_artist.to_dict()
        session.delete(saved_artist)
        return response.Response(message='{} successfully deleted.'.format(product))
