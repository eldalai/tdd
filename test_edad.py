from datetime import datetime
import unittest
from person.model import Persona
from utils.edad_util import edad

class TestEdad(unittest.TestCase):
    def test_edad_1(self):
        gabriel = Persona(nacimiento=datetime(1971, 07, 17))
        resultado = edad(gabriel)
        self.assertEqual(resultado, 45)
    def test_edad_2(self):
        gabriel = Persona(nacimiento=datetime(1971, 12, 17))
        resultado = edad(gabriel)
        self.assertEqual(resultado, 44)

if __name__ == "__main__":
    unittest.main()
