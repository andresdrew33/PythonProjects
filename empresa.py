# Ejercicio Final: Combinar Todo
# 🔹 Objetivo:
# Crea un sistema de gestión de empleados que use clases, listas, diccionarios y módulos.

# 📌 Debe incluir:

# Clase Empleado con nombre, edad, puesto, salario.
# Clase Empresa que maneja una lista de empleados.
# Método agregar_empleado(empleado).
# Método mostrar_empleados().
# Método buscar_empleado(nombre).

from empleados import Empleado
class Empresa:
    def __init__(self):
        self.__empleados : list[Empleado] = []
    
    def agregarEmpleados(self,empleado:Empleado):
        self.__empleados.append(empleado)
        print(f"Se ha agregado un empleado con nombre {empleado.getNombre()}")
    
    def mostrarEmpleados(self):
        for empleado in self.__empleados:
            print(empleado)
    
    def buscarEmpleado(self,nombre)->Empleado | str:
        for empleado in self.__empleados:
            if empleado.getNombre() == nombre:
                return empleado
        return "Empleado no encontrado"




