from tkinter import *

fenetre = Tk()

fenetre.title("Code Cesar")

fenetre.geometry("400x80")

						# the fonction of Code 

def Cesar_decode():

    u = []

    u = str(b.get())

    R = []

    for i in range(len(u)):

        number = ord(u[i])

        number = number - 2

        char = chr(number) 

        R = R + [(char)]

    label=Label(fenetre,text = R)
    
    label.grid(row = 2 , column = 4)

					# the fonction of decode 

def Cesar_code():

    u = []

    u = str(a.get())

    R = []

    for i in range(len(u)):

        number = ord(u[i])

        number = number + 2

        char = chr(number) 

        R = R + [(char)]

    label=Label(fenetre,text = R)
    
    label.grid(row = 0 , column = 4)

code = Label(fenetre,text = "CODE:")

code.grid(row = 0 , column = 0)

Decode = Label(fenetre,text = "DECODE:") 

Decode.grid(row = 2,column = 0)

btn1 = Button(fenetre,text = "Coder",command=Cesar_code)

btn2 = Button(fenetre,text = "DeCoder",command=Cesar_decode)

btn1.grid(row = 0 , column = 3)

btn2.grid(row = 2 , column = 3)

a = Entry(fenetre)

b = Entry(fenetre)

a.grid(row = 0 , column = 1)

b.grid(row = 2 , column = 1)

fenetre.mainloop()

