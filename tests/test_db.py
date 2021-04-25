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
