from provider import PostgresProvider
from models import Log


class LogRepository:
    """This class declares set of CRUD methods for 'Log' table"""

    def __init__(self, provider: PostgresProvider):
        self.session = provider.get_session()

    def create(self, data: dict):
        """Adds new record to table"""
        new_log = Log(timestamp=data['timestamp'], type=data['type'], message=data['message'])
        self.session.add(new_log)
        self.session.commit()
        return "success"

    def read(self, log_id: int):
        """Gets record from table using log id"""
        log = self.session.query(Log).filter_by(id=log_id).one()
        output_data = {"id": log.id, "timestamp": log.timestamp, "type": log.type, "message": log.message}
        return output_data

    def update(self, log_id: int, data: dict):
        """Updates record in table"""
        log = self.session.query(Log).filter_by(id=log_id).one()
        log.timestamp = data['timestamp']
        log.type = data['type']
        log.message = data['message']
        self.session.commit()

        return "success"

    def delete(self, log_id: int):
        """Deletes record from table"""
        log = self.session.query(Log).filter_by(id=log_id).one()
        self.session.delete(log)
        self.session.commit()

        return "success"
