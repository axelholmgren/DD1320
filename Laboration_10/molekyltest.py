import unittest
import main


class TestMolekyl(unittest.TestCase):
    def test_molekyl(self):
        with open(
            "/Users/axelholmgren/GitHub/DD1320/Laboration_9/sample_1.txt", "r", encoding="utf-8"
        ) as sample_1:
            inut = []
            for rad in sample_1:
                inut.append(rad.split(","))
            for i in inut:
                self.assertEqual(main.kolla_syntax(i[0])[0].strip(), i[1].strip())


if __name__ == "__main__":
    unittest.main()
