import unittest
from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine

class TestEngines(unittest.TestCase):
    def test_CapuletEngine_needs_service(self):
        engine = CapuletEngine(10000, 40001)
        self.assertTrue(engine.needs_service())
        
        engine = CapuletEngine(10000, 39999)
        self.assertFalse(engine.needs_service())
    
    def test_SternmanEngine_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())
        
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())
    
    def test_WilloughbyEngine_needs_service(self):
        engine = WilloughbyEngine(10000, 70001)
        self.assertTrue(engine.needs_service())
        
        engine = WilloughbyEngine(10000, 69999)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()