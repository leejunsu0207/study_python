import math

class Cone :
    def __init__(self, radius = 20, height = 30):
        self.rad = radius
        self.hei = height

    def get_vol(self):
        return  1 / 3 * math.pi *  self.rad ** 2 *  self.hei

    def get_surf(self):
        return  3.14 * self.rad ** 2 + math.pi * self.rad * self.hei



class PCone :
    def __init__(self, radius = 20, height = 30):
        self.__rad = radius
        self.__hei = height

    def get_vol(self):
        return  1 / 3 * math.pi *  self.__rad ** 2 *  self.__hei

    def get_surf(self):
        return  math.pi * self.__rad ** 2 + math.pi * self.__rad * self.__hei

    def get_radius(self):
        return self.__rad

    def get_radius(self, radius):
        if radius > 0 :
            self.__rad = radius