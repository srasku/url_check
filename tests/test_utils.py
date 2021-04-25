"""
Tests for `utils` module.
"""
import unittest

from url_check import utils


class TestGetHostAndPort(unittest.TestCase):
    """
    This class is used to test `get_host_and_port()` function.
    """
    def test_valid_case(self):
        """
        Test splitting string into host and port components
        """
        self.host_port_tester(
                'www.some-domain.com:8129', 'www.some-domain.com', 8129
                )
        self.host_port_tester(
                'www.another-domain.com', 'www.another-domain.com', 80
                )
        self.host_port_tester('host-only:8912', 'host-only', 8912)

    def host_port_tester(self, param, expected_domain, expected_port):
        """
        Helper function to test `get_host_and_port()`.
        """
        values = utils.get_host_and_port(param)
        self.assertEqual(len(values), 2)
        self.assertEqual(values[0], expected_domain)
        self.assertEqual(values[1], expected_port)
