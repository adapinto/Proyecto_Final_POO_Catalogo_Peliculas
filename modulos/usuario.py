import sqlite3
import random
import string

class Usuarios:
    def __init__(self):
        self.conn = sqlite3.connect('peliculas.db')
        self.cursor = self.conn.cursor()

    def iniciar_sesion(self, nombre_usuario, contrasena):
        self.cursor.execute('SELECT id, es_admin FROM Usuarios WHERE nombre_usuario = ? AND contrasena = ?', 
                           (nombre_usuario, contrasena))
        usuario = self.cursor.fetchone()

        if usuario:
            usuario_id, es_admin = usuario
            print("Inicio de sesión exitoso.")
            return usuario_id, es_admin
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return None, False

    def dar_like(self, usuario_id, lista_id):
        self.cursor.execute('INSERT INTO Calificaciones (lista_id, usuario_id, calificacion) VALUES (?, ?, ?)',
                           (lista_id, usuario_id, 'me gustó'))
        self.conn.commit()
        print("Has dado 'like' a la lista.")

    def dejar_comentario(self, usuario_id, lista_id, comentario):
        self.cursor.execute('INSERT INTO Comentarios (lista_id, usuario_id, comentario) VALUES (?, ?, ?)',
                           (lista_id, usuario_id, comentario))
        self.conn.commit()
        print("Comentario agregado.")
        
        
    def mostrar_lista(self, lista_id):
        self.cursor.execute('SELECT titulo, etiquetas FROM ListasReproduccion WHERE id = ?', (lista_id,))
        lista_info = self.cursor.fetchone()

        if lista_info:
            print("Título:", lista_info[0])
            print("Etiquetas:", lista_info[1])

            self.cursor.execute('SELECT pelicula_id FROM PeliculasListas WHERE lista_id = ?', (lista_id,))
            peliculas_en_lista = self.cursor.fetchall()

            if peliculas_en_lista:
                print("Películas en la lista:")
                for pelicula_id in peliculas_en_lista:
                    self.cursor.execute('SELECT titulo, genero, director, anio, descripcion FROM Peliculas WHERE id = ?', (pelicula_id[0],))
                    pelicula_info = self.cursor.fetchone()
                    print("  Título:", pelicula_info[0])
                    print("  Género:", pelicula_info[1])
                    print("  Director:", pelicula_info[2])
                    print("  Año:", pelicula_info[3])
                    print("  Descripción:", pelicula_info[4])
                    print()

                self.cursor.execute('SELECT COUNT(calificacion) FROM Calificaciones WHERE lista_id = ? AND calificacion = ?', (lista_id, 'me gustó'))
                me_gusta_count = self.cursor.fetchone()[0]

                self.cursor.execute('SELECT COUNT(calificacion) FROM Calificaciones WHERE lista_id = ? AND calificacion = ?', (lista_id, 'no me gustó'))
                no_me_gusta_count = self.cursor.fetchone()[0]

                print("Me gusta:", me_gusta_count)
                print("No me gusta:", no_me_gusta_count)

                self.cursor.execute('SELECT comentario FROM Comentarios WHERE lista_id = ?', (lista_id,))
                comentarios = self.cursor.fetchall()

                if comentarios:
                    print("Comentarios:")
                    for comentario in comentarios:
                        print("-", comentario[0])
                else:
                    print("Esta lista no tiene comentarios.")
            else:
                print("La lista está vacía.")
        else:
            print("Lista no encontrada.")


    def generar_identificador(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    def compartir_lista(self, lista_id):
        identificador = self.generar_identificador()
        print("Comparte este identificador único:", identificador)

    def agregar_pelicula_a_lista(self, usuario_id, lista_id, pelicula_id):
        self.cursor.execute('INSERT INTO PeliculasListas (lista_id, pelicula_id) VALUES (?, ?)',
                           (lista_id, pelicula_id))
        self.conn.commit()
        print("Película agregada a la lista con éxito.")

    
    def crear_lista(self, usuario_id, titulo, etiquetas, peliculas):
        self.cursor.execute('INSERT INTO ListasReproduccion (titulo, etiquetas) VALUES (?, ?)',
                       (titulo, etiquetas))
        self.conn.commit()
        lista_id = self.cursor.lastrowid

        for pelicula_id in peliculas:
            self.cursor.execute('INSERT INTO PeliculasListas (lista_id, pelicula_id) VALUES (?, ?)',
                           (lista_id, pelicula_id))
            self.conn.commit()

    print("Lista creada con éxito y películas agregadas.")

    def ver_peliculas(self):
        self.cursor.execute('SELECT id, titulo, genero, director, anio, descripcion FROM Peliculas')
        peliculas = self.cursor.fetchall()

        if peliculas:
            print("Lista de Películas Disponibles:")
            for pelicula in peliculas:
                pelicula_id, titulo, genero, director, anio, descripcion = pelicula
                print("ID:", pelicula_id)
                print("Título:", titulo)
                print("Género:", genero)
                print("Director:", director)
                print("Año:", anio)
                print("Descripción:", descripcion)
                print()
        else:
            print("No hay películas disponibles en la base de datos.")








