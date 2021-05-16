import csv
from os import system

'''
Estas 2 funciones sirven principalmente para evitar errores de parseo y
controlar el ingreso de la contraseña, que debe se run pin numerico de 6 digitos.
'''
def depurar_int(mensaje=""):
	while True:
			try:
				temp = int(input(mensaje))
				break
			except:
				print("Dato no valido, porfavor ingresa otro.\n")
	return temp

def contranomas6(contra):
	while True:
				if len(str(contra)) != 6:
					system("cls")
					print("La contraseña no es de 6 dígitos.")
					contra = input("Ingresa la contraseña: ")
				else:
					break
	return contra				

class Celular:
	def __init__(self):
		#El modelo es algo permanente,.. hasta que cambies de telefono, razón por la que esta encapsualdo.
		#El sistema operativo es la última version existente, por eso también esta encapsulado.
		self.__modelo = "Nokia Symbian"
		self.__OS = "Symbian OS 10.1"
		self.menu = "----Bienvenido---\n\n1) Contactos\n2) Agenda\n3) Calculadora\n4) Ajustes\n5) Apagar\n\n"
		self.valicalcu = False

		with open("Contra.txt","r") as file:
			temp = file.readlines()

		contra = "" 

		for x in temp:
			contra += x	

			
		if contra != "":

			intentos = 1
			print("Ingresa la contraseña: ")
			contrau = input()
			
			contrau = contranomas6(contrau)

			while True:
				
				if contra == contrau:
					break
				elif intentos>=3:
					system("cls")
					print("Superaste el límite de 3 intentos.\nPor seguridad el sistema se bloqueara.\n")
					system("pause")
					exit() 
				else:
					system("cls")
					print("Contraseña incorrecta, te quedan",(3-intentos),"intento(s)")
					contrau = input("Ingresa la contraseña: ")
					contrau = contranomas6(contrau)
					intentos +=1

		system("cls")
		self._funcionar()

	def _funcionar(self):

		self.Appcontactos = Contactos()
		self.Appagenda = Agenda()

		while True:
			
			print(self.menu)

			opcion = depurar_int("Ingrese la opción del menu: ")
			if opcion == 1:
				system("cls")
				self.Appcontactos._funcionar()
			elif opcion == 2:
				system("cls")
				self.Appagenda._funcionar()
			elif opcion == 3:	
				system("cls")
				self.valicalcu = True
				self.Appcalculadora = Calculadora()  
			elif opcion == 4:
				system("cls")
				self.ajustes()
			elif opcion == 5:
				print("\nApagando...")
				system("pause")
				exit()	
			else:
				system("cls")
				continue
			system("cls")

	def ajustes(self):
		menu = "----Ajustes---\n\n1) Cambiar contraseña\n2) Acerca del dispostivo\n3) Apps\n4) Salir\n"

		while True:
			
			print(menu)
			opcion = depurar_int("Ingrese una opcion del menu: ")
			if opcion == 1:
				system("cls")
				with open("Contra.txt","r") as file:
					temp = file.readlines()

				contra = "" 

				for x in temp:
					contra += x	

					
				if contra != "":
					intentos = 1
					print("Ingresa la contraseña actual: ")
					contrau = input()
				
					contrau= contranomas6(contrau)

					while True:
						
						if contra == contrau:
							break
						elif intentos>=5:
							system("cls")
							print("Superaste el límite de 5 intentos.\nPor seguridad el sistema se bloqueara.\n")
							system("pause")
							exit() 
						else:
							system("cls")
							print("Contraseña incorrecta, te quedan",(5-intentos),"intento(s)")
							contrau = input("Ingresa la contraseña: ")
							contrau = contranomas6(contrau)
							intentos +=1

					system("cls")
					newcontra = depurar_int("Ingresa la contraseña nueva, esta tiene que ser un pin numerico de 6 dígitos: ")
					newcontra = contranomas6(newcontra)
					system("cls")
					print("Esta sera la contraseña del dipostivo a partir de ahora:",newcontra,"\nRecuerdala.")
					system("pause")

					with open("Contra.txt","w") as file:
							file.write(str(newcontra))
					system("cls")		
					print("¡La contraseña a sido modificada con exito!")
					system("pause")
					system("cls")			
				else:
					print("Tu celular no tiene contraseña\n¿Quieres ponerle una?  1)Si 2)No: ")
					temp = depurar_int()

					if temp == 1:
						system("cls")
						newcontra = depurar_int("Ingresa la contraseña nueva, esta tiene que ser un pin numerico de 6 dígitos: ")
						newcontra = contranomas6(newcontra)
						print("Esta sera la contraseña del dipostivo a partir de ahora:",newcontra,"\nRecuerdala.")
						system("pause")
						with open("Contra.txt","w") as file:
							file.write(str(newcontra))
						system("cls")
						print("¡La contraseña a sido modificada con exito!")
						system("pause")
						system("cls")
					elif temp == 2:
						system("cls")
						print("Regresando al menu.")
						system("pause")
						system("cls")
					else:
						print("Dato no valido, regresaras al menu.\n")
						system("pause")
						system("cls")						
			elif opcion == 2:
				system("cls")
				print("Modelo del dispositivo: " + self.get_modelo() + "\n")
				print("Sistema operativo: " + self.get_OS())
				print()
				system("pause")
				system("cls")
			elif opcion == 3:
				
				
				while True:
					system("cls")
					print("1) Contactos\n2) Agenda\n3) Calculadora\n4) Salir\n")
					temp2 = depurar_int("Ingrese una opcion del menu: ")

					# Recordemos que la info de las Apps esta encapsulada, por lo que es importante hacer uso del método que les creamos
					# para poder imprimirlos en pantalla.
					if temp2 == 1:
						system("cls")
						print("Version: " + str(self.Appcontactos.get_version()) + "\nPeso: " + str(self.Appcontactos.get_peso()) + " GB\n")
						system("pause")
					elif temp2 == 2:
						system("cls")
						print("Version: " + str(self.Appagenda.get_version()) + "\nPeso: " + str(self.Appagenda.get_peso()) + " GB\n")
						system("pause")	
					elif temp2 == 3:
						if self.valicalcu == False:
							system("cls")
							print("No ha abierto la calculadora, porfavor abra antes la app.")
							system("pause")
						else:
							system("cls")	
							print("Version: " + str(self.Appcalculadora.get_version()) + "\nPeso: " + str(self.Appcalculadora.get_peso()) + " GB\n")
							system("pause")

					elif temp2 == 4:
						print("Saliendo...")
						system("pause")
						system("cls")
						break

					else:
						system("cls")
						continue
			elif opcion == 4:	
				
				print("Saliendo...")
				system("pause")
				break
			else:
				system("cls")
				continue	

	def	get_OS(self):
		return self.__OS
	def get_modelo(self):
		return self.__modelo			

