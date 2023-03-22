import unittest
import main


class TestMolekyl(unittest.TestCase):
    def test_enkel_molekyl(self):
        self.assertEqual(main.kolla_syntax("Ag3"), "Formeln är syntaktiskt korrekt")

    def test_syntaxfel(self):
        self.assertEqual(main.kolla_syntax("H01001"), "För litet tal vid radslutet 1001")

    def test_saknad_stor_bokstav(self):
        self.assertEqual(main.kolla_syntax("he1"), "Saknad stor bokstav vid radslutet he1")

    def test_för_litet_tal(self):
        self.assertEqual(main.kolla_syntax("He1"), "För litet tal vid radslutet ")


if __name__ == "__main__":
    unittest.main()
