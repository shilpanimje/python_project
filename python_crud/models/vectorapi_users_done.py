"""something."""
from oto import response
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from python_crud.connectors import mysql


class VectorapiUsers(mysql.BaseModel):
    __tablename__ = 'vectorapi_user_old'

    user_ = Column(
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


def get_all_vectorapi_users():
    with mysql.db_session() as session:
        result = session.query(VectorapiUsers).all()

        response_date = [user.to_dict() for user in result]
        return response.Response(message=response_date)


def insert_user(data):
    with mysql.db_session() as session:
        new_user = VectorapiUsers()
        new_user.name = data.get('user_name', 'demo')
        new_user.api_key = data.get('api_key')
        new_user.api_secret = data.get('api_secret', 'secret')

        session.add(new_user)
        session.flush()  # only if you need the new id
        return response.Response(message=new_user.to_dict())
