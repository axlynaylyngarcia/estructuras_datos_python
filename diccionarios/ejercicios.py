# EJERCICIOS DICCIONARIO

# Manipulación 

# 1. Muestra la traducción al inglés de los días Lunes, Martes y Miércoles.

diassemanaingles = {"Lunes" : "Monday",
                   "Martes": "Tuesday",
                   "Miércoles" : "Wednesday", 
                   "Jueves" : "Thursday",
                   "Viernes": "Friday",}

print(diassemanaingles["Lunes"])
print(diassemanaingles["Miércoles"])
print(diassemanaingles["Viernes"])

# 2. Añade los días sábado y domingo, modificando el valor de algún elemento y borrando algún elemento.

diassemanaingles = {"Lunes" : "Monday",
                   "Martes": "Tuesday",
                   "Miércoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes": "Friday"}
print(diassemanaingles)
diassemanaingles["Sábado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)
del diassemanaingles["Lunes"]
print(diassemanaingles)

# 3. Es posible utilizar las funciones len, max y min con los diccionarios. La primera devolverá el número de elementos que contiene el diccionario; la segunda, el elemento con el valor mayor y la tercera, el elemento con el valor menor. El valor mayor y el valor menor seárn devueltos siempre que pueda calcularse dependiendo de los elementos que componen el diccionario. 

diassemanaingles = {"Lunes" : "Monday",
                   "Martes": "Tuesday",
                   "Miércoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes": "Friday"}
print("Número de elementos del diccionario: ", len(diassemanaingles))
print("Elemento mayor del diccionario: ",max(diassemanaingles))
print("Elemento menor del diccionario: ",min(diassemanaingles))












