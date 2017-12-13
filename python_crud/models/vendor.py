"""Model Sample.

This is just a model sample. It depends on which database you want to use but
basically make sure this file only contains methods and classes that are
related to this model.
"""

from oto import response
from owsrequest import request
from pymysql import Date
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from env.Lib.sre_constants import error
from project.config import DB_URL
from project import config
from project.connectors import mysql

##class vendor##
class Vendor(mysql.BaseModel):
    """vendor model."""

    __tablename__ = 'vendor'

    vendor_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)
    company = Column(String)

    def to_dict(self):
        """return this data."""

        return {
            'vendor_id': self.vendor_id,
            'vendor_name': self.name,
            'vendor_company': self.company
        }

def get_all_vendors():
    """Get all vendor list.

    Returns:
        list of vendors.
    """
    with mysql.db_session() as session:
        vendor = session.query(Vendor).all()
        return_list = [each.to_dict() for each in vendor]
    return response.Response(return_list)

def get_vendor_by_id(vendor_id):
    """Get a vendor by its id.

    Note:
        This method will return vendor by its id.

    Args:
        vendor_id (int): vendor id.

    Returns:
        vendor data.
    """
    with mysql.db_session() as session:
        vendor_data = session.query(Vendor).get(vendor_id)

        if not vendor_data:
            return response.Response('{} record id not available.'.format(vendor_id))

        return response.Response(vendor_data.to_dict())

def save_vendor_data(vendor_data):
    """save vendor  data.

    Args:
        name(varchar), company(varchar)

    Returns:
        saved records.
    """
    with mysql.db_session() as session:
            new_vendor = Vendor(
            name=vendor_data['name'], company=vendor_data['company'])
            session.add(new_vendor)
    return response.Response(vendor_data)

def delete_vendor(id):
    """delete vendor by its id.

    Note:
        This method will delete vendor by id.

    Args:
        vendor_id (int): vendor id.

    Returns:
        delete message with record id.
    """
    with mysql.db_session() as session:
        saved_vendor = session.query(Vendor).get(id)

        if not saved_vendor:
            return response.Response('{} record id not found.'.format(id))

        session.delete(saved_vendor)

    return response.Response('{} vendor deleted successfully.'.format(id))


def update_vendor_by_id(data):
    """update vendor by its id.

    Note:
        This method will update name, company of vendor by id.

    Args:
        vendor_id (int), name(varchar), company(varchar)

    Returns:
        response.Response: update message.
    """
    if data == {}:
        return response.Response('Invalid data.')

    with mysql.db_session() as session:
        saved_vendor = session.query(Vendor) \
        .filter_by(vendor_id=data['vendor_id'])\
        .one_or_none()

        if not saved_vendor:
            return response.Response('{} record id not found.'.format(data['vendor_id']))
        else:
            saved_vendor.name = data['name']

            if data['company'] is not None:
                saved_vendor.company = data['company']

            session.merge(saved_vendor)

    return response.Response('data updated successfully')
