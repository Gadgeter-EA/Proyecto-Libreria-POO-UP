'''
Ideas de proyecto: (acomodo)
Pantalla:
1) Agregar miembro
     Membresías (cuando usuario quiera cambiarlo)
     Cancelar suscripcion
3) Rentar libro
5) Datos financieros
     Dinero generado
6) Regresar libro
7) Agregar libro (inventario)
8) Información

Pagos constantes: Las membresias
Pagos "de la nada" (multa, suscripcion update)
'''

import numpy as np
import pandas as pd
from os import system


# Funcion para generar ID random de 4 digitos de numeros del 1 al 9
def generarID():
    id = ""
    for i in range(4):
        num = str(np.random.randint(1, 10))
        id += num
    return id


def depWhileInt(cond1, cond2, message = ""):
    valor = depInt(message)
    while valor < cond1 or valor > cond2:
        print("\nEl valor ingresado no es valido, por favor ingresalo de nuevo.")
        valor = depInt(message)
    return valor


def depInt(mensaje=""):
    while True:
        try:
            temp = int(input(mensaje))
            break
        except:
            print("Dato no valido, por favor ingresa otro.\n")
    return temp


class Seguridad:
    def __init__(self):
        with open("Contra.txt") as file:
            temporal = file.readlines()
            contra = ""
            for x in temporal:
                contra += x

        self.contra = contra

    def validarContra(self):
        if self.contra != "":
            intentos = 1
            contrau = input("Ingresa la contrasenia: ")

            while True:
                if self.contra == contrau:
                    break
                elif intentos >= 3:
                    print("Superaste el límite de 3 intentos.\nPor seguridad el sistema se bloqueara.\n")
                    exit()
                else:
                    print("Contraseña incorrecta, te quedan", (3 - intentos), "intento(s)")
                    contrau = input("Ingresa la contrasenia: ")
                    intentos += 1

    def cambiarContra(self):
        self.validarContra()
        system("cls")
        newcontra = input("Ingresa la contraseña nueva: ")

        system("cls")
        print("Esta sera la contraseña del dipostivo a partir de ahora:", newcontra, "\nRecuerdala.")
        system("pause")

        with open("Contra.txt", "w") as file:
            file.write(newcontra)
        system("cls")
        print("¡La contraseña a sido modificada con exito!")
        system("pause")
        system("cls")


