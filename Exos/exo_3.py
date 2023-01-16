from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    name = "<Unnamed>"
    @abstractmethod
    def demarer(self):
        pass

class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def decoller(self):
        pass

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def rouler(self):
        pass

class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def couler(self):
        pass

class UAV(UnmannedVehicle,AerialVehicle):
    """Unmanned Aerial Vehicle"""
    def demarer(self):
        print("Je suis en marche !")
    pass

    def decoller(self):
        print("Je décolle !\n" )
    pass

class UUV(UnmannedVehicle,UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    def demarer(self):
        print("Je suis en marche !")
    pass

    def couler(self):
        print("Je coule !\n" )
    pass

class UGV(UnmannedVehicle,GroundVehicle):
    """Unmanned Ground Vehicle"""
    def demarer(self):
        print("Je suis en marche !")
    pass

    def rouler(self):
        print("Je roule !\n")
    pass

if __name__ == "__main__" :   
    uav = UAV()
    uav.demarer()
    uav.decoller()

    ugv = UGV()
    ugv.demarer()
    ugv.rouler()

    uuv = UUV()
    uuv.demarer()
    uuv.couler()

