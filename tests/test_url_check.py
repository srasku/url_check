"""
Test endpoints of URL lookup service
"""


def test_url_check(client):
    """
    Test blacklist endpoint `urlinfo/1/<host>:<port>/<path>`
    """
    url_check_tester(client, 'urlinfo/1/localhost:99', 204)
    url_check_tester(client, 'urlinfo/1/bad-host.com:8899', 403)
    url_check_tester(
        client,
        'urlinfo/1/grey-host.com:8231/free-mony.html',
        403)
    url_check_tester(
        client,
        'urlinfo/1/grey-host.com:8232/free-mony.html',
        204)
    url_check_tester(client, 'urlinfo/1/grey-host.com/free-mony.html', 204)


def url_check_tester(client, url, status_code):
    """
    Helper function to test blacklist endpoint.  This reduces the ammount of
    code duplicated for each individual test above.
    """
    response = client.get(url)
    assert response.status_code == status_code, \
        f'Unexpected status code for {url}'
    assert response.data == b''
