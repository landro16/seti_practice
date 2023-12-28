def descuentos(): #Se crea una funcion para calcular los descuentos
    Precio_Articulos = int(input("Ingrese el precio de sus productos: "))#insertando valor de los articulos del cliente
    if Precio_Articulos <= 0:#verificando que el valor no sea menor a cero
        print("Por favor, ingresar un valor mayor a cero ")
        return
    else:
        if Precio_Articulos <= 150000:#Comprobando descuento para valores menores a 150.000
            print("No aplican descuentos para su compra")
            print(f"Su compra tiene un valor total de: ${Precio_Articulos:,.2f}")#indicando valor total de la compra
            
        elif Precio_Articulos > 150000 and Precio_Articulos <= 250000:#Verificando que el valor de los articulos se encuentren en el rango correcto entre 150.000 y 250.000
            descuento1 = 0.05#descuento autorizado para el rango definido
            Valordescuento1 = Precio_Articulos * descuento1#calculando el valor neto del descuento
            valortotal1 = Precio_Articulos - Valordescuento1 #Calculando valor total a pagar 
            print("Su compra tiene un descuento del 5%")
            print(f"Su compra tiene un valor sin descuento de: ${Precio_Articulos:,.2f} pesos")#indicando el valor de compra sin descuento
            print(f"El valor del descuento es: ${Valordescuento1:,.2f} pesos")
            print(f"El precio que debe pagar usted es de: {valortotal1:,.2f} pesos")

        elif Precio_Articulos > 250000 and Precio_Articulos <= 500000:#verificando rango entre 250000 y 500000
            descuento2 = 0.07#Indicando valor de descuento para el rango definido
            Valordescuento2 = Precio_Articulos * descuento2 #Calculando valor del descuento
            valortotal2 = Precio_Articulos - Valordescuento2 #Calculando valor total a pagar
            print("Su compra tiene un descuento del 7%")
            print(f"Su compra tiene un valor sin descuento de: ${Precio_Articulos:,.2f} pesos")
            print(f"El valor del descuento es: ${Valordescuento2:,.2f} pesos")
            print(f"El precio que debe pagar usted es de: {valortotal2:,.2f} pesos")  

        elif Precio_Articulos > 500000 and Precio_Articulos <= 800000:#Verificando que el valor de los articulos se encuentren en el rango correcto entre 500.000 y 800.000
            descuento3 = 0.09 #idnicando valor descuento para el rango definido
            Valordescuento3 = Precio_Articulos * descuento3 #calculando valor descuento
            valortotal3 = Precio_Articulos - Valordescuento3 #Calculando valor total a pagar
            print("Su compra tiene un descuento del 9%")
            print(f"Su compra tiene un valor sin descuento de: ${Precio_Articulos:,.2f} pesos")
            print(f"El valor del descuento es: ${Valordescuento3:,.2f} pesos")
            print(f"El precio que debe pagar usted es de: {valortotal3:,.2f} pesos")

        elif Precio_Articulos > 800000: #Verificando que el valor este por encima de los 800.000
            descuento4 = 0.12 #definiendo descuento para el valor designado
            Valordescuento4 = Precio_Articulos * descuento4 #calculando valor del descuento
            valortotal4 = Precio_Articulos - Valordescuento4 #Calculando valor total a pagar
            print("Su compra tiene un descuento del 12%")
            print(f"Su compra tiene un valor sin descuento de: ${Precio_Articulos:,.2f} pesos")
            print(f"El valor del descuento es: ${Valordescuento4:,.2f} pesos")
            print(f"El precio que debe pagar usted es de: {valortotal4:,.2f} pesos")          
descuentos()
