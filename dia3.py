# Clases, modelos y paquetes
# EJERCICIO 1
# Crea una clase Persona con:
# Atributos: nombre, edad.
# Un método saludar() que imprima "Hola, mi nombre es {nombre} y tengo {edad} años".

class Persona:

    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def setNombre(self,nombre):
        self.__nombre = nombre

    def setEdad(self,edad):
        self.__edad = edad
    
    def saludar(self):
        print(f'Hola, mi nombre es {self.__nombre} y tengo {self.__edad} años')

persona = Persona("andres",31)
print(persona.getEdad())
print(persona.getNombre())
persona.setNombre("clara")
persona.setEdad(29)
print(persona.getNombre())
print(persona.getEdad())
persona.saludar()

# EJERCICIO 2
# Crea una clase Coche con:
# Atributos: marca, modelo, velocidad_actual.
# Método acelerar() que aumente la velocidad en 10 km/h.

class Coche:
    def __init__(self,marca,modelo):
        self.__marca = marca
        self.__modelo = modelo
        self. __velocidad = 0
    
    def getVelocidad(self):
        return self.__velocidad
    
    def acelerar(self):
        self.__velocidad +=10
    
    def frenar(self):
        self.__velocidad -=5

coche = Coche("Opel","Corsa")
print(coche.getVelocidad())
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
coche.acelerar()
print(coche.getVelocidad())

# EJERCICIO 3
#  Crea una clase CuentaBancaria con:

# Atributos: titular, saldo.
# Métodos:
# depositar(cantidad): Aumenta el saldo.
# retirar(cantidad): Reduce el saldo si hay suficiente dinero.

class CuentaBancaria:
    def __init__(self,titular,saldo = 0):
        self.__titular = titular
        self.__saldo = saldo
    
    def depositar(self,cantidad):
        self.__saldo +=cantidad
        print(f'Se han ingresado {cantidad} euros')
    
    def retirar(self,cantidad):
        if self.__saldo >= cantidad:
            self.__saldo-=cantidad
            print(f"Se han retirado {cantidad} euros. Quedan en la cuenta {self.__saldo} euros")
        else:
            print(f"En la cuenta solo hay {self.__saldo} euros")

    def getSaldo(self):
        return self.__saldo

cuenta = CuentaBancaria("andres")
cuenta.getSaldo()
cuenta.depositar(30)
cuenta.getSaldo()
cuenta.retirar(20)
cuenta.retirar(20)
