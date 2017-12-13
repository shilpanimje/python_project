"""db.py.

Database level utility class for testing against the artist_info schema.
"""

from functools import wraps
import sys

from python_crud import config
from python_crud.connectors import mysql
from python_crud.connectors.mysql import db_session
from python_crud.models.vectorapi_users import VectorapiUsers
from python_crud.models.product import Product


DROP_TABLE_VENDOR = """
DROP TABLE IF EXISTS vendor;
"""


CREATE_TABLE_VENDOR = """
CREATE TABLE `vendor` (
  `vendor_id` int(11) PRIMARY KEY,
  `name` varchar(255) NOT NULL,
  `company` varchar(255) NOT NULL);
"""


INSERT_VENDOR = """
    INSERT INTO vendor (vendor_id, name, company)
    VALUES
    (4, 'janata', 'sts');
"""


CREATE_TABLE_ITUNES_LANGUAGES = """
CREATE TABLE `itunes_film_languages` (
  `language_id` int(10) PRIMARY KEY,
  `language` TEXT DEFAULT NULL,
  `language_code` TEXT DEFAULT NULL);
"""


DROP_TABLE_ITUNES_LANGUAGES = """
DROP TABLE IF EXISTS itunes_film_languages;
"""


INSERT_ITUNES_LANGUAGES = """
    INSERT INTO itunes_film_languages (language_id, language, language_code)
    VALUES
    (1, 'Test Language', 'test');
"""


INSERT_ITUNES_ALLLANGUAGES = """
    INSERT INTO itunes_film_languages (language_id, language, language_code)
    VALUES
    (1, 'Test Language', 'test'),
    (2, 'Test Language2', 'test2');
"""

DROP_TABLE_PRODUCT = """
DROP TABLE IF EXISTS product;
"""

CREATE_TABLE_PRODUCT = """
CREATE TABLE `product` (
  `product_id` int(11) PRIMARY KEY,
  `product_name` varchar(255) NOT NULL);
"""

INSERT_PRODUCT = """
    INSERT INTO product (product_id, product_name)
    VALUES
    (4, 'itunes');
"""


def _exit_if_not_test_environment(session):
    """For safety, only run tests in test environment pointed to sqlite.

    Exit immediately if not in test environment or not pointed to sqlite.
    """
    if config.ENVIRONMENT != config.TEST_ENVIRONMENT:
        sys.exit('Environment must be set to {}.'.format(
            config.TEST_ENVIRONMENT))
    if 'sqlite' not in session.bind.url.drivername:
        sys.exit('Tests must point to sqlite database.')


def test_schema(function):
    """Create and tear down the test DB schema around a function call.

    This just creates the schema and does not seed data. Indvidual test cases
    can use factories to seed data as needed.

    Args:
        function (func): the function to be called after creating the test
        schema.

    Returns:
        Function: The decorated function.
    """
    @wraps(function)
    def call_function_within_db_context(*args, **kwargs):
        create_vectorapi_users()
        create_vendor()
        create_itunes_languages()
        create_product()

        try:
            function_return = function(*args, **kwargs)
        finally:
            drop_vectorapi_users()
            drop_vendor()
        drop_itunes_languages()
        drop_product()

        return function_return


def seed_models(models):
    """Save the given model(s) to the DB."""
    if not hasattr(models, '__iter__'):
        models = [models]

    with db_session() as session:
        _exit_if_not_test_environment(session)
        for model in models:
            session.merge(model)
        session.commit()

""" All Custom functions start here.."""


def create_vectorapi_users():
    """Create VectorapiUsers tables in testing DB."""
    VectorapiUsers.__table__.create(mysql._db_engine)


def drop_vectorapi_users():
    """Delete VectorapiUsers tables from testing DB."""
    VectorapiUsers.__table__.drop(mysql._db_engine)


def insert_vendor():
    """Insert data into vendor table."""
    with db_session() as session:
        session.execute(INSERT_VENDOR)


def drop_vendor():
    """Drop the `vendor` table."""
    with db_session() as session:
        _exit_if_not_test_environment(session)
        session.execute(DROP_TABLE_VENDOR)


def create_vendor():
    """Create the `vendor` table."""
    with db_session() as session:
        _exit_if_not_test_environment(session)
        drop_vendor()
        session.execute(CREATE_TABLE_VENDOR)


def insert_itunes_languages():
    """Insert data into itunes_languages table."""
    with db_session() as session:
        session.execute(INSERT_ITUNES_LANGUAGES)


def insert_itunes_alllanguages():
    """Insert data into itunes_languages table."""
    with db_session() as session:
        session.execute(INSERT_ITUNES_ALLLANGUAGES)


def create_itunes_languages():
    """Create the `itunes_languages` table."""
    with db_session() as session:
        _exit_if_not_test_environment(session)
        drop_itunes_languages()
        session.execute(CREATE_TABLE_ITUNES_LANGUAGES)


def drop_itunes_languages():
    """Drop the `itunes_languages` table."""
    with db_session() as session:
        _exit_if_not_test_environment(session)
        session.execute(DROP_TABLE_ITUNES_LANGUAGES)


def insert_product():
    """Insert data into product table."""
    with db_session() as session:
        session.execute(INSERT_PRODUCT)


def drop_product():
    """Drop the `product` table."""
    with db_session() as session:
        _exit_if_not_test_environment(session)
        session.execute(DROP_TABLE_PRODUCT)


def create_product():
    """Create the `product` table."""
    with db_session() as session:
        _exit_if_not_test_environment(session)
        drop_product()
        session.execute(CREATE_TABLE_PRODUCT)

