from modulos.usuario import Usuarios

class Administradores(Usuarios):
    def __init__(self):
        super().__init__()

    def agregar_pelicula(self, titulo, genero, director, anio, descripcion):
        self.cursor.execute('INSERT INTO Peliculas (titulo, genero, director, anio, descripcion) VALUES (?, ?, ?, ?, ?)',
                           (titulo, genero, director, anio, descripcion))
        self.conn.commit()
        print("Película agregada con éxito.")

    def editar_pelicula(self, pelicula_id, titulo, genero, director, anio, descripcion):
        self.cursor.execute('UPDATE Peliculas SET titulo = ?, genero = ?, director = ?, anio = ?, descripcion = ? WHERE id = ?',
                           (titulo, genero, director, anio, descripcion, pelicula_id))
        self.conn.commit()
        print("Película editada con éxito.")

    def eliminar_pelicula(self, pelicula_id):
        self.cursor.execute('DELETE FROM Peliculas WHERE id = ?', (pelicula_id,))
        self.conn.commit()
        print("Película eliminada con éxito.")

    def moderar_comentario(self, comentario_id):
        self.cursor.execute('DELETE FROM Comentarios WHERE id = ?', (comentario_id,))
        self.conn.commit()
        print("Comentario eliminado con éxito.")

    def ver_peliculas(self):
            self.cursor.execute('SELECT id, titulo, genero, director, anio FROM Peliculas')
            peliculas = self.cursor.fetchall()

            if peliculas:
                print("Lista de Películas:")
                for pelicula in peliculas:
                    pelicula_id, titulo, genero, director, anio = pelicula
                    print("ID:", pelicula_id)
                    print("Título:", titulo)
                    print("Género:", genero)
                    print("Director:", director)
                    print("Año:", anio)
                    print("-" * 30)
            else:
                print("No hay películas en la base de datos.")
