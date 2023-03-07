from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base


class PostgresProvider:
    """Class for connection with database"""
    def __init__(self):
        database_url = "postgresql://postgres:postgres@localhost/test"
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        self.db_session = sessionmaker(bind=self.engine)
        self.session = self.db_session()

    def get_session(self):
        """Returns session"""
        return self.session
