'''verificar una excepcion 3 veces, si a la tercera se comente el mismo error terminar el programa'''


def division (): #definimos la funcion dividir
    div = num1/num2
    print (("Resultado"), (div))

condicion =0
while condicion <3:
    try:
        
        num1 = int(input("Ingrese el primer numero"))
        num2 = int(input("Ingrese el segundo numero"))
        division() #invocando funcion dividir
    except TypeError:
        print("por favor ingresar numeros y no cadena")
        condicion +=1
    except ValueError:
        print("Por favor ingresar numeros")
        condicion +=1
    except ZeroDivisionError:
        print("La division por cero no es posible!! vuelve a intentarlo")
        condicion +=1       