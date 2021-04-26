"""
Flask app that provides a URL lookup service.  There is a single endpoint that
is described below.
"""
import os

from flask import Flask, make_response
from url_check import db, utils


def create_app():
    """
    This function creates a Flask app that compares a URL to a URL blacklist.
    If the URL is in the blacklist then it will return a `403 - Forbidden`
    response.  Otherwise it returns `204 - No content`.
    """
    app = Flask(__name__)

    # Set DATABASE configuration
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'url_check.sqlite'))

    @app.route('/urlinfo/1/<host_and_port>')
    def url_check(host_and_port):
        host, port = utils.get_host_and_port(host_and_port)
        cursor = db.get_db().cursor()
        cursor.execute(
            """
            SELECT id FROM bad_url
            WHERE host = :host AND
            port = :port AND
            path is NULL """,
            {'host': host, 'port': port})
        rows = cursor.fetchall()
        if len(rows) > 0:
            return make_response('', 403)
        return make_response('', 204)

    @app.route('/urlinfo/1/<host_and_port>/<path>')
    def url_check_with_path(
            host_and_port, path):  # pylint: disable=unused-argument
        host, port = utils.get_host_and_port(host_and_port)
        cursor = db.get_db().cursor()
        cursor.execute(
            """
            SELECT id FROM bad_url
            WHERE host = :host AND
            port = :port AND
            path = :path """,
            {'host': host, 'port': port, 'path': path})
        rows = cursor.fetchall()
        if len(rows) > 0:
            return make_response('', 403)
        return make_response('', 204)

    db.init_app(app)

    return app
