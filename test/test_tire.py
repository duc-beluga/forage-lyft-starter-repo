import unittest
from tire.Carrigan import Carrigan
from tire.Octoprime import Octoprime

class TestEngines(unittest.TestCase):
    def test_CarriganTire_needs_service(self):
        tire = Carrigan([0.3,0.5,0.7,0.9])
        self.assertTrue(tire.needs_service())
        
        tire = Carrigan([0.3,0.5,0.7,0.8])
        self.assertFalse(tire.needs_service())
    
    def test_OctoprimeTire_needs_service(self):
        tire = Octoprime([0,1,1,1])
        self.assertTrue(tire.needs_service())
        
        tire = Octoprime([0,0.9,1,1])
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()