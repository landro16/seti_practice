'''Escriba un programa en python que ingrese un numero y lo duplice'''

num = int(input("Ingresar numero a duplicar: ")) #Insertar por consola el valor a duplicar

def duplicar (num): #definiendo la funcion duplicar (recibe argumento num)
    total = num * 2    #ejecutando operacion multiplicando el valor num x 2
    print (("El doble del numero es: "), (total)) #imprimiendo resultado

duplicar(num) #invocando funcion
