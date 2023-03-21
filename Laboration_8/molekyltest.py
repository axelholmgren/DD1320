import unittest
from LinkedQueue import LinkedQ


class TestMolekyl(unittest.TestCase):
    def test_enkel_molekyl(self):
        self.assertEqual(molekyl("Ag3"), "Följer syntaxen!")

    def test_syntaxfel(self):
        self.assertEqual(regel_molekyl("Ag3"), "Följer inte syntaxen!")
