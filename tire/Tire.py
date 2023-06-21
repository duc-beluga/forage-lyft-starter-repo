from abc import ABC, abstractmethod
from Serviceable import Serviceable

class Tire(Serviceable):

    @abstractmethod
    def needs_service(self) -> bool:
        pass