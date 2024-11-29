import sqlite3

"""
    esta funcion crea una base de datos sqlite3 con una tabla usuarios
    que tiene un id que es un entero autoincrementable
    un username que es un texto no nulo y unico y un password_hash que es un texto no nulo
"""

def create_connection():
    # Crear la conexión a la base de datos (se creará si no existe)
    conexion = sqlite3.connect('usuarios.db')

    # Crear un cursor para ejecutar comandos SQL
    cursor = conexion.cursor()

    # Crear la tabla de usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
    ''')

    # Confirmar los cambios
    conexion.commit()

    # Cerrar la conexión
    conexion.close()


"""
    esta funcion recibe un username y un password_hash y los inserta en la tabla usuarios
"""

def insert_user(username, password_hash):
    # Crear la conexión a la base de datos
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()

    # Insertar un usuario en la tabla
    cursor.execute('''
    INSERT INTO usuarios (username, password_hash) VALUES (?, ?)
    ''', (username, password_hash))

    # Confirmar los cambios
    conexion.commit()

    # Cerrar la conexión
    conexion.close()



"""
    esta funcion consulta todos los usuarios de la tabla usuarios
    y los retorna en una lista de tuplas
"""
def consultausuario():
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conexion.close()
    return usuarios