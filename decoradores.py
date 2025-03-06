# Objetivo: Crear un decorador que mida cuánto tarda en ejecutarse una función.

import time

def medir_tiempo(funcion):
    def funcion_modificada():
        inicio = time.time()
        resultado = funcion()
        fin =time.time()

        print(f"Se ha tardado {fin-inicio:.5f} segundos")
        return resultado
    return funcion_modificada

@medir_tiempo
def dormir():
    time.sleep(2)
    print("Operacion completada")

# dormir()

# Objetivo: Crear un decorador que verifique si un usuario tiene permisos antes de ejecutar una función.

def verificar_permisos(funcion):
    def funcion_modificada(usuario,*args):
        if usuario != "administrador":
            print("No tienes permiso")
            return
        else:
            print("Tienes permiso")
            resultado = funcion(*args)
        return resultado
    return funcion_modificada

@verificar_permisos
def eliminar_usuario(usuario):
    print(f"Has eliminado al usuario {usuario}")

eliminar_usuario("administrador","Carlos")


