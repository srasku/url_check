"""
Test endpoints of URL lookup service
"""


def test_url_check(client):
    """
    Test blacklist endpoint `urlinfo/1/<host>:<port>`
    """
    response = client.get('urlinfo/1/localhost:99')
    assert response.status_code == 204
    assert response.data == b''

    response = client.get('urlinfo/1/bad-host.com:8899')
    assert response.status_code == 403
    assert response.data == b''
