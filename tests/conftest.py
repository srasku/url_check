"""
Test configuration
"""
import os
import tempfile

import pytest

from url_check import create_app
from url_check.db import get_db, init_db

with open(
        os.path.join(
            os.path.dirname(__file__), 'data.sql'), 'rb') as data_file:
    data_sql = data_file.read().decode('utf8')


@pytest.fixture
def app():
    """
    Fixture to create app to connect to.
    """
    db_fd, db_path = tempfile.mkstemp()
    the_app = create_app()

    with the_app.app_context():
        init_db()
        get_db().executescript(data_sql)

    yield the_app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):  # pylint: disable=redefined-outer-name
    """
    Fixture to create client for tests
    """
    return app.test_client()


@pytest.fixture
def runner(app):  # pylint: disable=redefined-outer-name
    """
    Test runner for the app's Click commands.
    This allows us to run the `init-db` command from tests.
    """
    return app.test_cli_runner()