# programa principal
class Administrador:
    def __init__(self):
        self.seguridad = Seguridad()
        self.seguridad.validarContra()
        # system("cls")
        self.menuPrincipal = "1) Miembros\n2) Libros\n3) Datos Financieros\n4) Salir\n\n"
        self.Work()

    # Programa y menu principal
    def Work(self):
        print(self.menuPrincipal)
        opcion = depInt("Ingresa una opcion del menu: ")

        if opcion == 1:
            self.Miembros()

    # Funciones de miembros
    def Miembros(self):
        while True:
            print("\n1) Agregar Miembros\n2) Lista de Miembros\n3) Actualizar Membresia\n4) Cancelar suscripcion\n5) Salir\n\n")
            opcion1 = depInt("Ingresa una opcion del menu: ")
            # Agregar miembro
            if opcion1 == 1:
                print("\n")

                id = generarID()
                nombre = input("Ingresa el nombre del nuevo miembro: ")
                numero = depInt("Ingresa el numero del telefono del nuevo miembro: ")
                print("\n1) Standard  $50 MXN\n2) Premium $100 MXN\n3) VIP $150MXN\n")
                print("Este cago sera mensual, y los beneficios entre una membresia y otra son el poder rentar más libros a la vez.\n")
                membresia = input("Ingresa una membresia del menu: ").lower()

                while membresia != "standard" and membresia != "premium" and membresia != "vip":
                    print("\nOpcion no valida.")
                    print("\n1) Standard  $50 MXN\n2) Premium $100 MXN\n3) VIP $150MXN\n")
                    membresia = input("Elija una membresia del menu: ").lower()

                if membresia == "standard":
                    pago = 50
                elif membresia == "premium":
                    pago = 100
                else:
                    pago = 150

                # Abrimos el csv de los miembros donde la columna sea unnamed
                df_agregar = pd.read_csv("Miembros.csv", index_col= "Unnamed: 0")
                nuevoMiembro = {'ID': id, 'Nombre': nombre,"Celular": numero, 'Membresia': membresia, 'Pago': pago}
                df_agregar = df_agregar.append(nuevoMiembro, ignore_index=True)
                df_agregar.to_csv("Miembros.csv")
            elif opcion1 == 2:
                # Lista de miembros
                df = pd.read_csv("Miembros.csv", index_col="ID")
                if df[1:].empty:
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                else:
                    df.drop('Unnamed: 0', axis=1, inplace=True)
                    print(df[1:])
            elif opcion1 == 3: # Actualizar membresia
                df = pd.read_csv("Miembros.csv")
                df_copia = pd.read_csv("Miembros.csv")
                df_copia.drop("Unnamed: 0", axis = 1, inplace=True)
                if df[1:].empty:
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                    continue

                while True:
                    idcambiar = depInt("Ingresa el ID del miembro: ")
                    try:
                        df_copia.set_index('ID', inplace=True)
                        print(df_copia.loc[idcambiar])
                        print("\nPorfavor confirma que esa es tu cuenta.\n")
                    except KeyError:
                        print("\nEste ID no existe porfavor verificalo.\n")
                        continue
                    opcion = depWhileInt(1, 2, " 1) Si  2)No: ")
                    if opcion == 1:
                        break
                    else:
                        print("\nPorfavor checa el ID en tu credencial que se te dio.\n")

                df.set_index('ID', inplace=True)

                if df.loc[idcambiar,"Membresia"] == "vip":
                    print("Tu membresia ya es VIP. No puedes mejorarla mas.")
                    continue
                elif df.loc[idcambiar,"Membresia"] == "premium": # Actualizar de premium a vip
                    print("¿Seguro que quieres mejorar tu membresia a VIP? Se te cobrarian $50 MXN: ")
                    opcion = depWhileInt(1, 2, " 1) Si  2)No: ")
                    if opcion == 1:
                        df.loc[idcambiar, "Membresia"] = "vip"
                        df.loc[idcambiar, "Pago"] = 150
                        with open("Gastos.txt") as file:
                            temporal = file.readlines()
                            gastos = ""
                            for x in temporal:
                                gastos += x

                            gastos = float(gastos)
                            gastos += 50
                        
                        with open("Gastos.txt", "w") as file:
                            file.write(str(gastos))
                        df.reset_index(inplace=True)
                        df.drop("Unnamed: 0", axis = 1, inplace=True)
                        df.to_csv("Miembros.csv")
                else:
                    print("\n¿Que membresia nueva quieres?\nSi eliges VIP serian $100 MXN.\nSi eliges Premium serian $50 MXN.")
                    opcion = depWhileInt(1, 2, " 1) VIP  2)Premium: ")

                    if opcion == 1:
                        nuevamem = "vip"
                        cargo = 100
                        nuevoc = 150
                    else:
                        nuevamem = "premium"
                        cargo = 50
                        nuevoc = 100

                    df.loc[idcambiar, "Membresia"] = nuevamem
                    df.loc[idcambiar, "Pago"] = nuevoc

                    with open("Gastos.txt") as file:
                        temporal = file.readlines()
                        gastos = ""
                        for x in temporal:
                            gastos += x

                        gastos = float(gastos)
                        gastos += cargo

                    with open("Gastos.txt", "w") as file:
                        file.write(str(gastos))
                    df.reset_index(inplace=True)
                    df.drop("Unnamed: 0", axis=1, inplace=True)
                    df.to_csv("Miembros.csv")
            elif opcion1 == 4:  # Cancelar suscripcion
                df = pd.read_csv("Miembros.csv")
                if df[1:].empty:
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                    continue

                dfTemp  = pd.read_csv("Miembros.csv", index_col = "ID")
                dfTemp.drop("Unnamed: 0", axis=1, inplace=True)

                while True:
                    idborrar = depInt("Ingresa el ID del miembro a eliminar: ")
                    try:
                        print(dfTemp.loc[idborrar])
                        print("\nPorfavor confirma que esa es tu cuenta.\n")
                    except KeyError:
                        print("\nEste ID no existe porfavor verificalo.\n")
                        continue
                    opcion = depWhileInt(1, 2," 1) Si  2)No: ")
                    if opcion == 1:
                        break
                    else:
                        print("\nPorfavor checa el ID en tu credencial que se te dio.\n")


                print("\nEsta accion es irreversible.¿Estas seguro?\n")
                opcion = depWhileInt(1, 2, " 1) Si  2)No: ")
                if opcion == 1:
                    df.drop(df.loc[df['ID']==idborrar].index, inplace=True)
                    df.drop("Unnamed: 0", axis=1, inplace=True)
                    df.to_csv("Miembros.csv")
                else:
                    continue
            else:
                continue


# ---------------------------


biblioteca = Administrador()



