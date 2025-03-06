# 📌 Objetivo: Crear un generador que devuelva números pares de uno en uno.

def pares():
    for i in range(1,50):
        if i%2==0:
            yield i

pares = pares()

print(next(pares))
print(next(pares))
print(next(pares))
print(next(pares))
print(next(pares))
print(next(pares))
print(next(pares))

