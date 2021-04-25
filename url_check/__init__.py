"""
Flask app that provides a URL lookup service.  There is a single endpoint that
is described below.
"""
from flask import Flask, make_response
from url_check import utils


def create_app():
    """
    This function creates a Flask app that compares a URL to a URL blacklist.
    If the URL is in the blacklist then it will return a `403 - Forbidden`
    response.  Otherwise it returns `204 - No content`.
    """
    app = Flask(__name__)

    @app.route('/urlinfo/1/<host_and_port>')
    def url_check(host_and_port):
        host, _ = utils.get_host_and_port(host_and_port)
        if host == 'bad-host.com':
            return make_response('', 403)
        return make_response('', 204)

    return app
