'''Crear programa en python que devuelva el valor absoluto de cualquier valor'''

numero = int(input("Ingresar numero: "))

def absoluto (numero):
    absnum = 0
    absnum = abs(numero)
    return absnum

print (("El valor absoluto del numero es :"), absoluto(numero))
    