"""Testing the methods"""

import unittest
from unittest import TestCase
from palindrome import palindrome
from primalidad import es_primo


class TestingFunctions(TestCase):
    """Tests to know if the methods works well"""
    
    def test_palindrome(self):
        """Testing palindrome method"""
        self.assertEqual(palindrome('Ligar es ser agil'), True)
        self.assertEqual(palindrome('Arepera'), True)
        self.assertEqual(palindrome('Esto no es un palindromo'), False)
        self.assertEqual(palindrome('ESto tampoco es un palindromo'), False)
        self.assertEqual(palindrome('Ana'), True)

    def test_es_primo(self):
        """Testing es_primo method"""
        self.assertEqual(es_primo(100), False)
        self.assertEqual(es_primo(200), False)
        self.assertEqual(es_primo(53), True)
        self.assertEqual(es_primo(23), True)
        self.assertEqual(es_primo(45), False)
        self.assertEqual(es_primo(32), False)
        self.assertEqual(es_primo(142), False)


if __name__ == '__main__':
    unittest.main()
