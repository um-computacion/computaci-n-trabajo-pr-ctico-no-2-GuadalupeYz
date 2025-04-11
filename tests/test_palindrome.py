import unittest
from src.palindrome import is_palindrome

class TestPalindromesSimples(unittest.TestCase):
    
    def test_palindrome_madam(self):
        self.assertTrue(is_palindrome("madam"))
    
    def test_palindrome_racecar(self):
        self.assertTrue(is_palindrome("racecar"))
    
    def test_palindrome_level(self):
        self.assertTrue(is_palindrome("level"))

class TestPalindromesFrases(unittest.TestCase):
    
    def test_palindrome_amaplan(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
    
    def test_palindrome_wasitacar(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
    
    def test_palindrome_nolemon(self):
        self.assertTrue(is_palindrome("No lemon, no melon"))
    
    def test_palindrome_anitalavalatina(self):
        self.assertTrue(is_palindrome("Anita lava la tina"))
    
    def test_palindrome_madamimadam(self):
        self.assertTrue(is_palindrome("Madam, I'm Adam"))
    
    def test_palindrome_larutatural(self):
        self.assertTrue(is_palindrome("La ruta natural"))
    
    def test_palindrome_amorroma(self):
        self.assertTrue(is_palindrome("Amor, Roma"))

class TestFrasesNoPalindromas(unittest.TestCase):

    def test_frase_comun(self):
        self.assertFalse(is_palindrome("Esto no es un palindromo"))

    def test_frase_con_mayusculas(self):
        self.assertFalse(is_palindrome("Hola Mundo"))

    def test_frase_con_simbolos(self):
        self.assertFalse(is_palindrome("comprar huevo"))

    def test_frase_larga(self):
        self.assertFalse(is_palindrome("Guadalupe Yañez"))

    def test_frase_casi_palindromo(self):
        self.assertFalse(is_palindrome("Anita lava la tina pero no"))

if __name__ == '__main__':
    unittest.main()