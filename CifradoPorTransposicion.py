from tkinter import *
import math

class MyWindow:
    def __init__(self,win):
        self.label1 = Label(win, text="Mensaje: ", fg='grey', font=('Arial', 14))
        self.label1.grid(row=0, column=0, padx=5, pady=10)

        self.texto2 = Label(win, text="Llave: ", fg='orange', font=('Arial', 14))
        self.texto2.grid(row=1, column=0, padx=5, pady=10)

        self.mensaje = Entry(fg='black', font=('Arial', 14))
        self.mensaje.grid(row=0, column=1)

        self.llave = Entry(fg='black', font=('Arial', 14))
        self.llave.grid(row=1, column=1)

        self.b1 = Button(win, text="Encriptar", command=self.crypt, fg='red', font=('Arial', 14))
        self.b1.grid(row=2, column=1)

        self.b2 = Button(win, text="Descencriptar", command=self.decrypt, fg='green', font=('Arial', 14))
        self.b2.grid(row=3, column=1, pady=5)

        self.label2 = Label(win, text="Respuesta ", fg='grey', font=('Arial', 12))
        self.label2.grid(row=4, column=1)
        self.respuesta = Text(win, width=20, height=5, fg='green', font=('Arial', 14), padx=5, pady=10)
        self.respuesta.grid(row=5, column=1)

    #Encriptar
    def crypt(self):
        texto = self.mensaje.get()  #Obtiene el mensaje de la interfaz
        key = int(self.llave.get()) #Obtiene la lave de la interfaz
        cifrado = [" "] * key       # Se define el texto cifrado como vacío
        for col in range(key):      #Se itera hasta el rango de la llave
            caracter = col
            while caracter < len(texto):
                cifrado[col] += texto[caracter]
                caracter += key
        cifrado = list(map(lambda x: x.strip(), cifrado)) #Se enlista los caracteres obtenidos
        resultado = "".join(cifrado)
        self.respuesta.insert(END, str(resultado))

    #Desencriptar
    def decrypt(self):
        texto = self.mensaje.get()  #Se obtiene el mensaje
        key = int(self.llave.get()) #Se obtiene la llave
        numCols = math.ceil(len(texto) / key) #Se asigna numero de columnas
        numRows = key #Se asigna el numero de filas
        numShadedBoxes = (numCols * numRows) - len(texto)
        plainText = [" "] * numCols
        col = 0; row = 0;
        for symbol in texto: #Se itera en función al numero de columnas y filas
            plainText[col] += symbol
            col += 1
            if (col == numCols) or (col == numCols - 1) and (row >= numRows - numShadedBoxes):
                col = 0
                row += 1
        plainText = list(map(lambda x: x.strip(), plainText))
        resultado = "".join(plainText)
        self.respuesta.insert(END, str(resultado))


window=Tk()
mywin=MyWindow(window)
window.title('CIFRADO POR TRANSPOSICIÓN')
window.geometry("400x400+10+10")
window.mainloop()