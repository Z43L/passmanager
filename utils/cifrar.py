import bcrypt

"""
    Funciones para cifrar usando bcrypt 
"""

def cifrar_contraseña(contrasena):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(contrasena.encode('utf-8'), salt)
    return hashed

""""
    Funcion para verificar si la contrasena ingresada es la misma que la almacenada
    en la base de datos
"""

def verificar_contraseña(contrasena, hashed):
    return bcrypt.checkpw(contrasena.encode('utf-8'), hashed)