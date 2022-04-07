from art import banner

print(banner)


def first_calc():
    resultado = (userinput2 * userinput1) / 100
    print("El", userinput2, "tanto por ciento de", userinput1, "es:", resultado)
    return resultado


userinput1 = float(input("Escribe el total del que quieras sacar un tanto por ciento: \n"))
userinput2 = float(input("Tanto por ciento a calcular:\n"))

fin = False
while not fin:
    fin2 = False
    per_cent = first_calc()
    userinput3 = input("¿Sumar o restar al total? Escribe + o -: ")
    if userinput3 == "+":
        print("La suma es:", userinput1 + per_cent)
        print("Operación terminada")
        while not fin2:
            userinput4 = input("""Quieres hacer alguna operación más? \nContesta S o N: """)
            if userinput4 == "n":
                print("Adiós!! ;-)")
                fin2 = True
                fin = True
            elif userinput4 == 's':
                fin2 = True

    elif userinput3 == "-":
        print("La resta es:", userinput1 - per_cent)
        print("Operación terminada")
        while not fin2:
            userinput4 = input("""Quieres hacer alguna operación más? \nContesta S o N: """)
            if userinput4 == "n":
                print("Adiós!! ;-)")
                fin2 = True
                fin = True
            elif userinput4 == 's':
                fin2 = True
    else:
        print("Operación terminada")
        userinput4 = input("""Quieres hacer alguna operación más? \nContesta S o N: """)
        if userinput4 == "n":
            print("Adiós!! ;-)")
            fin = True
