import unittest
from src.utils import ler_planilha

class TestLerPlanilha(unittest.TestCase):
    def test_ler_planilha(self):
        df = ler_planilha('data/minha_planilha.xlsx')
        self.assertIsNotNone(df)
        self.assertGreater(len(df),  0)

if __name__ == '__main__':
    unittest.main()