import unittest

import socket_test

class Testresults(unittest.TestCase):

    def test_port(self):
        self.assertEqual(socket_test.sockets("192.168.254.254", 53), "close")

if __name__ == '__main__':
    unittest.main()