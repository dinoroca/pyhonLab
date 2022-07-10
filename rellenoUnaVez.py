from tkinter import *
from operator import xor
import string
import random

class Principal:
    def __init__(self, win):
        self.titulo = Label(win, text = "Ingrese el texto a cifrar ", fg = 'green', font = ('Arial', 14))
        self.titulo.grid(row=0, column=1, padx=5, pady=10)

        self.texto1 = Label(win, text = "Ingrese: ", fg = 'green', font = ('Arial',12))
        self.texto1.grid(row = 1, column = 0, padx = 5, pady = 10)

        self.entrada = Entry(fg = 'black', font = ('Arial',14))
        self.entrada.grid(row = 1, column = 1)

        self.bCifrar = Button(win, text = "Cifrar", command = self.cifrar, fg = 'blue', font = ('Arial', 14))
        self.bCifrar.grid(row = 2, column = 1, pady = 5)

        self.resLabel = Label(win, text = "Resultado", fg = 'red', font = ('Arial',12))
        self.resLabel.grid(row = 3, column = 1)

        self.resultado = Text(win, width = 20, height = 5, fg = 'green', font = ('Arial', 14), padx = 5, pady = 10)
        self.resultado.grid(row = 4, column = 1)

    #Cifrar
    def cifrar(self):
        texto_plano = self.entrada.get()

        self.resultado.insert(END, '')

        print("Ingresado: ", texto_plano)

        # Se llama a la función definida
        texto_plano_bin = convertidorBinario(texto_plano)
        print("Plano bin: ", texto_plano_bin)

        aleatorio_bin = ''

        # Generador de caracteres de longitud del ingresado
        for x in range(1):
            aleatorio = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(texto_plano)))
            print("Complemento: ", aleatorio)
            aleatorio_bin = convertidorBinario(aleatorio)

        print("Complemento bin: ", aleatorio_bin)

        arr_bin = [ord(a) ^ ord(b) for a, b in zip(texto_plano_bin, aleatorio_bin)]
        encriptado_bin = "".join(map(str, arr_bin))

        print("Encriptado bin: ", encriptado_bin)
        texto_encriptado = ''
        texto_encriptado = binarioToString(encriptado_bin)
        print("Cifrado: ", texto_encriptado)

        self.resultado.insert(END, ('-', texto_encriptado))

#Función que convierte texto a arreglo de binarios
def convertidorBinario(texto):
    convertido = ''.join(format(c, 'b') for c in bytearray(texto, "utf-8"))
    return convertido

#Función que convierte binario a texto ASCII
def binarioToString(s):
    return ''.join(chr(int(s[i*7:i*7+7], 2)) for i in range(len(s)//7))

root=Tk()
mywin=Principal(root)
root.title('RELLENO DE UNA SOLA VEZ')
root.geometry("400x350+10+10")
root.mainloop()