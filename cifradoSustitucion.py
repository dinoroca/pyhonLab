from tkinter import *
debug = False

#Función que devuelve loa caracteres mayúsculas o minúsculas
def get_alphabet():
    alphabet = []
    
    # mayusculas:65-90
    for i in range(65,91):
        alphabet.append(chr(i))
    # minusculas:97-122
    for i in range(97,123):
        alphabet.append(chr(i))
    # numeros: 48,57
    for i in range(48, 58):
        alphabet.append(chr(i))

    alphabet.append(" ")
    return alphabet


#Función que devuelve un índice válido en un rango determinado
def get_index(index = 0, length = 0):
    min_index = 0
    max_index = length - 1

    while True:
        # índice excede el limite superior
        if index > max_index:
            index -= length
        # índice es menor al limite inferior
        elif index < min_index:
            index += length
        # índice es valido
        else:
            break
    return index

class MyWindow:
    def __init__(self, win):
        self.label1 = Label(win, text = "Mensaje: ", fg = 'grey', font = ('Arial',14))
        self.label1.grid(row = 0, column = 0, padx = 5, pady = 10)

        self.texto2 = Label(win, text = "Llave: ", fg = 'orange', font = ('Arial',14))
        self.texto2.grid(row = 1, column = 0, padx = 5, pady = 10)

        self.mensaje = Entry(fg = 'black', font = ('Arial',14))
        self.mensaje.grid(row = 0, column = 1)

        self.llave = Entry(fg= 'black', font = ('Arial',14))
        self.llave.grid(row=1, column=1)

        self.b1 = Button(win, text = "Encriptar", command = self.crypt, fg = 'red', font = ('Arial', 14))
        self.b1.grid(row = 2, column = 1)

        self.b2 = Button(win, text = "Descencriptar", command = self.decrypt, fg = 'green', font = ('Arial', 14))
        self.b2.grid(row = 3, column = 1, pady = 5)

        self.label2 = Label(win, text = "Respuesta ", fg = 'grey', font = ('Arial', 12))
        self.label2.grid(row = 4, column = 1)
        self.respuesta = Text(win, width = 20, height = 5, fg = 'green', font = ('Arial', 14), padx = 5, pady = 10)
        self.respuesta.grid(row = 5, column = 1)

    #Encriptar
    def crypt(self):
        message = self.mensaje.get()
        key = int(self.llave.get()) #Convierte la llave a un entero
        crypted = ""                # mensaje cifrado vacío
        alphabet = get_alphabet()   # alfabeto
        length = len(alphabet)      # longitud del alfabeto
        index = 0                   # indice de la letra en el alfabeto
    
        for letter in message:
            # se obtiene el indice de letter dentro de alphabet, si existe
            try:        
                index = alphabet.index(letter)          # indice dentro del alfabeto
            except:
                print ("No existe %s en el alfabeto") % (letter,)
                continue
    
            # se obtiene la nueva posicion, evitando desbordamiento
            move = index + key
            move = get_index(move, length)
            if debug:
                print ("move %d") %(move,)
            crypted += alphabet[move]   # agrega la letra al mensaje cifrado
            if debug:
                print ("%s = %s") % (alphabet[index],alphabet[move])
    
        self.respuesta.insert(END, str(crypted))

    #Desencriptar
    def decrypt(self):
        message = self.mensaje.get()# Obtiene el mensaje del campo de texto
        key = int(self.llave.get()) # Obtiene la llaver del campo de texto
        decrypted = ""              # Mensaje decifrado
        alphabet = get_alphabet()   # Alfabeto
        length = len(alphabet)      # Longitud del alfabeto
        index = 0
    
        for letter in message:
            try:
                index = alphabet.index(letter)  # indice dentro del alfabeto
            except:
                print ("No existe %s en el alfabeto") % (letter,)
                continue
            move = index - key              # nueva posicion
            move = get_index(move,length)
            decrypted += alphabet[move] # agrega al mensaje decifrado

        self.respuesta.insert(END, str(decrypted))

window=Tk()
mywin=MyWindow(window)
window.title('CIFRADO POR SUSTITUCIÓN')
window.geometry("400x400+10+10")
window.mainloop()
