fin = False
print ("""*****************
calculadora de %
*****************""")
while not(fin):
    fin2 = False
    user_input1 = float(input ("Pon el número del que quieras hacer el tanto por \
ciento:\n"))
    user_input2 = float(input ("¿Qué tanto por ciento quieres calcular?\n"))
    resultado = (user_input1 * user_input2) / 100
    print ("El resultado es ",(round(resultado, 3)))
    user_input3 = input ("¿Quieres sumar o restar el tanto por ciento al total?\n\
Escribe + o -: ")
#suma el % al total

    if user_input3 == "+":
        print ("El total más el tanto por ciento es:", user_input1 + resultado)
        print ("Operación terminada")
        while not(fin2):
            userinput4 = input("¿Quieres calcular algún número más?\nEscribe 's' o 'n': ").lower()
            if userinput4 == "n":
                print("Adiós! ;-)")
                fin2 = True
                fin = True
            elif userinput4 == "s":
                fin2 = True
                print ("""***************
nueva operación
***************""")
                fin2 = True
          #resta el % al total  
    elif user_input3 == "-":
        print ("El total menos el tanto por ciento es:", user_input1 - resultado)
        print ("Operación terminada")
        while not(fin2):
            userinput4 = input("¿Quieres calcular algún número más?\nEscribe 's' o 'n': ").lower()
            if userinput4 == "n":
                print("Adiós! ;-)")
                fin = True
                fin2 = True
            elif userinput4 == "s":
                print ("""***************
nueva operación
***************""")
                fin2 = True
    else:
        print ("Operación terminada")
        print("Adiós! ;-)")
        fin = True
