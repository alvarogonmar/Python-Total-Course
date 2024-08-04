import unittest
import Cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    #EMPEZAR SIEMPRE CON TEST
    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = Cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DIA')

if __name__ == '__main__':
    unittest.main()