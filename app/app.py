from flask import Flask, request
from database.api import LogRepository
from database.provider import PostgresProvider
import datetime


provider = PostgresProvider()
log_repo = LogRepository(provider)
app = Flask(__name__)


@app.route("/write", methods=['POST'])
def write_log():
    response = log_repo.create(
        data={"timestamp": datetime.datetime.now(), "type": "test_type", "message": "test_message"}
    )
    return {"response": response}


@app.route("/read", methods=['GET'])
def read_log():
    request_data = request.get_json()
    log_id = request_data['log_id']
    result = log_repo.read(log_id)
    return {"result": result}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
