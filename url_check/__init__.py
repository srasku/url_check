from flask import Flask, make_response

def create_app():
    app = Flask(__name__)

    @app.route('/urlinfo/1/<host_and_port>')
    def url_check(host_and_port):
        host, port = utils.get_host_and_port(host_and_port)
        if host == 'bad-host.com':
            return make_response('', 403)
        return make_response('', 204)

    return app
