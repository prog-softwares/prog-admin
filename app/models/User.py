from sqlalchemy.inspection import inspect
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import Integer, String, SmallInteger

from . import db


class User(db.Model):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=False)
    email = Column(String(150), nullable=False, unique=True)
    phone = Column(String(15), nullable=True, unique=False)
    mobile = Column(String(15), nullable=True, unique=False)
    salt = Column(String(35), nullable=False, unique=False)
    password = Column(String(150), nullable=False, unique=False)
    prefix = Column(String(60), nullable=True, unique=False)
    status = Column(SmallInteger, nullable=False, unique=False, default=1)

    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
