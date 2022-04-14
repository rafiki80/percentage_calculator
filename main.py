from art import banner
import os


def clear_console():
    os.system('clear')


def first_calc(a, b):
    resultado = (a * b) / 100
    print(f"El {b} por ciento de {a} es: {resultado}")
    return resultado


def new_operation():
    fin2 = False
    while not fin2:
        userinput4 = input("""Quieres hacer alguna operación más? \nContesta S o N: """)
        userinput4 = userinput4.lower()
        if userinput4 == "n":
            clear_console()
            print(banner)
            print("Adiós!! ;-)")
            fin2 = True
            return True
        elif userinput4 == "s":
            fin2 = True
            clear_console()


fin = False
while not fin:
    print(banner)
    userinput1 = float(input("Escribe el total del que quieras sacar un tanto por ciento: \n"))
    userinput2 = float(input("Tanto por ciento a calcular:\n"))

    per_cent = first_calc(userinput1, userinput2)
    userinput3 = input("¿Sumar o restar al total? Escribe + o -: ")
    if userinput3 == "+":
        print("La suma es:", userinput1 + per_cent)
        print("Operación terminada")
        fin = new_operation()

    elif userinput3 == "-":
        print("La resta es:", userinput1 - per_cent)
        print("Operación terminada")
        fin = new_operation()

    else:
        print("Operación terminada")
        fin = new_operation()
