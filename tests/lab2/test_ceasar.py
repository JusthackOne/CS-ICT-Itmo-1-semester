import unittest

import src.lab2.ceasar as ceasar

class EncryptandDecryptTestCase(unittest.TestCase):
    def test_one_encrypt(self):
        res = ceasar.encrypt_caesar('Hello, world!', 3)
        self.assertEqual(res, 'Khoor, zruog!')

    def test_two_encrypt(self):
        res = ceasar.encrypt_caesar('I love ICT so mach', 8)
        self.assertEqual(res, 'Q twdm QKB aw uikp')

    def test_three_encrypt(self):
        res = ceasar.encrypt_caesar('Django1.2', 10)
        self.assertEqual(res, 'Ntkxqy1.2')

    def test_one_decrypt(self):
        res = ceasar.decrypt_caesar('fqvc2', 2)
        self.assertEqual(res, 'dota2')

    def test_two_decrypt(self):
        res = ceasar.decrypt_caesar('LHRGZ', 25)
        self.assertEqual(res, 'MISHA')

    def test_three_decrypt(self):
        res = ceasar.decrypt_caesar('MppeMzzxEplx^)', 11)
        self.assertEqual(res, 'BeetBoomTeam^)')
