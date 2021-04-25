"""
Helper functions used by url_check module.
"""


def get_host_and_port(param):
    """
    Returns tuple representing host and port based on the provided `param`.
    The format of this string is expected to be `host:port`.  For example,
    a valid string would be 'www.some-domain.com:8080'.  If the port is
    omitted, it is assumed to be 80.
    """
    values = param.split(':')
    host = values[0]
    port = int(values[1]) if len(values) > 1 else 80

    return host, port
