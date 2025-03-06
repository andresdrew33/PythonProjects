# Ejercicios de tuplas,sets y diccionarios

# Crear una función que reciba una lista de números y devuelva otra lista con los valores al cuadrado.
lista=[1,2,3,4,5]
def elevate(lista):
    return [number**2 for number in lista] 
print(elevate(lista))

# Convertir una tupla (nombre, edad, ciudad) en un string formateado.
tupla = ("Andrés",31,"Burgos")
def formatTuple(tupla):
    message = f'{tupla[0]} vive en {tupla[2]} y tiene {tupla[1]} años'
    return message
print(formatTuple(tupla))

# Filtrar personas mayores de edad de un diccionario.
personas = {"Juan": 15, "Ana": 20, "Luis": 30, "Maria": 17}
def filterAge(personas):
    return {nombre : edad for nombre,edad in personas.items() if edad>=18 }
print(filterAge(personas))

# Contar cuántas veces aparece cada palabra en un string.
def contarPalabras(cadena):
    # lista = cadena.split(" ")
    # diccionario={}
    # for word in lista:
    #     if word not in diccionario:
    #         diccionario[word]=1
    #     else:
    #         diccionario[word]+=1
    # return diccionario
    palabras = cadena.split()
    return {palabra: palabras.count(palabra) for palabra in set(palabras)}

print(contarPalabras("hola mundo hola python"))  

# Crear un diccionario a partir de dos listas.
lista1 = ["Nombre","Apellidos","Edad"]
lista2 = ["Andrés","Martín",31]
def mergeList(lista1,lista2):
    return dict(zip(lista1,lista2))
    
print(mergeList(lista1,lista2))

# Escribe una función que encuentre los elementos en común entre dos listas.
lista1 = [1,3,5,7,9]
lista2 = [1,3,4,6,8]
def searchComun(lista1,lista2):
    # return[number for number in lista1 if number in lista2]
    return set(lista1) & set(lista2)
print(searchComun(lista1,lista2))

# Escribe una función que devuelva los elementos que están en la primera lista, pero no en la segunda.
lista1 = [1,3,5,7,9]
lista2 = [1,3,4,6,8]
def notSecond(lista1,lista2):
    return set(lista1) - set(lista2)
print(notSecond(lista1,lista2))

# Escribe una función que reciba un diccionario y devuelva un nuevo diccionario con claves y valores intercambiados.
diccionario = {"a": 1, "b": 2, "c": 3}
def reverseDict(diccionario):
    return {key:value for value,key in diccionario.items()}

print(reverseDict(diccionario))

# Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean su cuadrado.
def createDict():
    return {i:i**2 for i in range(1,6)}
print(createDict())

# Dado una lista de diccionarios con nombres y edades, crea una función que devuelva solo las personas mayores de 18 años.
personas = [
    {"nombre": "Carlos", "edad": 17},
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "María", "edad": 16}
]
def mayoresEdad(diccionario):
    return [persona for persona in diccionario if persona["edad"]>=18]
print(mayoresEdad(personas))

# Crea una función que reciba una lista de diccionarios y un número n, y devuelva los nombres de las personas que tengan exactamente n años.
personas = [
    {"nombre": "Carlos", "edad": 17},
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "María", "edad": 25}
]
def searchAge(diccionario,edad):
    return [persona for persona in diccionario if persona["edad"]==edad]
print(searchAge(personas,25))