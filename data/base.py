import sqlite3

# Conectar a la base de datos (o crear si no existe)
conn = sqlite3.connect('peliculas.db')
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Peliculas (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        genero TEXT,
        director TEXT,
        anio INTEGER,
        descripcion TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY,
        nombre_usuario TEXT NOT NULL,
        contrasena TEXT NOT NULL,
        es_admin INTEGER DEFAULT 0
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ListasReproduccion (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        etiquetas TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Calificaciones (
        id INTEGER PRIMARY KEY,
        lista_id INTEGER,
        usuario_id INTEGER,
        calificacion TEXT CHECK(calificacion IN ('me gustó', 'no me gustó')),
        FOREIGN KEY (lista_id) REFERENCES ListasReproduccion (id),
        FOREIGN KEY (usuario_id) REFERENCES Usuarios (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Comentarios (
        id INTEGER PRIMARY KEY,
        lista_id INTEGER,
        usuario_id INTEGER,
        comentario TEXT,
        FOREIGN KEY (lista_id) REFERENCES ListasReproduccion (id),
        FOREIGN KEY (usuario_id) REFERENCES Usuarios (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Administradores (
        id INTEGER PRIMARY KEY,
        usuario_id INTEGER UNIQUE,
        FOREIGN KEY (usuario_id) REFERENCES Usuarios (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS PeliculasListas (
        lista_id INTEGER,
        pelicula_id INTEGER,
        FOREIGN KEY (lista_id) REFERENCES ListasReproduccion (id),
        FOREIGN KEY (pelicula_id) REFERENCES Peliculas (id)
);
''')


# Cerrar la conexión (esto asegura que los cambios se guarden)
conn.commit()
conn.close()

print("Base de datos 'peliculas.db' creada con éxito.")
