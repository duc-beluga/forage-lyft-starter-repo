from Serviceable import Serviceable

class Battery(Serviceable):

    @abstractmethod
    def needs_service(self) -> bool:
        pass