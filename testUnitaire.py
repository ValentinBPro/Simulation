import unittest
from Simulation import Get_picBas_valeur, analyse_achat, maj_delta_achat

delta_test=[9,8,7,6,5,4,5,6] # pic bas à 4

class TestFonctions(unittest.TestCase):
    def test_Get_picBas_valeur(self):
        self.assertEqual(Get_picBas_valeur(delta_test), 4)

    def test_analyse_achat(self):
        deficit, rehausse = analyse_achat(delta_test)
        self.assertEqual(deficit, -0.56)
        self.assertEqual(rehausse, 0.5)
        
    #def test_maj_delta_achat(self):
    #   self.assertEqual(maj_delta_achat(delta_test),-0.55,0.5)

if __name__ == '__main__':
    unittest.main()
