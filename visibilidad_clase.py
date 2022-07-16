# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:32:38 2020

@author: RoGelIO
"""

"""
El nivel de visibilidad de la clase, ya sea de atributos y métodos
se da a 3 niveles:
   1.- Público. Que podemos acceder a métodos o atributos
       desde cualquier parte de nuestro código.
   2.- Privado. Que podemos acceder a métodos o atributos
       solamente desde la clase en donde estén definidos.
   3.- Protegido. Que podemos acceder a métodos o atributos
       desde la clase y desde las clases con las cuales se 
       aplique la herencia.
       
En los diagrmas de clases se representan de la siguiente forma:
   1.- Público    +
   2.- Privado    -
   3.- Protegido  #
   
En el código se representan así:
       visibilidad variable       metodo
   1.- Público      suma          suma()
   2.- Privado     __suma        __suma()
   3.- Protegido   _suma         _suma()
"""

class Prueba:
   def __init__(self):
      self.publico=10
      self._protegido=20
      self.__privado=50
   
   def Publico(self):
      print("Método público")
      
   def _Protegido(self):
      print("Método protegido")
      
   def __Privado(self):
      print("Método privado")
      
class Hija(Prueba):
   def __init__(self):
      Prueba.__init__(self)
      
   def tres(self):
      self._Protegido()
      
   def uno(self):
      print(self._protegido)
"""
# Quitar los comentarios de la función y ejecutar
# Como el atributo esta definido como privado no lo
# puedo llamar fuera de la clase y por lo tanto nos
# marca un error
"""
  
#   def dos(self):
#      print(self.__privado)
 
   
"""
# Fuera de las clases     
# Creamos el objeto de tipo hija     
"""
obj = Hija()
# Mandamos a imprimir el atributo publico
print(obj.publico)
"""
# Quitar el comentario del print y ejecutar
# Como el atributo esta definido como privado no lo
# puedo llamar fuera de la clase y por lo tanto nos
# marca un error
"""
#print(obj.privado)
"""
# Quitar el comentario del print y ejecutar
# Como el atributo esta definido como protegido solamente
# lo puedo llamar dentro de las clases en las que aplica la
# herencia y por lo tanto nos marca error
"""
#print(obj.protegido)
"""
Al invocar este método verificamos que se imprime el valor 
del atributo que esta definido como protegido en la clase
Prueba y que se hereda a la clase hija
"""
obj.uno()
"""
# Quitar el comentario del print y ejecutar
# Como el atributo esta definido como privado no lo
# puedo llamar fuera de la clase y por lo tanto nos
# marca un error
"""
#obj.dos()

obj.tres()
      


















