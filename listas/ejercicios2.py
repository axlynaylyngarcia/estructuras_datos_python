# EJERCICIOS LISTAS

# Métodos propios

lista =[45,32,3,78]
print("lista original: " , lista)
# funcion append: añade un elemento a la lista
lista.append(995)
lista.append(7)
print("Lista despues de usar append", lista)
# funcion sort: ordena la lista
lista.sort()
print("Lista ordenada: ", lista)
# funcion reverse: invierte el orden de la lista.
lista.reverse
print(" Lista al reves: " , lista)
# Funcion extend: añade los elementos de una lista hacia la lista
lista_extend =[1,5,87,45]
lista.extend(lista_extend)
print(" lista despues de extend; ", lista)
# funcion cound: cuenta el numero de veces que aparece el elemento indicado como parántesis de la lista
print(" Numero de elementos 45: ", lista.cound(45))
# funcion insert: añade el elemento pasado como parametro a la lista en a posicion inidcda tambien por parametros
lista.insert(4,11)
print("lista insert; ", lista)
# funcion remove: elimina la primera ocurrencia empezando por la izquierda de la lista del elemento indicado como parametro.
lista.remove(45)
print("Lista despues de remove: ", lista)
# funcion index: devuelve la posicion de la primera ocuurencia de izquieda a derecha en la lista del elemento pasado como prametro.
print("Posicion del elemento 111", lista.index(111))
# funcion pop: elimina un elemento de la lista y lo devuelve como resultado de la operacion,
lista.pop()
print("Lista despues de pop:", lista)
#funcion clear: eliina todos los elementos de la lista.
lista.clear()
print("lista despues de clear: ", lista)







