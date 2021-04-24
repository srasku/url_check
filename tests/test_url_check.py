import pytest


def test_url_check(client):
    response = client.get('urlinfo/1/localhost:99')
    assert response.data == b'Host: localhost, port: 99'
