from .Tire import Tire
from typing import List

class Carrigan(Tire):
    def __init__(self, sensor_arr: List[float]):
        self.sensor_arr = sensor_arr
    
    def needs_service(self) -> bool:
       return any(num >= 0.9 for num in self.sensor_arr)

