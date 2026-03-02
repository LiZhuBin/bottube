import pytest
import os
import tempfile
from bottube_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    db_fd, temp_db_path = tempfile.mkstemp()
    app.config['DATABASE'] = temp_db_path
    with app.test_client() as client:
        yield client
    os.close(db_fd)
    if os.path.exists(temp_db_path):
        os.unlink(temp_db_path)
