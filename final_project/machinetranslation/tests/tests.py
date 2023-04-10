import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_f2e(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_null_e2f(self):
        self.assertEqual(english_to_french("Null"),"Null")

    def test_null_f2e(self):
        self.assertEqual(french_to_english("Null"),"Null")

if __name__ == '__main__':
    unittest.main()
