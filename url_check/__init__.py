from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/urlinfo/1/<host_and_port>')
    def url_check(host_and_port):
        host, port = utils.get_host_and_port(host_and_port)
        return "Host: %s, port: %i" % (host, port)

    return app
