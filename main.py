import numpy as np
import pandas as pd
from os import system
import matplotlib.pyplot as plt
import seaborn as sns



# Funcion para generar ID random de 4 digitos de numeros del 1 al 9
def generarID():
    id = ""
    for i in range(4):
        num = str(np.random.randint(1, 10))
        id += num
    return id

def generarIDlib():
    id = ""
    for i in range(5):
        num = str(np.random.randint(1, 10))
        id += num
    return id


def depWhileInt(cond1, cond2, message = ""):
    valor = depInt(message)
    while valor < cond1 or valor > cond2:
        system("cls")
        print("El valor ingresado no es valido, por favor ingresalo de nuevo.\n")
        valor = depInt(message)
    return valor


def depInt(mensaje=""):
    while True:
        try:
            temp = int(input(mensaje))
            break
        except:
            print("Dato no valido, por favor ingresa otro.\n")
            system("cls")
    return temp


class Seguridad:
    def __init__(self):
        with open("Contra.txt") as file:
            temporal = file.readlines()
            contra = ""
            for x in temporal:
                contra += x

        self.contra = contra
    #verificar ontraseña
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
    #cambio de contraseña
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
        self.menuPrincipal = "1) Miembros\n2) Libros\n3) Datos Financieros\n4) Cambiar contrasenia\n5) Salir\n\n"

        self.Work()

    # Programa y menu principal
    def Work(self):
        system("cls")
        while True:
            opcion = depInt(self.menuPrincipal + "Ingresa una opcion del menu: ")

            if opcion == 1:  #1) Miembros
                system("cls")
                self.Miembros()
            elif opcion == 2:  #2) Libros
                system("cls")
                self.Libros()
            elif opcion == 3:
                system("cls")
                self.dFin()   #)Datos financieros
            elif opcion==4:
                system("cls")
                self.seguridad.cambiarContra()
            elif opcion == 5:
                print("\nSaliendo del programa")
                break
            else:
                system("cls")
                continue


    # Funciones de miembros
    def Miembros(self):
        while True:
            #menú de la opcion 1)miembros
            opcion1 = depWhileInt(1,6,"1) Agregar Miembros\n2) Lista de Miembros\n3) Actualizar Membresia\n4) Cancelar suscripcion\n5) Frecuencia de las membresias\n6) Salir\n\nIngresa una opcion del menu: ")
            system("cls")
            # Agregar miembro
            if opcion1 == 1:
                print("\n") #Agregar miembros
                # ingresar datos del usuario
                id = generarID()
                nombre = input("Ingresa el nombre del nuevo miembro: ")
                numero = depInt("Ingresa el numero del telefono del nuevo miembro: ")
                print("\n1) Standard  $50 MXN\n2) Premium $100 MXN\n3) VIP $150MXN\n")
                print("Este cargo sera mensual, y los beneficios entre una membresia y otra son el poder rentar libros por mas tiempo.\n")
                membresia = input("Ingresa una membresia del menu: ").lower()

                while membresia != "standard" and membresia != "premium" and membresia != "vip":
                    system("cls")
                    print("\nOpcion no valida.")
                    print("\n1) Standard  $50 MXN\n2) Premium $100 MXN\n3) VIP $150MXN\n")
                    membresia = input("Elija una membresia del menu: ").lower()

                if membresia == "standard":
                    pago = 50
                elif membresia == "premium":
                    pago = 100
                else:
                    pago = 150

                self.modificarIngresos(pago)
                # Abrimos el csv de los miembros donde la columna sea unnamed
                df_agregar = pd.read_csv("Miembros.csv", index_col= "Unnamed: 0")
                nuevoMiembro = {'ID': id, 'Nombre': nombre,"Celular": numero, 'Membresia': membresia, 'Pago': pago, 'Libro': "0"}
                df_agregar = df_agregar.append(nuevoMiembro, ignore_index=True)
                df_agregar.to_csv("Miembros.csv")
            elif opcion1 == 2:
                # Lista de miembros
                df = pd.read_csv("Miembros.csv", index_col="ID")
                if df[1:].empty:
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                else:
                    df.drop('Unnamed: 0', axis=1, inplace=True)
                    print(df[1:].to_string())
            elif opcion1 == 3: # Actualizar membresia
                df = pd.read_csv("Miembros.csv")
                df_copia = pd.read_csv("Miembros.csv")
                df_copia.set_index('ID', inplace=True)
                df_copia.drop("Unnamed: 0", axis = 1, inplace=True)
                if df[1:].empty:
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                    continue

                while True:
                    idcambiar = depInt("Ingresa el ID del miembro: ")
                    try:
                        print("\n" + df_copia.loc[idcambiar].to_string())
                    except KeyError:
                        print("Este ID no existe porfavor verificalo.\n")
                        system("pause")
                        system("cls")
                        continue
                    opcion = depWhileInt(1, 2, "\nPorfavor confirma que esa es tu cuenta.\n1) Si  2)No: ")
                    if opcion == 1:
                        break
                    else:
                        print("\nPorfavor checa el ID en tu credencial que se te dio.\n")
                        system("pause")
                        system("cls")

                df.set_index('ID', inplace=True)

                if df.loc[idcambiar,"Membresia"] == "vip":
                    print("Tu membresia ya es VIP. No puedes mejorarla mas.")
                    continue
                elif df.loc[idcambiar,"Membresia"] == "premium": # Actualizar de premium a vip
                    opcion = depWhileInt(1, 2, "\n¿Seguro que quieres mejorar tu membresia a VIP? Se te cobrarian $50 MXN.\n\n1) Si  2)No: ")
                    if opcion == 1:
                        df.loc[idcambiar, "Membresia"] = "vip"
                        df.loc[idcambiar, "Pago"] = 150
                        #remplaza a la función with open
                        self.modificarIngresos(50)

                        df.reset_index(inplace=True)
                        df.drop("Unnamed: 0", axis = 1, inplace=True)
                        df.to_csv("Miembros.csv")
                else:
                    opcion = depWhileInt(1, 2, "\n¿Que membresia nueva quieres?\n\nSi eliges VIP serian $100 MXN.\nSi eliges Premium serian $50 MXN.\n1) VIP  2)Premium: ")

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

                    self.modificarIngresos(cargo)

                    df.reset_index(inplace=True)
                    df.drop("Unnamed: 0", axis=1, inplace=True)
                    df.to_csv("Miembros.csv")
            elif opcion1 == 4: #Cancelar suscripcion
                df = pd.read_csv("Miembros.csv")
                if df[1:].empty:
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                    continue

                dfTemp  = pd.read_csv("Miembros.csv", index_col = "ID")
                dfTemp.drop("Unnamed: 0", axis=1, inplace=True)

                while True:
                    idborrar = depInt("Ingresa el ID del miembro a eliminar: ")
                    try:
                        print("\n" + dfTemp.loc[idborrar].to_string())
                    except KeyError:
                        print("\nEste ID no existe porfavor verificalo.\n")
                        system("pause")
                        system("cls")
                        continue
                    opcion = depWhileInt(1, 2,"\nPorfavor confirma que esa es tu cuenta.\n1) Si  2)No: ")
                    if opcion == 1:
                        break
                    else:
                        print("\nPorfavor checa el ID en tu credencial que se te dio.\n")


                print("")
                opcion = depWhileInt(1, 2, "\nEsta accion es irreversible.¿Estas seguro?\n1) Si  2)No: ")
                if opcion == 1:
                    df.drop(df.loc[df['ID']==idborrar].index, inplace=True)
                    df.drop("Unnamed: 0", axis=1, inplace=True)
                    df.to_csv("Miembros.csv")
                else:
                    system("cls")
                    continue
            elif opcion1 == 5: #Frecuencia de membresias
                df = pd.read_csv("Miembros.csv")
                df = df[1:]
                moda = df['Membresia'].mode()[0]
                sns.set(color_codes=True)
                sns.countplot(x = "Membresia", data = df,palette="Spectral")
                plt.title(label = "La frecuencia de nuestras membresias\nModa: " + str(moda))
                plt.show()
            elif opcion1 == 6: #Salir
                system("cls")
                break
            else:
                continue
            print()
            system("pause")
            system("cls")

    def Libros(self):
        while True:
            opcion2 = depWhileInt(1,6,"1) Añadir libro\n2) Mostrar Catalogo\n3) Rentar libro\n4) Regresar un libro\n5) Fecuencia genero de los libros\n6) Salir\n\nIngresa una opcion del menu: ")
            system("cls")
            if opcion2==1:
                id=generarIDlib()
                nombre = input("Ingresa el nombre del nuevo Libro: ")
                print()
                genero = depWhileInt(1,7,"\n1) Manga\n2) Ciencia ficcion\n3) Novela\n4) Policiaco\n5) Fantasia\n6) Aventura\n7) Cuentos de hadas\n\nSelecciona un género: ")
                if genero == 1:
                    genero = 'Manga'
                elif genero == 2:
                    genero = 'Ciencia ficcion'
                elif genero == 3:
                    genero = 'Novela'
                elif genero == 4:
                    genero = 'Policiaco'
                elif genero == 5:
                    genero = 'Fantasia'
                elif genero == 6:
                    genero = 'Aventura'
                else:
                    genero = 'Cuentos de hadas'
                autor = input("Ingresa el nombre del autor del libro: ")
                renta = "No"
                df_agregar = pd.read_csv("Libros.csv", index_col= "Unnamed: 0")
                nuevoLibro = {'ID': id, 'Nombre Libro': nombre,'Genero': genero, 'Autor':autor, 'Rentado': renta}
                df_agregar = df_agregar.append(nuevoLibro, ignore_index=True)
                df_agregar.to_csv("Libros.csv")
            elif opcion2==2:
                df = pd.read_csv("Libros.csv")
                selec = depWhileInt(1,2,"Elija si quiere ver.\n1) Catalogo completo.\n2) Algun genero en especifico: ")
                if selec == 1:
                    system("cls")
                    print("Estos son los libros que tenemos disponibles: ")
                    df.drop("Unnamed: 0", axis=1, inplace=True)
                    df.set_index('ID', inplace=True)
                    print("\n" + df.to_string())
                elif selec == 2:
                    gen_esp = depWhileInt(1,7,"\n1) Manga\n2) Ciencia ficcion\n3) Novela\n4) Policiaco\n5) Fantasia\n6) Aventura\n7) Cuentos de hadas\n\nSelecciona el genero que guste revisar:")
                    if gen_esp == 1:
                        genero1 = "Manga"
                    elif gen_esp == 2:
                        genero1 = "Ciencia ficcion"
                    elif gen_esp == 3:
                        genero1 = "Novela"
                    elif gen_esp == 4:
                        genero1 = "Policiaco"
                    elif gen_esp == 5:
                        genero1 = "Fantasia"
                    elif gen_esp == 6:
                        genero1 = "Aventura"
                    elif gen_esp == 7:
                        genero1 = "Cuentos de hadas"
                    system("cls")
                    print(f"Usted eligio: {genero1}. Estas son las opciones que tenemos: ")
                    df.drop("Unnamed: 0", axis=1, inplace=True)
                    df.set_index('ID', inplace=True)
                    print("n" + df[df['Genero'] == genero1].to_string())
            elif opcion2==3:
                df = pd.read_csv("Libros.csv")
                gen_ren = depWhileInt(1,7,"1) Manga\n2) Ciencia ficcion\n3) Novela\n4) Policiaco\n5) Fantasia\n6) Aventura\n7) Cuentos de hadas\n\nSelecciona un genero: ")

                if gen_ren == 1:
                    genero = "Manga"
                elif gen_ren == 2:
                    genero = "Ciencia ficcion"
                elif gen_ren == 3:
                    genero = "Novela"
                elif gen_ren == 4:
                    genero = "Policiaco"
                elif gen_ren == 5:
                    genero = "Fantasia"
                elif gen_ren == 6:
                    genero = "Aventura"
                elif gen_ren == 7:
                    genero = "Cuentos de hadas"

                df.drop("Unnamed: 0", axis=1, inplace=True)
                df.set_index('ID', inplace=True)

                df_miembros = pd.read_csv("Miembros.csv")

                if df_miembros[1:].empty:
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                    system("pause")
                    system("cls")
                    continue

                df_miembros.set_index("ID",inplace=True)

                id_personita = depInt("Ingresa tu ID para completar el registro: ")

                try:
                    if df_miembros.loc[id_personita, "Libro"] != 0:
                        print("Usted ya tiene un libro rentado. Si desea rentar otro libro, devuelva el anterior.\n")
                        system("pause")
                        system("cls")
                        continue
                except KeyError:
                    print("El ID que ingreso no existe. Por favor vuelva a intentarlo.\n")
                    system("pause")
                    system("cls")
                    continue

                while True:
                    system("cls")
                    id_lib = depInt(df[(df['Genero'] == genero) & (df['Rentado'] == 'No')].to_string() + "\n\nElija el ID del libro que desea rentar: ")
                    try:
                        df.loc[id_lib, "Rentado"] = 'Si'
                        df.reset_index(inplace=True)
                        df_miembros.loc[id_personita, "Libro"] = id_lib
                        df_miembros.drop("Unnamed: 0",axis=1,inplace=True)
                        df_miembros.reset_index(inplace=True)
                        df.to_csv("Libros.csv")
                        df_miembros.to_csv("Miembros.csv")
                        break
                    except KeyError:
                        print("Este ID no existe.\nIngresa algo valido.")
                    except ValueError:
                        print("Este ID no existe.\nIngresa algo valido.")
            elif opcion2==4:
                df_miembros = pd.read_csv("Miembros.csv")
                df_libros = pd.read_csv("Libros.csv")
                df_miembros.set_index("ID", inplace=True)
                df_libros.set_index("ID",inplace=True)

                if df_miembros[1:].empty:
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                    continue

                id_personita= depInt("Ingresa tu ID: ")
                try:
                    if df_miembros.loc[id_personita,"Libro"] == 0:
                        print("No tienes libros rentados.")
                        system("pause")
                        system("cls")
                        continue
                except KeyError:
                    print("El ID no existe. Por favor vuelva a intentarlo.")
                    system("pause")
                    system("cls")
                    continue

                idLibro = df_miembros.loc[id_personita,"Libro"]
                df_libros.loc[idLibro,"Rentado"]="No"
                df_miembros.loc[id_personita,"Libro"]=0
                df_miembros.drop("Unnamed: 0",axis=1, inplace=True)
                df_miembros.reset_index(inplace=True)
                df_libros.drop("Unnamed: 0",axis=1, inplace=True)
                df_libros.reset_index(inplace=True)
                print("\nEl libro ha sido devuelto con exito en el sistema.")
                df_libros.to_csv("Libros.csv")
                df_miembros.to_csv("Miembros.csv")
            elif opcion2==5:
                df = pd.read_csv("Libros.csv")
                sns.set(color_codes=True)
                plt.figure(figsize=(9, 7))
                sns.countplot(x="Genero", data=df, palette="Spectral", hue = "Rentado")
                plt.title(label="Frecuencia de los libros")
                plt.show()
            elif opcion2==6:
                system("cls")
                break
            else:
                system("cls")
                continue
            print()
            system("pause")
            system("cls")

    def dFin(self):
        while True:
            opcion3 = depWhileInt(1,3, "1) Ingresos\n2) Utilidades\n3) Salir\n\nIngresa una opcion del menu: ")
            if opcion3==1:
                df_gan=pd.read_csv("Miembros.csv", index_col= "Unnamed: 0")
                ganancia = df_gan.Pago.sum()

                with open("Ingresos.txt") as file:
                    temporal = file.readlines()
                    gastos = ""
                    for x in temporal:
                        gastos += x
                    ingresos = float(gastos)

                ganancia = ganancia + ingresos

                df_gan = df_gan[1:]
                sns.set(color_codes=True)
                plt.figure(figsize=(9, 7))
                df_gan.groupby("Membresia")["Pago"].sum().plot(kind="bar")
                plt.title(label="Ingresos por membresia\nLos ingresos del mes son: " + str(ganancia) + "$")
                plt.show()
            elif opcion3==2:
                gasto_luz = 100
                gasto_agua = 170
                gasto_renta = 199

                df_gan = pd.read_csv("Miembros.csv", index_col="Unnamed: 0")
                ganancia = df_gan.Pago.sum()

                with open("Ingresos.txt") as file:
                    temporal = file.readlines()
                    gastos = ""
                    for x in temporal:
                        gastos += x
                    ingresos = float(gastos)

                ganancia = ganancia + ingresos
                utilidades = ganancia - gasto_luz - gasto_agua - gasto_renta
                system("cls")
                print(f"El gasto de luz este mes fue de ${gasto_luz}")
                print(f"El gasto de agua de este mes fue de ${gasto_agua}")
                print(f"El gasto de la renta este mes fue de ${gasto_renta}")

                if utilidades<=0:
                    print("Esta teniendo perdidas.")
                    print(f"La utilidad de este mes es de: ${utilidades}")
                else:
                    print(f"La utilidad de este mes es de: ${utilidades}")
            elif opcion3 == 3:
                system("cls")
                break
            else:
                continue
            print()
            system("pause")
            system("cls")


    def modificarIngresos(self,cargo):
         with open("Ingresos.txt") as file:
             temporal = file.readlines()
             gastos = ""
             for x in temporal:
                 gastos += x

             gastos = float(gastos)
             gastos += cargo

         with open("Ingresos.txt", "w") as file:
             file.write(str(gastos))


biblioteca = Administrador()




