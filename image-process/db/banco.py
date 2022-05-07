import sqlite3

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def create_db(path):
    return sqlite3.connect(path)



def create_table(cursor):
    cursor.execute( "CREATE TABLE PLACAS( imagem blob, coordenadas text, imagemCinza blob, placa text)")

def insert_db(coordinates, placa, original_file, gray_file, cursor):

    sqlite_insert_blob_query = """ INSERT INTO PLACAS
                                (imagem, coordenadas, imagemCinza, placa) VALUES (?, ?, ?, ?)"""

    original_image = convertToBinaryData(original_file)
    gray_image = convertToBinaryData(gray_file)
    data_tuple = (original_image, coordinates, gray_image, placa)

    cursor.execute(sqlite_insert_blob_query, data_tuple)

def commit_db(banco):
    banco.commit()

def consulta_db(cursor):
    cursor.execute("SELECT coordenadas, placa FROM PLACAS")
    print(cursor.fetchall())

def close_db(banco):
    banco.close()