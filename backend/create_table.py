import os
from datetime import datetime

from api.db.db import Base, engine, session
from api.db.models.common import SQLITE3_NAME
from api.db.models.task import Task
from api.db.models.user import User

if __name__ == "__main__":
    path = SQLITE3_NAME
    if not os.path.isfile(path):
        print("Creating database...")
        Base.metadata.create_all(engine)
        print("Database created!")

    admin = User(
        username="admin",
        password="admin",
        email="hogehoge@example.com",
    )
    session.add(admin)
    session.commit()

    task = Task(
        user_id=admin.id,
        content="test",
        deadline=datetime(2023, 8, 31, 12, 00, 00),
    )
    print(task)
    session.add(task)
    session.commit()

    session.close()
