import numpy as np
import pandas as pd
from os import system
import matplotlib.pyplot as plt
import seaborn as sns

'''
Importamos todas las librerias necesarias
'''



# Funcion para generar ID random de 4 digitos de numeros del 1 al 9
def generarID():
    # Creamos un acumulador tipo string
    id = ""
    for i in range(4):
        # Generamos un numero entero de 1 a 9 que formara parte del ID
        num = str(np.random.randint(1, 10))
        # Concatenamos le numero generado
        id += num
    return id

# Funcion para generar ID random de 5 digitos de numeros del 1 al 9
def generarIDlib():
    id = ""
    for i in range(5):
        num = str(np.random.randint(1, 10))
        id += num
    return id

# 5 y 7, Ingresa un numero entre 5 y 7
def depWhileInt(cond1, cond2, message = ""):
    valor = depInt(message) #Le pedimos al ususario un numero entero
    while valor < cond1 or valor > cond2: # Si el numero que ingresa el usuario, no cumple las condiciones, entramos al bucle while
        system("cls") # Borramos lo que esta impreso en consola por limpeza, esto se mandara a llamar varias veces a lo largo del programa
        print("El valor ingresado no es valido, por favor ingresalo de nuevo.\n")
        valor = depInt(message)
    return valor

# Funcion que nos permite forzar al usuario a ingresar solo numeros enteros
def depInt(mensaje=""): # Podemos
    # Ciclo que se va a detener hasta el usuario ingresa un entero
    while True:
        # Try/ Except para evitar el problema mencionado arriba
        try:
            temp = int(input(mensaje)) # Le pedimos el numero entero al ususario
            break # Si no surge ningun error, rompemos el ciclo
        except:
            # Si ocurre alguna excepcion, imprimimos un mensaje de error en consola
            print("Dato no valido, por favor ingresa otro.\n")
            system("cls")
    return temp

# Creamos la clase seguridad que nos ayudara con la misma del sistema.
class Seguridad:
    def __init__(self): # Creamos el constructor
        # Todo esto se ejecutra cuando se cree un objeto de la clase seguridad
        with open("Contra.txt") as file: # Abrimos el txt contra, en donde esta almacenada la contrasña del sistema
            temporal = file.readlines()
            contra = "" # Leemos la contraseña y creamos un acmulador de string
            for x in temporal: #Como el readlines() nos guarda la informacion en una lista, usamos este ciclo for para concatenarlo
                contra += x    # todo en contra
        # Creamos el atributo contra de la clase, que va a ser la contrasenia leida del txt
        self.contra = contra
    #verificar contraseña
    def validarContra(self):
        if self.contra != "": # Si el atributo contra es diferente de nada, quiere decir que hay contraseña
            intentos = 1 # Inicializamos el numero de intentos
            contrau = input("Ingresa la contrasenia: ")

            while True:
                if self.contra == contrau: #Checamos si la contraseña que ingreso que el ususario esta bien
                    break # Si es asi, rompemos el ciclo while y continuamos
                elif intentos >= 3:
                    print("Superaste el límite de 3 intentos.\nPor seguridad el sistema se bloqueara.\n")
                    exit()
                else:
                    print("Contraseña incorrecta, te quedan", (3 - intentos), "intento(s)")
                    contrau = input("Ingresa la contrasenia: ")
                    intentos += 1
    #cambio de contraseña
    def cambiarContra(self):
        self.validarContra() # Le pedimos la contraseña al usuario
        system("cls")
        newcontra = input("Ingresa la contrasenia nueva: ")

        system("cls")
        # Imprimimos la contraseña nueva que acaba de ingresar y le pedimos al usuario que la recuerde
        print("Esta sera la contrasenia del dipostivo a partir de ahora:", newcontra, "\nRecuerdala.")
        system("pause")

        with open("Contra.txt", "w") as file: # Abrimos el txt con w para sobrescribir la contrasenia actual
            file.write(newcontra) # Escribimos la nueva contraseña
        system("cls")
        print("¡La contraseña a sido modificada con exito!") # Informamos al usuario que todo bien
        system("pause")
        system("cls")


