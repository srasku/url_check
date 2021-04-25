"""
Database module to access SQLite3 database.
"""

import os
import sqlite3
import click

from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """
    Get connection to the database.  Connection is cached for subsequent use.
    """
    if 'db' not in g:
        db_file = current_app.config['DATABASE']
        print(db_file)
        try:
            # Create parent directory if it doesn't exist.  If it exists it
            # ignores the resulting FileExistsError.
            db_dir = os.path.dirname(db_file)
            os.mkdir(db_dir)
        except FileExistsError:
            pass
        g.db = sqlite3.connect(
            db_file,
            detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(_=None):
    """
    Close the connection to the database.
    """
    database = g.pop('db', None)

    if database is not None:
        database.close()


def init_db():
    """
    Initializes database using `schema.sql`.
    """
    database = get_db()

    with current_app.open_resource('schema.sql') as schema_file:
        database.executescript(schema_file.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Command to initialize database.  To use from command line, type
        `flask init-db`.
    """
    init_db()
    click.echo('Imported schema')


def init_app(app):
    """
    Register database functions with the Flask app.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
