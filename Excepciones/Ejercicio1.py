'''Localiza el error en el siguiente bloque de código.
 Crea una excepción para evitar que el programa se bloquee'''



try: 
    a = int(input("por favor inserte un numero: ")) #insertando el primer dato
    b = int(input("por favor inserte un numero: ")) #insertando el segundo dato   
except TypeError:
    print("Solo inserta numeros") #imprimir advertencia de error

try: 
  print(a/b)    
except ZeroDivisionError:
    print("La division por cero no es correcta") #imprimir advertencia de error


