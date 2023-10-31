import unittest

import src.lab2.RSA as RSA

class EncryptandDecryptTestCase(unittest.TestCase):
    def test_one_encrypt(self):
        res = RSA.generate_keypair(3,2)
        self.assertEqual(res, ((1, 6), (1, 6)))

