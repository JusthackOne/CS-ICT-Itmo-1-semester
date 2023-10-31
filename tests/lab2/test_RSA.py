import unittest

import src.lab2.RSA as RSA

class EncryptandDecryptTestCase(unittest.TestCase):
    def test_one_encrypt(self):
        res = RSA.generate_keypair(3,2)
        self.assertEqual(res, ((1, 6), (1, 6)))

    def test_two_encrypt(self):
        res = RSA.generate_keypair(7, 5)
        self.assertEqual(res, ((13, 35), (-11, 35)))

    def test_three_encrypt(self):
        res = RSA.generate_keypair(7, 5)
        self.assertEqual(res, ((23, 35), (-1, 35)))

    def test_four_encrypt(self):
        res = RSA.generate_keypair(7, 5)
        self.assertEqual(res, ((17, 35), (-7, 35)))

    def test_five_encrypt(self):
        res = RSA.generate_keypair(7, 5)
        self.assertEqual(res, ((19, 35), (-5, 35)))