'''
La clase App sera el molde que se use para todas las apps, como atributos tiene nombre, version y peso.
El peso y versión estan encapsulados para evitar errores de nombre de variable, y porque son archivos que no se
planean ser modificados de manera directa por el usuario.

Como métodos tiene un getter y un setter, que nos permiten modificar la información o obtenerla, esto es necesario debido a la
encapsulación. 
'''		
class App:
	def __init__(self):
		#Tanto el peso como la version son encapsulados para que el usuario no pueda modificarlos de alguna manera.
		self.__version = 1.0
		self.nombre = "App"
		#Peso en GB
		self.__peso = 0

	def get_peso(self):
		return self.__peso
	def set_peso(self, npeso):
		self.__peso = npeso
		return self.__peso	
	
	def get_version(self):
		return self.__version
	def set_version(self, nversion):
		self.__version = nversion
		return self.__version

#Cada una de las apps hereda los atributos la clase App, razón por lo que podemos hacer uso del setter, que recordemos
#es un método de la clase Padre, aparte se tiene que hacer uso de este método forzosamente, ya que esta información esta
#encapsulada				
class Contactos(App):
	def __init__(self):
		self.nombre = "Contactos"
		self.set_version(1.0)
		self.set_peso(4)
		self.menu = "----Contactos---\n1) Añadir contacto\n2) Lista de contactos\n3) Buscar contacto\n4) Editar Contacto\n5) Salir"

	def _funcionar(self):

		while True:
			print(self.menu)
		
			opcion = depurar_int("\nIngrese la opción del menu: ")


			if opcion == 1:
				self.anadir()
			elif opcion ==2:
				self.lista()
			elif opcion ==3:
				self.buscar()
			elif opcion ==4:
				self.editar()
			elif opcion==5:
				print("\nSaliendo...")
				system("pause")
				break
			else:
				system("cls")
				continue
					

	def anadir(self):
		system("cls")
		print("\n---Añadir Contacto---\n")
		#newline="" indica que una nueva linea para escrbir sera una vacía, así evitamos los espacios que deja el append
		with open("AgendaContactos.csv", "a", newline="") as file:
			writer = csv.writer(file, delimiter=",")
			nombre = input("Ingresa el nombre del contacto: ")
			numero = depurar_int("Ingresa el numero del contacto: ")
			correo = input("Ingresa el correo del contacto: ")
			temp = [nombre,numero,correo]
			writer.writerow(temp)
		system("cls")	

	def lista(self):
		system("cls")
		print("\n---Contactos Actuales---\n")
		with open("AgendaContactos.csv") as file:
			reader = csv.reader(file, delimiter=",")
			for row in reader:
				print("Nombre:", row[0], "\nNumero:", row[1], "\nCorreo:", row[2],"\n\n")
		system("pause")
		system("cls")				

	def buscar(self):
		system("cls")
		print("\n---Buscar Contacto---\n")
		nombre = input("Ingresa el nombre del contacto a buscar: ")
		vali = False
		with open("AgendaContactos.csv") as file:
			reader = csv.reader(file,delimiter=",")
			for row in reader:
				if row[0] == nombre:
					vali = True
					print("\nNombre:", row[0], "\nNumero:", row[1], "\nCorreo:", row[2],"\n")
					break

			if vali == False:
				print("\nEl contacto no fue encontrado, regresando al menu.")
		system("pause")
		system("cls")			
			
	def editar(self):
		system("cls")
		print("\n---Editar Contacto---\n")
		nombre = input("Ingresa el nombre del contacto a buscar: ")
		system("cls")
		vali = False
		
		#Creamos una lista temporal de los contactos
		with open("AgendaContactos.csv") as file:
			reader = csv.reader(file, delimiter=",")
			lista_contactos = []
			for row in reader:
				lista_contactos.append(row)
			
		
		#Cambiamos el valor
		for contacto in lista_contactos:
			if contacto[0] == nombre:
				vali = True
				print("1)Nombre")
				print("2)Numero")
				print("3)Correo\n")
				opcion = depurar_int("Ingresa la opcion del dato que quieres modificar: ")
				system("cls")
				
				while True:
					if opcion<1 or opcion>3:
						print("El dato no es válido, ingresa otro.\n")
						print("1)Nombre")
						print("2)Numero")
						print("3)Correo\n")
						opcion = depurar_int("Ingresa la opcion del dato que quieres modificar: ")
						system("cls")
					else:
						break	
				
				print()

				if opcion == 1:
					dato = input("Ingresa el nuevo nombre: ")
					contacto[0] = dato
				elif opcion == 2:
					dato = depurar_int("Ingresa el nuevo numero: ")
					contacto[1] = dato
				elif opcion == 3:
					dato = input("Ingresa el nuevo correo: ")
					contacto[2] = dato
					
				break

		if vali == False:
			print("\nEl contacto no fue encontrado, o ingresaste algo no valido, regresando al menu.")
			system("pause")
			system("cls")
		else:
			with open("AgendaContactos.csv","w",newline="") as file:
				writer = csv.writer(file, delimiter=",")
				writer.writerows(lista_contactos)
			
			system("cls")	

