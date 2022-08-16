mi_lista = []
numeroUsuario = int (input("Por favor, introducir un numero entero: "))
mi_lista.append(numeroUsuario)

numeroUsuario2 = int (input("Por favor, introduce otro numero entero: "))
mi_lista.append(numeroUsuario2)

numeroUsuario3 = int (input("Por favor, introduce otro numero entero: "))
mi_lista.append(numeroUsuario3)

numeroUsuario4 = int (input("Por favor, introduce otro numero entero: "))
mi_lista.append(numeroUsuario4)

numeroUsuario5 = int (input("Por favor, introduce otro numero entero: "))
mi_lista.append(numeroUsuario5)

print (mi_lista)

print ("Esta es una suma de todos los elementos de la lista:")

def sumar_lista(mi_lista):
    suma = 0

    for numero in mi_lista:
        suma += numero
    return suma

print (sumar_lista(mi_lista))
print ("Este es el promedio de todos los elementos:")

def promedio(mi_lista):
    prom = sum(mi_lista) / len(mi_lista)
    return prom

print (promedio(mi_lista))


maximo = mi_lista[0]
for i in range (0,len(mi_lista)):
    if mi_lista [i]>maximo:
        maximo=mi_lista[i]
print("Este es el numero mayor:" , maximo)


minimo = mi_lista[0]
for i in range (0,len(mi_lista)):
    if mi_lista [i]<minimo:
        minimo=mi_lista[i]
print("Este es el numero menor:" , minimo)
