import unittest

from url_check import utils

class TestGetHostAndPort(unittest.TestCase):
    def test_valid_case(self):
        self.host_port_tester('www.some-domain.com:8129', 'www.some-domain.com', 8129)
        self.host_port_tester('www.another-domain.com', 'www.another-domain.com', 80)
        self.host_port_tester('host-only:8912', 'host-only', 8912)

    def host_port_tester(self, param, expected_domain, expected_port):
        tuple = utils.get_host_and_port(param)
        self.assertEqual(len(tuple), 2)
        self.assertEqual(tuple[0], expected_domain)
        self.assertEqual(tuple[1], expected_port)
