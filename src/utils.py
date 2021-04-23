"""
Returns tuple representing host and port based on the provided `param`.
The format of this string is expected to be `host:port`.  For example,
a valid string would be 'www.some-domain.com:8080'.
"""
def get_host_and_port(param):
    host, port = param.split(':')
    port = int(port)

    return host, port
