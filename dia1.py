# Ejercicios de sintaxis,operadores y listas

# Escribe una función que tome una lista de números y devuelva la suma de todos los elementos.
lista = [14,2,34,3,26,18]

def sumList(lista):
    return sum(lista)

# def sumList2(lista):
#     suma = 0 #MAL PORQUE SI HAY NUMEROS NEGATIVOS DARÍA ERROR
#     for number in lista:
#         suma+=number
#     return suma

print(sumList(lista))
# print(sumList2(lista))

# Escribe una función que reciba una lista de números y devuelva el número más grande de la lista.
def biggerList(lista):
    lista.sort()
    return lista[-1]

def biggerList2(lista):
    biggerNumber = 0
    for number in lista:
        if number > biggerNumber:
            biggerNumber = number
    return biggerNumber
    
print (biggerList(lista))
print (biggerList2(lista))

# Escribe una función que reciba una lista y devuelva el número de elementos en ella.
def countList(lista):
    return len(lista)

def countList2(lista):
    count = 0
    for number in lista:
        count+=1
    return count

print(countList(lista))
print(countList2(lista))

# Escribe una función que reciba una lista y un valor, y devuelva True si el valor está en la lista, False en caso contrario.
def verifyList(lista: list,valor):
    if valor in lista:
        return True
    else:
        return False    

print(verifyList(lista,1)) 
print(verifyList(lista,34)) 

# Escribe una función que reciba una lista de números y devuelva el resultado de multiplicar todos los elementos.
def multiplyList(lista:list):
    value=1
    for number in lista:
        value*=number
    return value

print(multiplyList(lista))

# Escribe una función que tome un string y devuelva cuántas vocales (a, e, i, o, u) tiene.
def countVocals(cadena):
    vocals = ['a','e','i','o','u','á','é','í','ó','ú']
    counter = 0
    for letter in cadena:
        if letter.lower() in vocals:
            counter += 1
    return counter

print(countVocals("Python es increíble"))

# Dada una lista de palabras, devuelve la palabra más larga.
lista= ["Hola","Amigo","Elefante","Gato",]
def largestWord(lista):
    counter = 0
    largestWord = ""
    for word in lista:
        letters = len(word)
        if letters > counter:
            counter = letters
            largestWord = word
    return largestWord

print(largestWord(lista))

# Escribe una función que reciba una lista de números y devuelva un string donde cada número esté separado por una coma.
lista = [2,4,6,5,3,1]
def transformList(lista):
    string = ""
    for number in lista:
        string += f"{number},"
    return string
print(transformList(lista))

# Dado un string, devuelve otro string donde el orden de las palabras esté invertido.
def reverseString(cadena):
    lista = list(cadena)
    lista.reverse()
    cadena = ""
    for letter in lista:
        cadena+=letter
    return cadena

print(reverseString("Hola que tal"))

# Dada una lista con elementos mixtos (strings, enteros, flotantes, booleanos), devuelve solo los números (enteros y flotantes).
lista=["Python", 3, True, 5.7, "Backend", 42]
def filterList(lista):
    new_list=[]
    for element in lista:
        if isinstance(element,float) or isinstance(element,int) and not isinstance(element,bool):
            new_list.append(element)
    return new_list

print(filterList(lista))

# Ejercicio 1: Contar vocales en un string
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vocales)

# Ejercicio 2: Encontrar la palabra más larga en una lista
def palabra_mas_larga(lista):
    return max(lista, key=len)

# Ejercicio 3: Convertir lista de números en string
def convertir_a_string(lista):
    return ",".join(map(str, lista))

# Ejercicio 4: Invertir el orden de las palabras en un string
def invertir_palabras(texto):
    return " ".join(texto.split()[::-1])

# Ejercicio 5: Filtrar números de una lista mixta
def filtrar_numeros(lista):
    return [elemento for elemento in lista if isinstance(elemento, (int, float))]

# Escribe una función que reciba un string con varias palabras y devuelva el string con cada palabra iniciando en mayúscula (como un título).
def titleStrings(cadena):
    return cadena.title()

print(titleStrings("Hola que tal estas"))

# Escribe una función que reciba una lista de palabras y una letra, y devuelva una nueva lista con las palabras que contienen esa letra.
def searchLetter(lista,letra):
    new_list = []
    for word in lista:
        if letra in word:
            new_list.append(word)
    return new_list

print(searchLetter(["Hola","eres","un","amigo","muy","agradable"], "a"))

# Escribe una función que reciba una lista y devuelva una nueva lista sin elementos duplicados.
def deleteDuplicate(lista:list):
    new_list = []
    for element in lista:
        if element not in new_list:
            new_list.append(element)
    
    return new_list

print(deleteDuplicate([1,2,4,6,4,2,7,8,1,2]))

# Escribe una función que reciba un número entero y devuelva una lista con sus dígitos individuales.
def splitInteger(entero):
    cadena = str(entero)
    new_list = []
    for element in cadena:
        new_list.append(element)
    
    return new_list

print(splitInteger(145))

# Escribe una función que reciba un string y devuelva un diccionario con la cantidad de veces que aparece cada caracter.
def charFrequency(cadena: str):
    dictionary = {}
    for letter in cadena:
        if letter in dictionary:
            dictionary[letter] +=1  
        else:
            dictionary[letter] =1
    return dictionary

print(charFrequency("banana"))  

# Reemplazar los Números Negativos con 0
numeros = [1,4,-4,7,-2,-9,-8,-4]
def negativesToZero(lista):
    return [0 if num<0 else num for num in numeros]

print(negativesToZero(numeros))

# Dada una lista de nombres, devuelve solo los que contienen la letra 'a'.
nombres = ["andres","clara", "fer","juan"]
def namesWithA(lista):
    return [nombre for nombre in nombres if "a" in nombre]

print(namesWithA(nombres))

# Convierte una lista de palabras en una lista con la cantidad de letras de cada palabra.
nombres = ["andres","clara", "fer","juan"]
def listToLenght(lista):
    return [len(nombre) for nombre in nombres]
print(listToLenght(nombres))

# Dada una lista de palabras, devuelve las que empiezan con vocal
palabras = ["elefante", "mesa", "avión", "oso", "barco"]
def wordsStartWithVowel(lista):
    return [palabra for palabra in palabras if palabra[0].lower() in "aeiou"]

print(wordsStartWithVowel(palabras))

