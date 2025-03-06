# Ejercicio Final: Combinar Todo
# 🔹 Objetivo:
# Crea un sistema de gestión de empleados que use clases, listas, diccionarios y módulos.

# 📌 Debe incluir:

# Clase Empleado con nombre, edad, puesto, salario.
# Clase Empresa que maneja una lista de empleados.
# Método agregar_empleado(empleado).
# Método mostrar_empleados().
# Método buscar_empleado(nombre).

from empresa import Empresa
from empleados import Empleado

empresa = Empresa()

empleado1 = Empleado("andres",25,"Developer",1600)
empleado2 = Empleado("clara",22,"Profesora",1800)
empleado3 = Empleado("diego",35,"Escalador",1200)

print(empleado1.getNombre())
print(empleado2.getNombre())
print(empleado3.getNombre())

empresa.agregarEmpleados(empleado1)
empresa.agregarEmpleados(empleado2)
empresa.agregarEmpleados(empleado3)

empresa.mostrarEmpleados()

print(empresa.buscarEmpleado("andres"))
print(empresa.buscarEmpleado("rosa"))


