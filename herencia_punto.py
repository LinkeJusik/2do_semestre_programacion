# -*- coding: utf-8 -*-
"""
Created on Sat May 30 21:52:18 2020

@author: RoGelIO
"""
from math import pow
from math import sqrt
class Punto:
   def __init__(self, x, y):
      self._Cx = x
      self._Cy = y
   
   def _ImprimirPunto(self):
      print("(",self._Cx,",",self._Cy,")")
      
class Distancia(Punto):
   def __init__(self, x, y):
      Punto.__init__(self, x, y)
      
   def CalcularDistancia(self, P0, P1):
      return sqrt((pow(P0._Cx+P1._Cx, 2.0)+pow(P0._Cy+P1._Cy, 2.0)))
   
obj = Distancia(0,0)
obj1 = Punto(1,1)
obj._ImprimirPunto()
obj1._ImprimirPunto()
print(obj.CalcularDistancia(obj1,obj))