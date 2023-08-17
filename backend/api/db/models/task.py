from datetime import datetime

from api.db.db import Base
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.mysql import BOOLEAN, INTEGER
from sqlalchemy.sql.functions import current_timestamp


class Task(Base):
    __tablename__ = "tasks"
    id = Column(
        "id",
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    user_id = Column("user_id", ForeignKey("users.id"), nullable=False)
    content = Column("content", String(256), nullable=False)
    deadline = Column(
        "deadline",
        DateTime,
        default=datetime.now(),
        nullable=False,
        server_default=current_timestamp(),
    )
    date = Column(
        "date",
        DateTime,
        default=datetime.now(),
        nullable=False,
        server_default=current_timestamp(),
    )
    done = Column("done", BOOLEAN, default=False, nullable=False)

    def __init__(
        self, user_id: int, content: str, deadline: datetime, date=datetime.now()
    ):
        self.user_id = user_id
        self.content = content
        self.deadline = deadline
        self.date = date
        self.done = False

    def __str__(self):
        return (
            str(self.id)
            + ": user_id -> "
            + str(self.user_id)
            + ", content -> "
            + self.content
            + ", deadline -> "
            + self.deadline.strftime("%Y/%m/%d - %H:%M:%S")
            + ", date -> "
            + self.date.strftime("%Y/%m/%d - %H:%M:%S")
            + ", done -> "
            + str(self.done)
        )
