numeros_ganadores = input("Introduce los números ganadores separados por espacios: ")
numeros_ganadores = numeros_ganadores.split() 
numeros_ganadores = [int(numero) for numero in numeros_ganadores]   
numeros_ganadores.sort()

print("Números ganadores ordenados de menor a mayor:")
for numero in numeros_ganadores:
    print (numero)

#prueba de codigo, commit ramas