# Métodos propios

# Las funciones de listas que pone a nuestra disposición Python son las siguientes:

# Copy: Realiza una copia exacta del diccionario en uno nuevo. Valor devuelto: diccionario copiado y parámetros no tiene.

diassemanaingles = {"Lunes" : "Monday",
                   "Martes": "Tuesday",
                   "Miércoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes": "Friday"}
print("Diccionario original; ",diassemanaingles)  
diccionariocopia  = diassemanaingles.copy()
print("Diccionario copy: ",diccionariocopia) 

# pop: obtiene el valor de la clave pasada comp parámetro y además elimina el elemento del diccionario. Valor devuelto: valor del elemento o erroe en caso de no encontrar la clave en el diccionario. Parámetros: clave a buscar en el diccionario.

print("Valor del lunes (pop): ",diassemanaingles.pop("Lunes"))
print("Diccionario después del pop: ",diassemanaingles)

# popitem: obtiene un elemento aleatorio del diccionario y lo elimina del mismo.
print("Elemento al azar con pipitem: ", diassemanaingles.popitem())
print("Diccionario después del popitem: ",diassemanaingles)     

# get: obtene el valor de la clave pasada como parámetro.

print("Valor del Martes (get): ",diassemanaingles.get("Martes"))
print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes"))
print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes", "No existe"))

# update: realiza una actualización del diccionario utilizando otro diccionario. Aquellos elementos del diccionario que se utilizan para actualizar el pincipal sustituirán los existentes en el ismo y aquellos elementos que no existían serán aadidos al diccionario como nuevos elementos.

diassemanaingles.update({"Lunes": "MondayNUEVO", "Martes": "TuesdayNUEVO"})
print("Diccionario después del update: ",diassemanaingles)

# setdefault: intenta insertar un elemento (clave y valor) en el diccionario. 

print("etdefault del Sábado: ",diassemanaingles.setdefault("Sabado","Saturday"))
print("Diccionario después del setfault (nuevo elemento): ",diassemanaingles)
print("setdefault del Lunes: ",diassemanaingles.setdefault("Lunes","Lunes"))
print("Diccionario después del seldefault (elemento existente): ",diassemanaingles)

# items: devuelve un objeto iterable (puede utilizarse en bucles) comupuestos por todos los elementos del diccionario 

print("Elemento iterable (items): ".diassemanaingles.items())

#keys: devuelve un objeto iterable, puede utilizarse en bucles, compuesto por todas las claves del diccionario.

print("Elemento iteable (claves): ",diassemanaingles.keys())

# values: devuelve un obejto iterable,compuesto por todos los valores del diccionario

print("Elemento iterable (valores): ",diassemanaingles.values())

# clear: elimina todos los elementos del diccionario.

print("Diccionario después del clear: ", diassemanaingles.clea())
















