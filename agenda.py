# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, 
# el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones
# Añadir contacto
# Lista de contactos
# Buscar contacto
# Editar contacto
# Cerrar agenda

class Agenda():
    
    def __init__(self):
        # Creamos una lista en donde cada entrada son los datos de un contacto en la agenda
        self.contactos_agenda=[]
    
    #Ahora nos falta construir todos los metodos para simular de manera eficiente una lista
    # inicialmente tenemos que tener un menu que nos indique que deseamos realizar

    def menu(self):
        menu=[
            ["Agenda personal"],
            ["1. Lista de contactos"],
            ["2. Buscar contacto"],
            ["3. Añadir contacto"],
            ["4. Editar contacto"],
            ["5. Eliminar contacto"],
            ["6. Salir de la agenda"]    
        ]

        #para que el metodo menu nos muestre el menu
        for accion in range(len(menu) ): 
            print(menu[accion][0])
            
        eleccion=int( input("Introduzca la accion que desea realizar ") )
        #Se contruyen las acciones que desea realizar la persona (y se ponen los enlaces con los metodos respectivos para la accion)
        if eleccion==1:
            self.nombre_contactos() #para consultar nombres contactos
                
            
        elif eleccion==2:
            self.buscar_contacto() # para buscar un solo contacto
            

        elif eleccion==3:
            self.añadir_contacto() #para crear un nuevo contacto
               

        elif eleccion==4:
            self.editar_contacto() #para editar un contacto existente
            

        elif eleccion==5:
            self.eliminar_contacto() #para eliminar un contacto

        elif eleccion==6:
            print('Saliendo de la agenda ... ')
            exit() 

        #Se vuelve a llamar al menu    
        self.menu()

    def nombre_contactos(self):
        # self.contactos_agenda
        if len(self.contactos_agenda)==0:
            print("La agenda no tiene contactos ")
        
        else:
            for nombre in range(len(self.contactos_agenda)):
                print(self.contactos_agenda[nombre]["Nombre"]) #Como voy a crear diccionarios, asi accedo a sus valores
                
    #Este es un ejemplo claro donde las dos comillas producen un error de sintaxis:
    #nota: cuando se acceda a los valores de un diccionario que esta contenido en una lista,
    #usar '' en lugar de ""
    # def buscar_contacto(self):
    #     print("---------------------")
    #     print("Buscador de contactos")
    #     print("---------------------")
    #     nomb = input("Introduzca el nombre del contacto: ")
    #     for contacto in range(len(self.contactos_agenda)):
    #         if nomb == self.contactos_agenda[contacto]["nombre"]:
    #             print("Datos del contacto")
    #             print(f"Nombre: {self.contactos_agenda[contacto]['nombre']}")
    #             print(f"Teléfono: {self.contactos_agenda[contacto]['telefono']}")
    #             print(f"E-mail: {self.contactos_agenda[contacto]['email']}")
    #             return contacto

    def buscar_contacto(self):
        print("---------------------")
        print("Buscador de contactos ")
        print("---------------------")
        nomb=input("Introduzca el nombre del contacto ")
        for contacto in range(len(self.contactos_agenda)):
            if nomb==self.contactos_agenda[contacto]["Nombre"]:
                print("Datos del contacto")
                print(f"Nombre: {self.contactos_agenda[contacto]['Nombre']}")
                print(f"Telefono: {self.contactos_agenda[contacto]['Telefono']}")
                print(f"E-mail: {self.contactos_agenda[contacto]['Email']}")
                return contacto

    #Metodo para añadir contactos
    def añadir_contacto(self):
        print("---------------------")
        print("Añadir nuevo contacto")
        print("---------------------")
        nomb=input("Introduzca el nombre del contacto ")
        tel=int(input("Introduzca el teleono del contacto "))
        email=input("Introduzca el email del contacto ")
        self.contactos_agenda.append({"Nombre":nomb,"Telefono":tel,"Email":email})
				            
        

	#Metodo para editar contactos	
    def editar_contacto(self):
        print("---------------------")
        print("Editar contactos")
        print("---------------------")
        informacion=self.buscar_contacto()
        condicion=False

        while condicion==False:
            print('Selecciona que deseas editar: ')
            print('1. Nombre')
            print('2. Telefono')
            print('3. E-mail')
            print('4. Volver')
            opcion = int(input('Introduzca la opcion deseada: '))
			
            if opcion==1:
                nombre_nuevo=input("Introduzca el nombre que desea actualizar: ")
                self.contactos_agenda[informacion]['Nombre'] = nombre_nuevo
            elif opcion == 2:
                telefono_nuevo=int(input("Introduzca el telefono que desea actualizar: "))
                self.contactos_agenda[informacion]['Telefono']=telefono_nuevo
            
            elif opcion==3:
                email_nuevo=input("Introduzca el E-mail que desea actualizar: 3")
                self.contactos_agenda[informacion]["Email"]=email_nuevo
            
            elif opcion ==4:
                condicion == True #Con esta condicion se rompe el ciclo while
                self.menu()
                 


    def eliminar_contacto(self):
        print("---------------------")
        print("Editar contactos")
        print("---------------------")
        informacion=self.buscar_contacto()
        self.contactos_agenda.remove(informacion)

        
agenda1=Agenda()

#agenda1.añadir_contacto()

agenda1.menu()

print(agenda1.contactos_agenda)