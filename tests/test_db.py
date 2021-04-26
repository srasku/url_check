"""
Tests for database access functions.
"""
import sqlite3

import pytest
from url_check.db import get_db


def test_get_close_db(app):
    """
    Tests `close_db()`.  Verifies that you cannot issue database commands
    against a closed database.
    """
    with app.app_context():
        database = get_db()
        assert database is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as err:
        database.execute('SELECT 1')

    assert 'closed' in str(err.value)


def test_init_db_command(runner, monkeypatch):
    """
    Tests init_db command.  Verifies that init-db is called.
    """
    class Recorder:  # pylint: disable=too-few-public-methods
        """ Keeps track of whether "init-db" was called """
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('url_check.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Imported' in result.output
    assert Recorder.called
