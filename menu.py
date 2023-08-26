from modulos.usuario import Usuarios
from modulos.administrador import Administradores

def iniciar_sesion_usuario(usuario_manager):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    usuario_id, es_admin = usuario_manager.iniciar_sesion(nombre_usuario, contrasena)
    return usuario_id, es_admin

def iniciar_sesion_admin(admin_manager):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    usuario_id, es_admin = admin_manager.iniciar_sesion(nombre_usuario, contrasena)
    return usuario_id, es_admin

def mostrar_menu_usuario(usuario_manager, usuario_id):
    while True:
        print("\n--- Menú de Usuario ---")
        print("1. Crear lista de películas")
        print("2. Calificar lista")
        print("3. Comentar lista")
        print("4. Mostrar detalles de lista")
        print("5. Compartir lista")
        print("6. Ver lista de películas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo_lista = input("Ingrese el título de la nueva lista de películas: ")
            etiquetas = input("Ingrese las etiquetas (separadas por comas): ")
            peliculas = input("Ingrese los IDs de las películas (separados por comas): ").split(",")
            usuario_manager.crear_lista(usuario_id, titulo_lista, etiquetas, peliculas)

        elif opcion == "2":
            lista_id = input("Ingrese el ID de la lista a calificar: ")
            calificacion = input("Ingrese su calificación ('me gustó' o 'no me gustó'): ")
            usuario_manager.dar_like(usuario_id, lista_id)
        elif opcion == "3":
            lista_id = input("Ingrese el ID de la lista a comentar: ")
            comentario = input("Ingrese su comentario: ")
            usuario_manager.dejar_comentario(usuario_id, lista_id, comentario)
        elif opcion == "4":
            lista_id = input("Ingrese el ID de la lista a mostrar detalles: ")
            usuario_manager.mostrar_lista(lista_id)
        elif opcion == "5":
            lista_id = input("Ingrese el ID de la lista a compartir: ")
            usuario_manager.compartir_lista(lista_id)
        elif opcion == "6":
            usuario_manager.ver_peliculas()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


def mostrar_menu_admin(admin_manager):
    while True:
        print("\n--- Menú de Administrador ---")
        print("1. Agregar película")
        print("2. Editar película")
        print("3. Eliminar película")
        print("4. Moderar comentario")
        print("5. Ver lista de películas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Ingrese el título de la película: ")
            genero = input("Ingrese el género de la película: ")
            director = input("Ingrese el director de la película: ")
            anio = input("Ingrese el año de la película: ")
            descripcion = input("Ingrese la descripción de la película: ")
            admin_manager.agregar_pelicula(titulo, genero, director, anio, descripcion)
        elif opcion == "2":
            pelicula_id = input("Ingrese el ID de la película a editar: ")
            titulo = input("Ingrese el nuevo título de la película: ")
            genero = input("Ingrese el nuevo género de la película: ")
            director = input("Ingrese el nuevo director de la película: ")
            anio = input("Ingrese el nuevo año de la película: ")
            descripcion = input("Ingrese la nueva descripción de la película: ")
            admin_manager.editar_pelicula(pelicula_id, titulo, genero, director, anio, descripcion)
        elif opcion == "3":
            pelicula_id = input("Ingrese el ID de la película a eliminar: ")
            admin_manager.eliminar_pelicula(pelicula_id)
        elif opcion == "4":
            comentario_id = input("Ingrese el ID del comentario a moderar: ")
            admin_manager.moderar_comentario(comentario_id)
        elif opcion == "5":
            admin_manager.ver_peliculas()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


def main():
    usuario_manager = Usuarios()
    admin_manager = Administradores()
    
    while True:
        print("\n--- Sistema de Películas ---")
        print("1. Ingresar como usuario")
        print("2. Ingresar como administrador")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            usuario_id, es_admin = iniciar_sesion_usuario(usuario_manager)
            if usuario_id and not es_admin:
                mostrar_menu_usuario(usuario_manager, usuario_id)
        elif opcion == "2":
            usuario_id, es_admin = iniciar_sesion_admin(admin_manager)
            if usuario_id and es_admin:
                mostrar_menu_admin(admin_manager)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
