'''Crear un programa en python que mediante el uso de funciones multiplique dos numeros, solamente usando sumas'''

num1 = int(input("Indique el numero a multiplicar: "))
num2 = int(input("Indique el numero de veces a multiplicar: "))


def multisuma(num1,num2):
    producto = 0
    for i in range (1,num2 + 1):
        producto = producto + num1
    print(("Producto de las sumas :"),(producto))
# print (("Producto"),(producto))

multisuma(num1,num2)






