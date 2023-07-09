# Probando los metodos listas
frutas = ['manzana', 'banana', 'cereza', 'naranja']

# Obtener la longitud de la lista
print("Longitud de la lista:", len(frutas))

# Acceder a elementos de la lista por índice
print("Primer elemento:", frutas[0])
print("Último elemento:", frutas[-1])

# Agregar un elemento al final de la lista
frutas.append('uva')
print("Lista después de agregar 'uva':", frutas)

# Insertar un elemento en una posición específica
frutas.insert(2, 'pera')
print("Lista después de insertar 'pera' en la posición 2:", frutas)

# Eliminar un elemento de la lista por valor
frutas.remove('banana')
print("Lista después de eliminar 'banana':", frutas)

# Eliminar un elemento de la lista por índice
elemento_eliminado = frutas.pop(1)
print("Elemento eliminado:", elemento_eliminado)
print("Lista después de eliminar el elemento en la posición 1:", frutas)

# Revertir el orden de la lista
frutas.reverse()
print("Lista después de revertir el orden:", frutas)

# Ordenar la lista en orden ascendente
frutas.sort()
print("Lista ordenada en orden ascendente:", frutas)

# Verificar si un elemento está en la lista
if 'manzana' in frutas:
    print("'manzana' está en la lista")
else:
    print("'manzana' no está en la lista")
