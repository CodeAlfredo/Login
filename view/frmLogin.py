from tkinter import *


def frame():
    root = Tk()
    root.title("Login")

    frm1 = Frame(root, width=300, height=300)
    frm1.pack()

    tituloLabel = Label(frm1, text="sistema de autenticacion", fg="green")
    tituloLabel.grid(row=0, column=0, columnspan=3)

    # --------------------- LABELS -----------------------------------

    usuarioLabel = Label(frm1, text="Usuario: ")
    usuarioLabel.grid(row=1, column=0, pady=10, padx=10)

    passworLabel = Label(frm1, text="Clave: ")
    passworLabel.grid(row=2, column=0, pady=10, padx=10)

    # --------------------- CAJA DE TEXTOS -----------------------------------
    tituloText = Entry(frm1)
    tituloText.grid(row=1, column=2)

    passwordText = Entry(frm1)
    passwordText.grid(row=2, column=2)

    # ---------------------   BOTONES -----------------------------------

    btnOk = Button(frm1, text="OK")
    btnOk.grid(row=3, column=1)

    btnCancel = Button(frm1, text="Cancel")
    btnCancel.grid(row=3, column=2)

    root.mainloop()