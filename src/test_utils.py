import unittest

import utils

class TestGetHostAndPort(unittest.TestCase):
    def test_valid_case(self):
        self.host_port_tester('www.some-domain.com:8129', 'www.some-domain.com', 8129)
    def host_port_tester(self, param, expected_domain, expected_port):
        tuple = utils.get_host_and_port(param)
        self.assertEqual(len(tuple), 2)
        self.assertEqual(tuple[0], expected_domain)
        self.assertEqual(tuple[1], expected_port)