class Calculadora(App):
	def __init__(self):
		App.__init__(self)
		self.nombre = "Calculadora"	
		self.set_peso(1)
		self.set_version(1.0)

		while True:
			print("----Calculadora----\n")
			self.x = depurar_int("Ingresa el primer numero: ")
			self.y = depurar_int("Ingresa el segundo numero: ")
			system("cls")
			self.calculo(self.x,self.y)
			
			print("\nQuieres hacer otra operacion: 1)Si 2)No")
			opcion = depurar_int()

			if opcion == 2:
				break
			system("cls")	


	def calculo(self,x,y):
	    try:
	        lista_op=[lambda x,y:x+y,
	                  lambda x,y:x-y,
	                  lambda x,y:x/y if y!=0 else "No se puede dividir entre 0",
	                  lambda x,y:x*y,
	                  lambda x,y:x**y,
	                  lambda x,y:x**(1/y) if y!=0 else "No se puede sacar raíz de 0"]
	        operaciones=("Suma","Resta","División","Multiplicación","Potencia","Raíz")
	        print(30*"-")
	        print("Ingrese la opción deseada:")
	        for n in range(len(operaciones)):
	            print(n+1,")",operaciones[n])
	        print(30*"-")    
	        inciso=depurar_int("Indique el inciso de la operacion: ")
	        print("El resultado de la operación",operaciones[inciso-1],"es: ")
	        print(lista_op[inciso-1](x,y))
	    
	    except:
	        print("Alguno de sus valores no es válido, probablemente intento dividir entre 0.") 

