import sqlite3


def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def create_db():
    banco = sqlite3.connect('db/banco_pardal.db')
    return banco.cursor()


def create_table(cursor):
    cursor.execute( "CREATE TABLE CARROS( imagem blob, coordenadas integer, imagemCinza blob, placa text)")

def insert_db(original_image, coordinates, gray_image, placa, file, cursor, banco):
    sqlite_insert_blob_query = """ INSERT INTO CARROS
                                (imagem, coordenadas, imagemCinza, placa) VALUES (?, ?, ?, ?)"""

    original_image = convertToBinaryData(f'{file}.jpg')
    gray_image = convertToBinaryData(f'{file}.jpg')
    data_tuple = (original_image, coordinates, gray_image, placa)

    cursor.execute(sqlite_insert_blob_query, data_tuple)

    banco.commit()

def consulta_db(cursor):
    cursor.execute("SELECT * FROM CARROS")
    print(cursor.fetchall())