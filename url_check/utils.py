"""
Returns tuple representing host and port based on the provided `param`.
The format of this string is expected to be `host:port`.  For example,
a valid string would be 'www.some-domain.com:8080'.  If the port is
omitted, it is assumed to be 80.
"""


def get_host_and_port(param):
    tuple = param.split(':')
    host = tuple[0]
    port = int(tuple[1]) if len(tuple) > 1 else 80

    return host, port
