from oto import response
from sqlalchemy import Column
from sqlalchemy import update
from sqlalchemy import Integer
from sqlalchemy import String
from ows_asset.constants import error
from ows_asset.config import DB_URL
from ows_asset import config
from ows_asset.connectors import mysql
import os


class ItunesLanguages(mysql.BaseModel):
    """ItunesLanguages Model.
    Represents vw_product view in animal.
    """

    __tablename__ = 'itunes_film_languages'

    language_id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False)
    language = Column(String)
    language_code = Column(String)

    def to_dict(self):
        """Return a dictionary of a product's properties."""

        return {
            'language_id': self.language_id,
            'language': self.language,
            'language_code' : self.language_code
        }


def get_all_language():
    """Get all languages.
    """
    with mysql.db_session() as session:
        ItunesLanguage = session.query(ItunesLanguages).all()
        returnlist = [each.to_dict() for each in ItunesLanguage]
        return response.Response(message=returnlist)


def get_language_by_id(language_id):
    """Get language information by language id.
    Args:
        language_id (int): unique identifier for the language (language_id).
    Returns:
        response.Response: containing dict of product or error.
    """
    with mysql.db_session() as session:
        ItunesLanguage = session.query(ItunesLanguages).get(language_id)

        if not ItunesLanguage:
            return response.create_error_response(
                error.ERROR_CODE_NOT_FOUND,
                '{} record id not available.'.format(language_id))

        return response.Response(message=ItunesLanguage.to_dict())


def add_language(language_name, language_codename):
    """Add language information .
    Args:
        language (str): the language.
        language_code (str): the language_code.
    Returns:
        response.Response: containing dict of product or error.
    """
    with mysql.db_session() as session:
        ItunesLanguage = ItunesLanguages(language = language_name, language_code = language_codename)
        session.add(ItunesLanguage)

        return response.Response(message=ItunesLanguage.to_dict())


def update_language(data):
    """Update language information .
    Args:
        id (int): unique identifier for the language (language_id).
        data (str): dictionary record contain language_name and language_code
    Returns:
        response.Response: message or error.
    """
    if not isinstance(data, dict) or not data:
        return response.create_error_response(
            error.ERROR_CODE_NOT_FOUND,
            'Invalid data sent for save language.')

    with mysql.db_session() as session:
            update_language = session.query(ItunesLanguages) \
                .get(data.get('language_id'))
            if not update_language:
                return response.create_error_response(
                error.ERROR_CODE_NOT_FOUND,
                '{} record id not found.'.format(data['language_id']))
            else:
                update_language.language = data.get('language_name')
                update_language.language_code= data.get('language_code')
                session.merge(update_language)

    return response.Response(message='Data updated!!!')


def delete_by_id(language_id):
    """Delete language information by product id.
    Args:
        language_id (int): unique identifier for the language (language_id).
    Returns:
        response.Response: containing dict of product or error.
    """
    with mysql.db_session() as session:
        ItunesLanguage = session.query(ItunesLanguages).get(language_id)

        if not ItunesLanguage:
            return response.create_error_response(
                error.ERROR_CODE_NOT_FOUND,
                '{} record id already deleted!!!'.format(language_id))

        session.delete(ItunesLanguage)

        return response.Response(message=ItunesLanguage.to_dict())



