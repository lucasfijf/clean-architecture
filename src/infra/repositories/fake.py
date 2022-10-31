# pylint: disable=E1102

from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakeRepository:
    """Fake repository"""

    @classmethod
    def insert_user(cls):
        """Insert user"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Lucas", password="Rangel")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