# programa principal que funciona mediante la clase administrador
class Administrador:
    def __init__(self):
        self.seguridad = Seguridad() # Creamos un objeto de la clase seguridad, en ese mismo instante leemos la contra del txt
        self.seguridad.validarContra() # Le pedimos al usuario que ingrese la contraseña del sistema, si falla los 3 intentos, se
        # system("cls")  # detendra la ejecucion del programa
        self.menuPrincipal = "1) Miembros\n2) Libros\n3) Datos Financieros\n4) Cambiar contrasenia\n5) Salir\n\n"

        self.Work() # Mandamos a llamar el menu principal donde estan las 4 opciones principales

    # Programa y menu principal
    def Work(self):
        system("cls")
        while True: # Hacemos un ciclo infinito que dure todo lo que quiera el usuario, esto funciona tambien para los submenus
            opcion = depInt(self.menuPrincipal + "Ingresa una opcion del menu: ") # Le pedimos un numero del menu al usuario

            if opcion == 1:  #1) Miembros
                system("cls")
                self.Miembros()
            elif opcion == 2:  #2) Libros
                system("cls")
                self.Libros()
            elif opcion == 3:   #3) Datos financieros
                system("cls")
                self.dFin()
            elif opcion==4:  #4) Cambiar contraseña
                system("cls")
                self.seguridad.cambiarContra()
            elif opcion == 5:
                print("\nSaliendo del programa. Hasta luego vuelva pronto.")
                break
            else:
                system("cls")
                continue


    # Funciones de miembros
    def Miembros(self):
        while True:
            #menú de la opcion
            opcion1 = depWhileInt(1,6,"1) Agregar Miembros\n2) Lista de Miembros\n3) Actualizar Membresia\n4) Cancelar suscripcion\n5) Frecuencia de las membresias\n6) Salir\n\nIngresa una opcion del menu: ")
            system("cls")
            # Agregar miembro
            if opcion1 == 1:
                print("\n") #Agregar miembros

                id = generarID() # Usamos funcion generar ID para crear un numero de 4 cifras
                nombre = input("Ingresa el nombre del nuevo miembro: ") # Le pedimos al usuario el nombre del nuevo miembro
                numero = depInt("Ingresa el numero del telefono del nuevo miembro: ") # Le pedimos su numero de telefono
                print("\n1) Standard  $50 MXN\n2) Premium $100 MXN\n3) VIP $150MXN\n") # Imprimimos las opciones de membresia e informacion sobre estas
                print("Este cargo sera mensual, y los beneficios entre una membresia y otra son el poder rentar libros por mas tiempo.\n")
                membresia = input("Ingresa una membresia del menu: ").lower() # La membresia que ingrese la usuario la convertimos al minisculas para evitar
                # problemas

                # While para verificar que membresia sea una opcion valida
                while membresia != "standard" and membresia != "premium" and membresia != "vip":
                    system("cls")
                    print("\nOpcion no valida.")
                    print("\n1) Standard  $50 MXN\n2) Premium $100 MXN\n3) VIP $150MXN\n")
                    membresia = input("Elija una membresia del menu: ").lower()

                # Dependiendo de la membresia que eligio el nuevo miembro, pago adquire un valor diferente
                if membresia == "standard":
                    pago = 50
                elif membresia == "premium":
                    pago = 100
                else:
                    pago = 150

                self.modificarIngresos(pago) # Usamos la funcion modificar ingresos para sumar la nueva cantidad que cobramos
                # Abrimos el csv de los miembros donde la columna sea unnamed
                # Abrimos el CSV como un DataFrame de  los miembros, en donde los indices sera la columna sin nombre para evitarnos problema despues
                # a la hora de sobrescibir  el archivo
                df_agregar = pd.read_csv("Miembros.csv", index_col= "Unnamed: 0")
                # Creamos un diccionario con toda la informacion que nos ingreso el ususario, la key libro la inicializamos en 0
                # ya que por defecto el miembro nuevo no tiene ningun libro rentado
                nuevoMiembro = {'ID': id, 'Nombre': nombre,"Celular": numero, 'Membresia': membresia, 'Pago': pago, 'Libro': "0"}
                # Agregamos al datrame de los data el nuevo renglon con los datos del nuevo miembro.
                df_agregar = df_agregar.append(nuevoMiembro, ignore_index=True) # Ponemos ignore_index=True para evitar problemas con los indices
                # Soscribimos en el archivo ya que con el nuevo miembro añadido
                df_agregar.to_csv("Miembros.csv")
            elif opcion1 == 2:
                # Lista de miembros
                df = pd.read_csv("Miembros.csv", index_col="ID") # Abrimos el csv donde los indices sean los IDs
                if df[1:].empty: # Checamos si el Dataframe despues del admin esta vacio
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                else:
                    # Al momento de leer el CSV tambien le la columna que no tiene nombre, por lo para evitar confundir al usuario
                    # y tambien porque nuestros indices ya son los IDs, la borramos con .drop()
                    df.drop('Unnamed: 0', axis=1, inplace=True)
                    print(df[1:].to_string()) # Imprimos despues del administrador, y usamos to_string() para que el dataframe se convierta
                    # en una concatenacion, de esta manarea evitamos que por alguna razón este se corte o resuma cuando lleguen a ser muchos mimbros
            elif opcion1 == 3: # Actualizar membresia
                df = pd.read_csv("Miembros.csv") # Abrimos el csv de miembros y generamos una copia en df
                df_copia = pd.read_csv("Miembros.csv") # Abrimos el csv de miembros y generamos otra copia en df_copia
                df_copia.set_index('ID', inplace=True) # Los indices de la copia pasan a ser los IDs, esto con el fin de facilitarnos la busqueda de los miembros
                df_copia.drop("Unnamed: 0", axis = 1, inplace=True) # Borramos la columna sin nombre ya que no es necesario y confunde al usuario
                if df[1:].empty: # Checamos que el Dataframe despues del admin no este vació
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                    # si lo esta, no hacemos nada mas y nos saltamos esta vuelta del ciclo
                    continue

                while True: #Ciclo while para depurar ciertas cosas
                    idcambiar = depInt("Ingresa el ID del miembro: ") # Le pedimos al ususario que ingrese su ID
                    try:
                        # Dentro de un try le imprimimos al usuario un resumen de su informacion de la copia del archivo
                        print("\n" + df_copia.loc[idcambiar].to_string()) #
                        # Usamos to_string() para evitar que se imprime el dtype y name, que son cosas que pueden confundir al usuario
                    except KeyError:
                        # Si nos da un error KeyError, quiere decir que el ID no existe dentro de nuestros datos
                        # y le informamos de ello al usuario
                        print("Este ID no existe porfavor verificalo.\n")
                        system("pause")
                        system("cls")
                        continue
                    opcion = depWhileInt(1, 2, "\nPorfavor confirma que esa es tu cuenta.\n1) Si  2)No: ")
                    # Una vez el usuario pueda ver su informacion, le pedimos que confirme que es suya
                    if opcion == 1:
                        break # Si nos dice que si, rompemos el ciclo while
                    else:
                        # Si nos dice que no, le informamos que porfavor cheque su ID en su "credencial"
                        # y le volvemos a pedir en el siguiente ciclo el ID
                        print("\nPorfavor checa el ID en tu credencial que se te dio.\n")
                        system("pause")
                        system("cls")

                # Del dataframe "original" ponemos los IDs como indices
                df.set_index('ID', inplace=True)

                if df.loc[idcambiar,"Membresia"] == "vip":
                    # Checamos si el usuario en base al ID que nos paso no tenga ya la membresia máxima
                    print("Tu membresia ya es VIP. No puedes mejorarla mas.") # Si la tiene, le informamos de ello
                    continue # Usamos continue para cancelar todo el ciclo del while del menu
                elif df.loc[idcambiar,"Membresia"] == "premium": # Actualizar de premium a vip
                    # En caso de que el miembro ya sea premium, solo puede mejorar a VIP, y le pedimos que confirme si quiere hacerlo
                    opcion = depWhileInt(1, 2, "\n¿Seguro que quieres mejorar tu membresia a VIP? Se te cobrarian $50 MXN.\n\n1) Si  2)No: ")
                    if opcion == 1:
                        #Si nos dice que si, cambiamos la membresia del miembro a vip en la casilla del Dataframe, los mismo con su pago mensual
                        df.loc[idcambiar, "Membresia"] = "vip"
                        df.loc[idcambiar, "Pago"] = 150

                        # Sumamos a nuestros ingresos la diferencia entre el costo de la membresia vip y la premiumm, es decir, 150-100
                        self.modificarIngresos(50)

                        # Paro luego evitar errores a la hora de agregar nuevos miembros despues, nos aseguramos que el dataframe sea igual
                        # a como esta la informacion en el excel, por lo que:
                        df.reset_index(inplace=True) #volvemos a poner los indices de 0 a n
                        df.drop("Unnamed: 0", axis = 1, inplace=True) #Borramos la columna extra sin nombre
                        df.to_csv("Miembros.csv") # Una vez que todo esta libre de errores, sobrescribimos el archivo CSV
                else:
                    opcion = depWhileInt(1, 2, "\n¿Que membresia nueva quieres?\n\nSi eliges VIP serian $100 MXN.\nSi eliges Premium serian $50 MXN.\n1) VIP  2)Premium: ")
                    # el else entra en caso de que la membresia del miembro sea standard, así que puede mejorarla a premium o a vip directamente, eso es lo que le preguntamos

                    # Dependiendo de lo que pida el usuario, nuevamem, cargo, nuevoc adquieren un valor específico
                    if opcion == 1:
                        nuevamem = "vip"
                        cargo = 100
                        nuevoc = 150
                    else:
                        nuevamem = "premium"
                        cargo = 50
                        nuevoc = 100

                    # Cambiamos la membresia y el pago mensual a la nueva membresia y el nuevo pago, que adquirieron cierto valor dependiendo
                    # de lo que eligio el usuario
                    df.loc[idcambiar, "Membresia"] = nuevamem
                    df.loc[idcambiar, "Pago"] = nuevoc

                    # Le cobramos al usuario la diferencia de pago entre la nueva membresia que eligio el usuario y los 50 de la membresia standard
                    self.modificarIngresos(cargo)

                    # Paro luego evitar errores a la hora de agregar nuevos miembros despues, nos aseguramos que el dataframe sea igual
                    # a como esta la informacion en el excel, por lo que:
                    df.reset_index(inplace=True)    # Volvemos a poner los indices de 0 a n
                    df.drop("Unnamed: 0", axis=1, inplace=True) # Borramos la columna extra sin nombre
                    df.to_csv("Miembros.csv")  # Una vez que todo esta libre de errores, sobrescribimos el archivo CSV
                    # Esto mismo lo haremos despues cada vez que tengamos que sobrescribir el arcihvo CSV
            elif opcion1 == 4: #Cancelar suscripcion
                df = pd.read_csv("Miembros.csv")
                if df[1:].empty: # Checamos que el dataframe despues del admin este vació
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                    continue

                dfTemp  = pd.read_csv("Miembros.csv", index_col = "ID") # Creamos otra copia como dataframe del archivo de miembros
                dfTemp.drop("Unnamed: 0", axis=1, inplace=True) # De esta copia borramos la columna sin nombre

                while True: #Ciclo while para depurar ciertas cosas
                    idborrar = depInt("Ingresa el ID del miembro a eliminar: ") # Le pedimos su ID al usuario
                    try:
                        print("\n" + dfTemp.loc[idborrar].to_string())
                        # Dentro de un try le imprimimos al usuario un resumen de su informacion de la copia del dataframe, es decir dfTemp
                    except KeyError:
                        # Si nos da un error KeyError, quiere decir que el ID no existe dentro de nuestros datos
                        # y le informamos de ello al usuario
                        print("\nEste ID no existe porfavor verificalo.\n")
                        system("pause")
                        system("cls")
                        continue
                    opcion = depWhileInt(1, 2,"\nPorfavor confirma que esa es tu cuenta.\n1) Si  2)No: ")
                    # Una vez el usuario pueda ver su informacion, le pedimos que confirme que es suya
                    if opcion == 1:
                        break   # Si nos dice que si, rompemos el ciclo while
                    else:
                        print("\nPorfavor checa el ID en tu credencial que se te dio.\n")
                        # Si nos dice que no, le informamos que porfavor cheque su ID en su "credencial"
                        # y le volvemos a pedir en el siguiente ciclo el ID

                print("") # Print estetico para dejar un espacio
                opcion = depWhileInt(1, 2, "\nEsta accion es irreversible.¿Estas seguro?\n1) Si  2)No: ")
                #Como es una accion más erie, le decimos si esta seguro de borrar su membresia
                if opcion == 1:
                    # Si nos dice que si, procedemos a borrar
                    df.drop(df.loc[df['ID']==idborrar].index, inplace=True) # En esta ocasion los indices de df no son los id
                    # van de 0 a n, por lo que mediante df.loc[df['ID']==idborrar].index le pedismos que borre el renglon con ese indice
                    df.drop("Unnamed: 0", axis=1, inplace=True)
                    df.to_csv("Miembros.csv")
                else:
                    system("cls")
                    continue
            elif opcion1 == 5: #Frecuencia de membresias
                df = pd.read_csv("Miembros.csv")
                df = df[1:] # Como dentro esta el administrador, y este tiene una membresia totalemente diferente
                # decimos que el dataframa sea despues del renglon del admin, para que no afecte nuestra gráfica
                moda = df['Membresia'].mode()[0] # Le pedimos la moda de la columna membresia, como esta accion
                # genera una Serie, usamos [0] para obtener solo el valor de tipo String
                sns.set(color_codes=True) #Linea que mejora el atractivo de la grafica a generar
                sns.countplot(x = "Membresia", data = df,palette="Spectral")
                # Le pedimos a seaborn que genera una grafica de la frecuencia de las membresias, que la paleta de colores sea "Spectral"
                plt.title(label = "La frecuencia de nuestras membresias\nModa: " + str(moda)) # Cambiamos el titulo de nuestra gráfica
                plt.show() # Mostramos la grafica
            elif opcion1 == 6: #Salir del menu
                system("cls")
                break
            else:
                continue
            print()
            system("pause")
            system("cls")

    def Libros(self):
        while True:
            #Le pedimos al usuario que ingresa una opcion del menu Libros
            opcion2 = depWhileInt(1,6,"1) Añadir libro\n2) Mostrar Catalogo\n3) Rentar libro\n4) Regresar un libro\n5) Fecuencia genero de los libros\n6) Salir\n\nIngresa una opcion del menu: ")
            system("cls")
            if opcion2==1:
                # Agregar Libro
                id=generarIDlib()
                # Generamos un ID aleatorio de 5 digitos
                nombre = input("Ingresa el nombre del nuevo Libro: ")
                print()
                genero = depWhileInt(1,7,"\n1) Manga\n2) Ciencia ficcion\n3) Novela\n4) Policiaco\n5) Fantasia\n6) Aventura\n7) Cuentos de hadas\n\nSelecciona un género: ")
                # Le pedimos que ingresa uno de los generos que existen dentro de nuestro dataframe, esto mismo los elegimos nosotros
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
                # Dependiendo de lo que elija el usuario genero va a adquierir un valor diferente
                autor = input("Ingresa el nombre del autor del libro: ")
                renta = "No" # Por defecto los libros no esta rentados
                df_agregar = pd.read_csv("Libros.csv", index_col= "Unnamed: 0") # Los indices  van a ser la columna sin nombre del CSV
                # Esto para evitar problemas a la hora de guardar la informacion
                nuevoLibro = {'ID': id, 'Nombre Libro': nombre,'Genero': genero, 'Autor':autor, 'Rentado': renta}
                # Creamos un diccionario con los datos
                df_agregar = df_agregar.append(nuevoLibro, ignore_index=True) # Agregamos el diccionario al dataframe con append
                df_agregar.to_csv("Libros.csv")
            elif opcion2==2:
                df = pd.read_csv("Libros.csv") #Guardamos en un dataframe una copia del CSV de los libros
                # El usuario pued elegir si quiere ver todo el catalogo o por genero
                selec = depWhileInt(1,2,"Elija si quiere ver.\n1) Catalogo completo.\n2) Algun genero en especifico: ")
                if selec == 1:
                    system("cls")
                    # Si elige por genero imprimimos todo el dataframe
                    print("Estos son los libros que tenemos disponibles: ")
                    df.drop("Unnamed: 0", axis=1, inplace=True) # Eliminamos la columa sin nombre
                    df.set_index('ID', inplace=True) # Los IDs pasan a ser los indices
                    print("\n" + df.to_string()) # to_string() evita que a la hora de imprimir la informacion este se resuma o corte
                elif selec == 2:
                    gen_esp = depWhileInt(1,7,"\n1) Manga\n2) Ciencia ficcion\n3) Novela\n4) Policiaco\n5) Fantasia\n6) Aventura\n7) Cuentos de hadas\n\nSelecciona el genero que guste revisar:")
                    # Le pedimos al usuario que ingrese el genero que quiere ver
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
                    # Dependiendo de lo que elija, se le informa al usuario que opcion eligio
                    df.drop("Unnamed: 0", axis=1, inplace=True)
                    df.set_index('ID', inplace=True)
                    print("\n" + df[df['Genero'] == genero1].to_string()) # Se muestran solos los libros del genero que eligió el usuario
            elif opcion2==3: #Rentar libro
                df = pd.read_csv("Libros.csv")
                gen_ren = depWhileInt(1,7,"1) Manga\n2) Ciencia ficcion\n3) Novela\n4) Policiaco\n5) Fantasia\n6) Aventura\n7) Cuentos de hadas\n\nSelecciona un genero: ")
                # Le pedimos al usuario que elija de que genero quiere rentar su libro
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
                # Creamos un dataframe que es copia del CSV de los miembros
                if df_miembros[1:].empty:
                    print("No hay ningun miembro registrado todavia.\nPor favor agrega antes uno.")
                    system("pause")
                    system("cls")
                    continue

                df_miembros.set_index("ID",inplace=True)

                id_personita = depInt("Ingresa tu ID para completar el registro: ") # Le pedimos su ID al usuario

                try:
                    if df_miembros.loc[id_personita, "Libro"] != 0:
                        # Checamos que el usuario no tenga ya rentado un libro
                        # Si esta condicion se cumple le informamos de ello al usuario
                        print("Usted ya tiene un libro rentado. Si desea rentar otro libro, devuelva el anterior.\n")
                        system("pause")
                        system("cls")
                        # Volvemos al submenu de Libros
                        continue
                except KeyError:
                    # Depuramos en caso de que el ID del usuario no exista
                    print("El ID que ingreso no existe. Por favor vuelva a intentarlo.\n")
                    system("pause")
                    system("cls")
                    # Si ocurre algo un error, nos saltamos to el ciclo y volvemos al submenu
                    continue

                while True:
                    system("cls")
                    #Imprimimos todos lo libros del genero que pidio el usuario y que no esten rentados
                    # De igual manera le pedimos al usuario que ingresa el ID del libro que desea rentar
                    id_lib = depInt(df[(df['Genero'] == genero) & (df['Rentado'] == 'No')].to_string() + "\n\nElija el ID del libro que desea rentar: ")
                    try:
                        df.loc[id_lib, "Rentado"] = 'Si' # La casillo Rentado del libro pasa a Si, ya que este se remtrp
                        df.reset_index(inplace=True)
                        df_miembros.loc[id_personita, "Libro"] = id_lib # La casillo libro del miembro pasa a tener el ID del libro que rento
                        df_miembros.drop("Unnamed: 0",axis=1,inplace=True)
                        df_miembros.reset_index(inplace=True)
                        df.to_csv("Libros.csv")
                        df_miembros.to_csv("Miembros.csv")
                        break
                        # Depuramos las posibilidades de errores que existen
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
                    if df_miembros.loc[id_personita,"Libro"] == 0: #Checamos el miembro tenga un libro que devolver
                        print("No tienes libros rentados.")
                        system("pause")
                        system("cls")
                        # Si la condicion se cumple volvemos al submenu libros
                        continue
                except KeyError:
                    print("El ID no existe. Por favor vuelva a intentarlo.")
                    system("pause")
                    system("cls")
                    # Si ocurre un error volvemos al submenu Libros
                    continue

                idLibro = df_miembros.loc[id_personita,"Libro"] #Obtenemos el ID del libro que tiene rentado el usuario
                df_libros.loc[idLibro,"Rentado"]="No" # El libro que rento el usuario pasa de nuevo a estar disponible
                df_miembros.loc[id_personita,"Libro"]=0 # El miembro en su casilla de Libro pasa a ser 0, ya que devolvio su libro
                df_miembros.drop("Unnamed: 0",axis=1, inplace=True)
                df_miembros.reset_index(inplace=True)
                df_libros.drop("Unnamed: 0",axis=1, inplace=True)
                df_libros.reset_index(inplace=True)
                # Recordemos que antes de sobrescribir la información, la esturcutra del dataframe debe ser la misma que la del excel
                # por estra razón devolvemos los indices a 0 a an, y borramos la columna extra sin nombre
                print("\nEl libro ha sido devuelto con exito en el sistema.") # Le informamos al usuario que el libro se ha devuelto con exito al sistema
                df_libros.to_csv("Libros.csv")
                df_miembros.to_csv("Miembros.csv")
            elif opcion2==5:
                df = pd.read_csv("Libros.csv")
                sns.set(color_codes=True) # Esta linea mejora el atractiva de la gráfica
                plt.figure(figsize=(9, 7)) # Debido a la cantidad de informacion, aumentamos el tamaño de la ventana
                # donde se mostrará la grafica
                sns.countplot(x="Genero", data=df, palette="Spectral", hue = "Rentado")
                # Le pedimos a seaborn que genere una gráfica de conteo de los generos, y que esto a su vez los divida
                # entre Rentados y no rentados
                plt.title(label="Frecuencia de los libros") # Cambiamos el titulo de la grafica
                plt.show() # Mostramos la grafica
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
                ganancia = df_gan.Pago.sum() # Sumamos todo los que nos generan las membrisias

                with open("Ingresos.txt") as file:
                    temporal = file.readlines()
                    gastos = ""
                    for x in temporal:
                        gastos += x
                    ingresos = float(gastos)
                # Leemos y convertimos mediante with open y un acumulador los ingresos que tenemos del día a día

                ganancia = ganancia + ingresos #Sumamos las ganancias mas lo ingresos para obtener las ganancias totales del mes

                df_gan = df_gan[1:] # Eliminamos el renglon del admin del dataframe para que no afecte a nuestra grafica
                sns.set(color_codes=True)
                plt.figure(figsize=(9, 7)) # Cambiamos el tamaño de la ventana donde se mostrara la gráfica
                df_gan.groupby("Membresia")["Pago"].sum().plot(kind="bar") # Le pedimos a matplotlib que generea una grafica de barras
                # de los ingresos que genera cada membresia
                plt.title(label="Ingresos por membresia\nLos ingresos del mes son: " + str(ganancia) + "$")
                plt.show()
            elif opcion3==2:
                # Creamos 3 ingresos fijos que son los gastos de luz, agua y renta
                gasto_luz = 100
                gasto_agua = 170
                gasto_renta = 300

                df_gan = pd.read_csv("Miembros.csv", index_col="Unnamed: 0")
                ganancia = df_gan.Pago.sum()  # Sumamos todo los que nos generan las membrisias

                with open("Ingresos.txt") as file:
                    temporal = file.readlines()
                    gastos = ""
                    for x in temporal:
                        gastos += x
                    ingresos = float(gastos)
                    # Leemos y convertimos mediante with open y un acumulador los ingresos que tenemos del día a día

                ganancia = ganancia + ingresos # Calculamos las ganancias totales del mes
                utilidades = ganancia - gasto_luz - gasto_agua - gasto_renta # Calcualmos la utilidad del mes
                # Restandole a las ganancias totales todos los gastos
                system("cls")
                # Imprimimos en pantalla la informacion de los gastos del mes
                print(f"El gasto de luz este mes fue de ${gasto_luz}")
                print(f"El gasto de agua de este mes fue de ${gasto_agua}")
                print(f"El gasto de la renta este mes fue de ${gasto_renta}")

                # Si el ususario tiene perdidas le informamos de ello
                # Si no, simplemente le imprimimos la la informacion la utilidad del mes
                if utilidades<=0:
                    print("Esta teniendo perdidas.")
                    print(f"Las perdidas fueron de de: ${utilidades*-1}")
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

    # Metodo al que le pasamos un cargo, y lo sumara al txt actual de ingresos
    def modificarIngresos(self,cargo):
         with open("Ingresos.txt") as file:
             temporal = file.readlines() # Abrimos el el txt de los ingresos y leemos todo
             gastos = "" # Creamos el acumulador de texto gastos
             for x in temporal:
                 gastos += x # Concatenamos todo el numero

             gastos = float(gastos) # Lo parseamos a float para poder hacer sumas aritméticas
             gastos += cargo # sumamos el cargo que pasamos como parametro

         with open("Ingresos.txt", "w") as file: #Abrimos otraves Ingresos esta vez en modo escritura
             file.write(str(gastos)) # Sobrescribimos lo que hay en el txt con la nueva cantidad
            # Y parseamos eso mismo a string ya que write solo admite ese tipo de variable


biblioteca = Administrador()