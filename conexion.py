import sqlite3
from tkinter import messagebox



def conection():
    conexion=sqlite3.connect("BBDDVenta")
    cursor=conexion.cursor()

    try:
        cursor.execute("CREATE TABLE USUARIO(IDUSUARIO INTEGER PRIMARY KEY AUTOINCREMENT, USUARIO VARCHAR(20) UNIQUE, PASSWORD VARCHAR(20), ESTADO INTEGER )")
        messagebox.showinfo("BBDD","Base de datos conectada")
    except:
        messagebox.showinfo("BBDD","ya existe la coneccion a base de datos")

