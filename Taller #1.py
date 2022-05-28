# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:32:48 2022

@author: Deimer Morelo Ospino
"""
a=int(input("Por favor ingrese el valor correspondiente a la variable 'a': " ))
b=int(input("Por favor ingrese el valor correspondiente a la variable 'b': " ))
c=int(input("Por favor ingrese el valor correspondiente a la variable 'c': " ))
d=int(input("Por favor ingrese el valor correspondiente a la variable 'd': " ))
e=int(input("Por favor ingrese el valor correspondiente a la variable 'e': " ))
f=int(input("Por favor ingrese el valor correspondiente a la variable 'f': " ))

ecu1=((a+(b/c))/(d+(e/f)))
ecu2=(a-(b/(c-d)))

print("\n"+"El resultado de la ecuacion 1 original es "+str(ecu1))
print("\n"+"El resultado de la ecuacion 2 original es "+str(ecu2))
      
aux = ecu1
ecu1 = ecu2
ecu2 = aux

print("\n"+"El resultado de la nueva ecuacion 1 es "+str(ecu1))
print("\n"+"El resultado de la nueva ecuacion 2 es "+str(ecu2))



