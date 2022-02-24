import math as m

cadena = "m.pow(3+4/2, 2)"

resultado = eval(cadena)

print(resultado)

#Evaluacion de Funciones de Segundo Grado:
# ax**2 + bx + c

#Formula General: -b +- Math.sqrt( (b**2 - 4ac)) / (2*a)

#dentro de un boton:

a = 1  #self.spinBoxA.value()
b = 4  #self.spinBoxB.value()
c = 2  #self.spinBoxC.value()

cadena1 = "-b + m.sqrt( (b**2 - 4*a*c)) / (2*a)"
cadena1 = eval(cadena1)
print("Resultado X1: ", cadena1)

cadena2 = "-b - m.sqrt( (b**2 - 4*a*c)) / (2*a)"
cadena2 = eval(cadena2)
print("Resultado X2:", cadena2)