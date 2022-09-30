#!/usr/bin/python3
import dis
import math

class Magic:
    
    def __init__(self, radius=0):
        if type(self.radius) is not int or type(self.radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.radius = radius

    def area(self):
        return ((self.radius ** 2) * math.pi)

    def circunference(self):
        return (2 * math.pi * self.radius)

dis.dis(Magic)
