from .Tire import Tire
from typing import List

class Octoprime(Tire):
    def __init__(self, sensor_arr: List[float]):
        self.sensor_arr = sensor_arr
    
    def needs_service(self) -> bool:
        return sum(self.sensor_arr) >= 3

