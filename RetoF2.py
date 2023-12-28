def calculadora_salario():#Definiendo la funcion calculadora de salario
    nombre = input("Ingrese su nombre: ")#Variable para guardar el nombre del trabajador
    cantidad_hora = int(input("Ingrese la cantidad de horas laboradas: "))#Declarando variable para guardar la cantidad de horas trabajadas por el empleado
    if cantidad_hora <36 :#Verificando que la cantidad de horas no sea menor a 36 horas semanales
        print("Un trabajador no puede tener menos de 36 horas trabajadas")
        return
    else:
        valor_hora = int(input("Ingrese el valor por hora trabajada: "))#Declarando el valor de la hora trabajada
        '''if valor_hora <= 0:
            print("Por favor ingresar un valor mayor que cero")'''
        incremento_hora_extra = 0.25 #Declarando porcentaje de recargo a la hora extra
    if valor_hora <= 0:#Verificando que el valor de la hora no sea menor que cero       
        print("Por favor ingresar un valor mayor que cero")
        return
    else:
        if cantidad_hora < 36 :#Verificando que el valor de las horas no sea menor que 36 
            print(f"El trabajador- {nombre} no cumple con las horas minimas laboradas.")#indicando incumplimiento en horas laboradas
            return
        else:
            if cantidad_hora == 36:#calculando valores cuando no tiene recargos (Horas extra)
                Salario = valor_hora * cantidad_hora #Calculando salario neto
                print(f"Señor@ {nombre}.")
                print (f"Su salario trabajado es:{Salario} ")
            elif cantidad_hora > 36: #Calculando valores cuando el trabajador tiene recargos (Horas Extra)
                horasextra = cantidad_hora - 36 #calculando cuantas horas extra trabajo
                Recargo = (valor_hora * horasextra) * incremento_hora_extra #calculando recargo
                salario_final_extra = (valor_hora * horasextra) + Recargo #Calculando valor completo por horas extras
                Salario_Neto = salario_final_extra + (36 * valor_hora) #calculando salario Neto con recargos
                print(f"Señor {nombre}.")
                print(f"su pago es : ${Salario_Neto:,.2f}")
calculadora_salario()

