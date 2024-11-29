from cryptography.fernet import Fernet
import csv

# Generar clave de cifrado
clave = Fernet.generate_key()
cifrador = Fernet(clave)

"""
    esta funcion recibe una lista de diccionarios con los datos de los usuarios
    abre el arhivo.csv donde se va a escribir que se pasa como parametro de la funcion 
    escribe los datos de los usuarios en el archivo.csv una vez escrito los datos
    cifra el archivo.csv con la variable cifrador que pertenece a la funcion 
    Fernet y se le pasa como parametro una clave qe es la del cifrado
     y lo guarda con la extension .enc
"""
def exportar_datos(datos, archivo_csv):
    with open(archivo_csv, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['username', 'password_hash'])
        for usuario in datos:
            writer.writerow([usuario['username'], usuario['password_hash']])
    
    # Cifrar archivo
    with open(archivo_csv, 'rb') as f:
        datos_cifrados = cifrador.encrypt(f.read())
    with open(archivo_csv + '.enc', 'wb') as f:
        f.write(datos_cifrados)


"""
    esta funcion recibe un archivo.csv cifrado y una clave para descifrarlo
    al igual que en la funcion superior vovemos a usar Fernet para descifrar el archivo
    una vez descifrado el archivo se guarda en un archivo temporal para posteriormente
    se lee y se guarda en una lista de diccionarios que se retorna al final de la funcion
"""


def importar_datos(archivo_csv_enc, clave):
    cifrador = Fernet(clave)
    
    # Descifrar archivo
    with open(archivo_csv_enc, 'rb') as f:
        datos_descifrados = cifrador.decrypt(f.read())
    
    # Leer CSV descifrado
    with open('temp.csv', 'wb') as temp_file:
        temp_file.write(datos_descifrados)
    
    usuarios = []
    with open('temp.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            usuarios.append({'username': row['username'], 'password_hash': row['password_hash']})
    
    return usuarios