import unittest

import src.lab2.vigenere as vigenere

class EncryptandDecryptTestCase(unittest.TestCase):
    def test_one_encrypt(self):
        res = vigenere.encrypt_vigenere('Hello,world!', 'tictac')
        self.assertEqual(res, 'Amneo,yhznw!')

    def test_two_encrypt(self):
        res = vigenere.encrypt_vigenere('I love ICT so mach', 'tomhardi')
        self.assertEqual(res, 'B zace ZFB lc yhcy')

    def test_three_encrypt(self):
        res = vigenere.encrypt_vigenere('Django1.2', 'pinpong')
        self.assertEqual(res, 'Srncub1.2')

    def test_one_decrypt(self):
        res = vigenere.decrypt_vigenere('pogm2', 'man')
        self.assertEqual(res, 'dota2')

    def test_two_decrypt(self):
        res = vigenere.decrypt_vigenere('XWKCI', 'losvinturas')
        self.assertEqual(res, 'MISHA')

    def test_three_decrypt(self):
        res = vigenere.decrypt_vigenere('txeolwbmltod^)', 'stavkinasport1xbet')
        self.assertEqual(res, 'beetboomteam^)')
