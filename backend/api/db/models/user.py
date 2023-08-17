import hashlib

from api.db.db import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER


class User(Base):
    __tablename__ = "users"
    id = Column(
        "id",
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    username = Column("username", String(256), nullable=False)
    password = Column("password", String(256), nullable=False)
    email = Column("email", String(256), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.email = email

    def __str__(self):
        return str(self.id) + ":" + self.username
