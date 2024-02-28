import unittest
from Caesar.Caesar import Caesar


class TestCaesar(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(Caesar.encrypt("hello", 3), "khoor")

    def test_decrypt(self):
        self.assertEqual(Caesar.decrypt("khoor", 3), "hello")

    def test_crack_caesar(self):
        encrypted_text = Caesar.encrypt("hello", 3)
        cracked_text = Caesar.crack_caesar(encrypted_text)
        self.assertEqual(cracked_text, "hello") #edit to contain


if __name__ == '__main__':
    unittest.main()