class Agenda(App):
	def __init__(self):
		self.name = "Agenda"
		self.set_version(1.0)
		self.set_peso(10)
		self.menu = "----Agenda---\n\n1) Añadir tarea\n2) Lista de tareas\n3) Eliminar tarea\n4) Salir\n"

	def _funcionar(self):
		while True:
			print(self.menu)

			opcion = depurar_int("Ingrese la opción del menu: ")
			if opcion == 1:
				self.anadir_tarea()
			if opcion == 2:
				self.lista()
			if opcion == 3:	
				self.eliminar()
			if opcion == 4:
				print("\nSaliendo....")
				system("pause")
				break
			else:
				system("cls")
				continue
							

	def anadir_tarea(self):
		system("cls")

		opcion = depurar_int("Ingresa el numero del día de la semana al que agregar la tarea (1-7, Empezando por Lunes): ")
		print()
		if opcion == 1:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Lunes.txt","a") as file:
				tarea = input("Ingresa la tarea: ")
				file.write(tarea+"\n")
				system("cls")
		elif opcion == 2:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Martes.txt","a") as file:
				tarea = input("Ingresa la tarea: ")
				file.write(tarea+"\n")
				system("cls")
		elif opcion == 3:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Miercoles.txt","a") as file:
				tarea = input("Ingresa la tarea: ")
				file.write(tarea+"\n")
				system("cls")
		elif opcion == 4:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Jueves.txt","a") as file:
				tarea = input("Ingresa la tarea: ")
				file.write(tarea+"\n")
				system("cls")
		elif opcion == 5:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Viernes.txt","a") as file:
				tarea = input("Ingresa la tarea: ")
				file.write(tarea+"\n")
				system("cls")
		elif opcion == 6:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Sabado.txt","a") as file:
				tarea = input("Ingresa la tarea: ")
				file.write(tarea+"\n")
				system("cls")
		elif opcion == 7:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Domingo.txt","a") as file:
				tarea = input("Ingresa la tarea: ")
				file.write(tarea+"\n")
				system("cls")
		else:
			print("Dato no valido, regresaras al menu.\n")
			system("pause")
			system("cls")														

	def lista(self):

		system("cls")
		print("1) Para mostrar las tareas de un día en específico\n2) Para las de toda la semana: ")
		opcion = depurar_int()
		system("cls")

		if opcion == 1:
			temp = depurar_int("Ingresa el numero del día de la semana (1-7, Empezando por Lunes): ")
			system("cls")
			if temp == 1:
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Lunes.txt","r") as file:
					print("Las tareas a realizar para el Lunes son: \n")
					i = 1
					for tarea in file:
						print(str(i) + ")",tarea)
						i+=1

				
			elif temp == 2:
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Martes.txt","r") as file:
					print("Las tareas a realizar para el Martes son: \n")
					i = 1
					for tarea in file:
						print(str(i) + ")",tarea)
						i+=1
					
			elif temp == 3:
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Miercoles.txt","r") as file:
					print("Las tareas a realizar para el Miércoles son: \n")
					i = 1
					for tarea in file:
						print(str(i) + ")",tarea)
						i+=1
					
			elif temp == 4:
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Jueves.txt","r") as file:
					print("Las tareas a realizar para el Jueves son: \n")
					i = 1
					for tarea in file:
						print(str(i) + ")",tarea)
						i+=1
					
			elif temp == 5:
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Viernes.txt","r") as file:
					print("Las tareas a realizar para el Viernes son: \n")
					i = 1
					for tarea in file:
						print(str(i) + ")",tarea)
						i+=1
			elif temp == 6:
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Sabado.txt","r") as file:
					print("Las tareas a realizar para el Sábado son: \n")
					i = 1
					for tarea in file:
						print(str(i) + ")",tarea)
						i+=1
			elif temp == 7:
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Domingo.txt","r") as file:
					print("Las tareas a realizar para el Domingo son: \n")
					i = 1
					for tarea in file:
						print(str(i) + ")",tarea)
						i+=1
			else:
				print("Dato no valido, regresaras al menu.\n")
				system("pause")
				system("cls")			
		elif opcion == 2:
			dias=("Lunes","Martes","Miercoles","Viernes","Jueves","Sabado","Domingo")

			print("Las tareas a realizar para la siguiente semana son: ")
			print()

			for x in range(7):
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\\"+ dias[x] +".txt","r") as file:
					print("-"*10,dias[x],"-"*10)
					i = 1
					for tarea in file:
						print(str(i) + ")",tarea)
						i+=1
					print("\n")	
		else:
			print("Dato no valido, regresaras al menu.\n")
			system("pause")
			system("cls")		

		system("pause")
		system("cls")			

	def eliminar(self):	
		system("cls")

		opcion = depurar_int("Ingresa el numero del día de la semana del cual eliminar una tarea (1-7, Empezando por Lunes): ")
		
		print()
		if opcion == 1:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Lunes.txt","r") as file:
				
				lista = file.readlines()
			
				
			#Depuramos en caso de que el txt este vació.
			if lista == []:
				print("No existe una tarea en este día.\nAgrega una tarea antes o seleccione otro día.\n")
				system("pause")	
			else:
				i = 1			
				for tarea in lista:
					print(str(i) + ")",tarea)
					i+=1
				print("\nElige la tarea que quieres eliminar mediante su indice: ")

				temp = depurar_int()
				lista.pop(temp-1)

				#Como el nombrearchivo.write() solo admite strings, acumulamos todo en nuevotxt y despues lo pasamos
				nuevotxt = ""

				for tarea in lista:
					nuevotxt += tarea 

				#Sobrescribimos la informacion
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Lunes.txt","w") as file:
					file.write(nuevotxt)
				system("cls")		
		elif opcion == 2:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Martes.txt","r") as file:
				
				lista = file.readlines()
								
			#Depuramos en caso de que el txt este vació.
			if lista == []:
				print("No existe una tarea en este día.\nAgrega una tarea antes o seleccione otro día.\n")
				system("pause")
			else:
				i = 1			
				for tarea in lista:
					print(str(i) + ")",tarea)
					i+=1
				print("\nElige la tarea que quieres eliminar mediante su indice: ")
				temp = depurar_int()
				lista.pop(temp-1)

				#Como el nombrearchivo.write() solo admite strings, acumulamos todo en nuevotxt y despues lo pasamos
				nuevotxt = ""

				for tarea in lista:
					nuevotxt += tarea 

				#Sobrescribimos la informacion
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Martes.txt","w") as file:
					file.write(nuevotxt)
				system("cls")		
		elif opcion == 3:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Miercoles.txt","r") as file:
				
				lista = file.readlines()
								
			#Depuramos en caso de que el txt este vació.
			if lista == []:
				print("No existe una tarea en este día.\nAgrega una tarea antes o seleccione otro día.\n")
				system("pause")
			else:
				i = 1			
				for tarea in lista:
					print(str(i) + ")",tarea)
					i+=1
				print("\nElige la tarea que quieres eliminar mediante su indice: ")
				temp = depurar_int()
				lista.pop(temp-1)

				#Como el nombrearchivo.write() solo admite strings, acumulamos todo en nuevotxt y despues lo pasamos
				nuevotxt = ""

				for tarea in lista:
					nuevotxt += tarea 

				#Sobrescribimos la informacion
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Miercoles.txt","w") as file:
					file.write(nuevotxt)
				system("cls")					
		elif opcion == 4:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Jueves.txt","r") as file:
				
				lista = file.readlines()
								
			#Depuramos en caso de que el txt este vació.
			if lista == []:
				print("No existe una tarea en este día.\nAgrega una tarea antes o seleccione otro día.\n")
				system("pause")
			else:
				i = 1			
				for tarea in lista:
					print(str(i) + ")",tarea)
					i+=1
				print("\nElige la tarea que quieres eliminar mediante su indice: ")
				temp = depurar_int()
				lista.pop(temp-1)

				#Como el nombrearchivo.write() solo admite strings, acumulamos todo en nuevotxt y despues lo pasamos
				nuevotxt = ""

				for tarea in lista:
					nuevotxt += tarea 

				#Sobrescribimos la informacion
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Jueves.txt","w") as file:
					file.write(nuevotxt)
				system("cls")					
		elif opcion == 5:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Viernes.txt","r") as file:
				
				lista = file.readlines()
								
			#Depuramos en caso de que el txt este vació.
			if lista == []:
				print("No existe una tarea en este día.\nAgrega una tarea antes o seleccione otro día.\n")
				system("pause")
			else:
				i = 1			
				for tarea in lista:
					print(str(i) + ")",tarea)
					i+=1
				print("\nElige la tarea que quieres eliminar mediante su indice: ")
				temp = depurar_int()
				lista.pop(temp-1)

				#Como el nombrearchivo.write() solo admite strings, acumulamos todo en nuevotxt y despues lo pasamos
				nuevotxt = ""

				for tarea in lista:
					nuevotxt += tarea 

				#Sobrescribimos la informacion
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Viernes.txt","w") as file:
					file.write(nuevotxt)
				system("cls")					
		elif opcion == 6:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Sabado.txt","r") as file:
				
				lista = file.readlines()
								
			#Depuramos en caso de que el txt este vació.
			if lista == []:
				print("No existe una tarea en este día.\nAgrega una tarea antes o seleccione otro día.\n")
				system("pause")
			else:
				i = 1			
				for tarea in lista:
					print(str(i) + ")",tarea)
					i+=1
				print("\nElige la tarea que quieres eliminar mediante su indice: ")
				temp = depurar_int()
				lista.pop(temp-1)

				#Como el nombrearchivo.write() solo admite strings, acumulamos todo en nuevotxt y despues lo pasamos
				nuevotxt = ""

				for tarea in lista:
					nuevotxt += tarea 

				#Sobrescribimos la informacion
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Sabado.txt","w") as file:
					file.write(nuevotxt)
				system("cls")					
		elif opcion == 7:
			with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Domingo.txt","r") as file:
				
				lista = file.readlines()
								
			#Depuramos en caso de que el txt este vació.
			if lista == []:
				print("No existe una tarea en este día.\nAgrega una tarea antes o seleccione otro día.\n")
				system("pause")
			else:
				i = 1			
				for tarea in lista:
					print(str(i) + ")",tarea)
					i+=1
				print("\nElige la tarea que quieres eliminar mediante su indice: ")
				temp = depurar_int()
				lista.pop(temp-1)

				#Como el nombrearchivo.write() solo admite strings, acumulamos todo en nuevotxt y despues lo pasamos
				nuevotxt = ""

				for tarea in lista:
					nuevotxt += tarea 

				#Sobrescribimos la informacion
				with open("D:\Apuntes IAV 2 Semestre\Apuntes POO\Proyectos\Proyecto 2do Parcial\Dias\Domingo.txt","w") as file:
					file.write(nuevotxt)
				system("cls")					
		else:
			print("Dato no valido, regresaras al menu.\n")
			system("pause")
			system("cls")	 		

cel = Celular()			