import os

res1 = '1.- Agregar Nuevo Contacto' 
res2 = '2.- Editar Contacto' 
res3 = '3.- Ver Contactos' 
res4 = '4.- Buscar Contacto' 
res5 = '5.- Eliminar Contacto' 


CARPETA = 'contactos/'
EXTENSION = '.txt'

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    # ReVISA
    crear_directorio()
    motrar_menu()

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            print(res3)
            preguntar = False
        elif opcion == 4:
            print(res4)
            preguntar = False
        elif opcion == 5:
            print(res5)
            preguntar = False
        else:
            print('Opcion no válida')

def agregar_contacto():
    print('Escribe los datos para agregar nuevo contacto')
    nombre_contacto = input('Nombre del Contacto:\r\n')

    # Revisar si el contacto ya existe
    existe = existe_usuario(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # resto de los campos
            telefono_contacto = input('Agrega Telefono:\r\n')
            categoria_contacto = input('Agrega Categoria:\r\n')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            # Escribir en el archivo:
            archivo.write('Nombre: '+ contacto.nombre + '\n')
            archivo.write('Telefono: '+ contacto.telefono + '\n')
            archivo.write('Categoria: '+ contacto.categoria + '\n')

            # mensaje de exito
            print('\r\n Contacto Creado...')
        
    else:
        print('Ese contacto ya existe')

    # Reiniciar la app
    app()

def editar_contacto():
    contacto_original = input('Nombre del contacto a editar \r\n')

    # Revisar si el contacto existe antes de editarlo
    existe = existe_usuario(contacto_original)

    if existe:
        with open(CARPETA + contacto_original + EXTENSION, 'w') as archivo:

            # Actualizar campos
            nombre_contacto = input('Nuevo Nombre: \r\n')
            telefono_contacto = input('Nuevo Telefono: \r\n')
            categoria_contacto = input('Nueva Categoria: \r\n')

            # Instanciar 
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Rescribir archivo
            archivo.write('Nombre: '+ contacto.nombre + '\n')
            archivo.write('Telefono: '+ contacto.telefono  + '\n')
            archivo.write('Categoria: '+ contacto.categoria + '\n')

        # Renombrar el archivo editado
        os.rename(CARPETA + contacto_original + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
    else:
        print('Ese usuario no existe')

def motrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5)

def crear_directorio():
    # crear la carpeta
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
    
def existe_usuario(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()
