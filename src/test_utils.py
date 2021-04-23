import unittest

import utils

class TestGetHostAndPort(unittest.TestCase):
    def test_valid_case(self):
        tuple = utils.get_host_and_port('www.some-domain.com:8129')
        self.assertEqual(len(tuple), 2)
        self.assertEqual(tuple[0], 'www.some-domain.com')
        self.assertEqual(tuple[1], 8129)
