from oto import response
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from python_crud.connectors import mysql
from python_crud.connectors.mysql import db_session


class VectorapiUsers(mysql.BaseModel):
    __tablename__ = 'vectorapi_user'

    user_id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(255), nullable=False)
    api_key = Column(String, default='hello')
    api_secret = Column(String)

    # deletions = Column(Enum('Y', 'N'))

    def to_dict(self):
        """Get dict representation of this object."""
        return {
            'user_id': self.user_id,
            'user_name': self.name,
            'api_key': self.api_key
        }


def get_all_users(user_id):

    with db_session() as sesion:
        result = sesion.query(VectorapiUsers) \
            .filter(VectorapiUsers.user_id == user_id)\
            .all()

        if not result:
            return response.create_not_found_response('No user found.')

        dict_result = [user.to_dict() for user in result]

        return response.Response(message=dict_result)


def insert_users(data):

    with db_session() as session:
        user1 = VectorapiUsers()
        user1.name = data.get('name')
        user1.api_key = data.get('api_key')
        user1.api_secret = data.get('api_secret')
        session.add(user1)
        session.flush()
        return response.Response(message=user1.to_dict())


def update_users(user_id, data):

    with db_session() as session:
        existing_user = session.query(VectorapiUsers).get(user_id)
        
        if not existing_user:
            return response.create_not_found_response('No user found.')
            
        existing_user.name = data.get('name')
        existing_user.api_key = data.get('api_key')
        existing_user.api_secret = data.get('api_secret')
        session.merge(existing_user)
        session.flush()
        return response.Response(message=existing_user.to_dict())

