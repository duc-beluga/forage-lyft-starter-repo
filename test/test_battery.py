import unittest
from datetime import date, timedelta
from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattery

class TestBatteries(unittest.TestCase):
    def test_SpindlerBattery_needs_service(self):
        battery = SpindlerBattery(date.today() - timedelta(days=1106), date.today())
        self.assertTrue(battery.needs_service())
        
        battery = SpindlerBattery(date.today() - timedelta(days=1104), date.today())
        self.assertFalse(battery.needs_service())
    
    def test_NubbinBattery_needs_service(self):
        battery = NubbinBattery(date.today() - timedelta(days=1461), date.today())
        self.assertTrue(battery.needs_service())
            
        battery = NubbinBattery(date.today() - timedelta(days=731), date.today())
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
