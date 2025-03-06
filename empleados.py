# Ejercicio Final: Combinar Todo
# 🔹 Objetivo:
# Crea un sistema de gestión de empleados que use clases, listas, diccionarios y módulos.

# 📌 Debe incluir:

# Clase Empleado con nombre, edad, puesto, salario.
# Clase Empresa que maneja una lista de empleados.
# Método agregar_empleado(empleado).
# Método mostrar_empleados().
# Método buscar_empleado(nombre).

class Empleado:
    def __init__(self,nombre,edad,puesto,salario):
        self.__nombre = nombre
        self.__edad = edad
        self.__puesto = puesto
        self.__salario = salario

    def __str__(self):
        return f'Nombre: {self.__nombre}, Edad: {self.__edad}, Puesto: {self.__puesto}, Salario: {self.__salario} '
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getPuesto(self):
        return self.__puesto
    
    def getSalario(self):
        return self.__salario
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def setEdad(self,edad):
        self.__edad = edad
    
    def setPuesto(self,puesto):
        self.__puesto = puesto
    
    def setSalario(self,salario):
        self.__salario = salario