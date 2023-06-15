from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import datetime
import pygame
import time
import threading

pygame.mixer.init()

'''
Esta función se encarga de crear la ventana principal, donde se muestra la consola de comandos y el robot virtual.
Parámetros:
    None
Retorna:
    No retorna 
'''
def ventana():
    ventana = Tk()
    ventana.title('Robot Virtual')
    ventana.minsize(1280, 720)
    ventana.resizable(width=NO, height=NO)
    ventana.configure(background='#C3DFF4')
    
    canvas = Canvas(ventana, width=450, height=400, background='#7293C4')
    canvas.place(x=40, y=150)
    canvas2 = Canvas(ventana, width=650, height=600, background='White')
    canvas2.place(x=600, y=50)
    
    '''
    Objeto Robot
    atributos: ventana, nombre (str), imagen, fecha_creacion (str), felicidad (int), contador (int), anim (boolean)
    metódos:
    hello_ani(): se encarga de crear la animación del robot saludando
    sayhello(): muestra en un messagebox  el nombre del robot y llama a la función hello_ani
    built(): muestra en un messagebox la fecha y la hora en la que se ejecutó el programa
    forward_ani(): se encarga de crear la animación del robot caminando hacia adelante
    forward(): cambia la imagen del robot para que este mire hacia adelante
    backward_ani(): se encarga de crear la animación del robot caminando hacia atrás
    backward(): cambia la imagen del robot para que este mire hacia atrás
    stop(): se encarga de detener cualquier animación
    turnRight(): cambia la imagen del robot para que este mire hacia la derecha
    turnLeft(): cambia la imagen del robot para que este mire hacia la izquierda
    dance_ani(): se encarga de crear la animación del robot bailando
    dance(): se encarga de llamar a la funcion dance_ani
    music_on(): carga un archivo mp3 y lo reproduce
    music_off(): detiene la reproducción del archivo mp3 y lo cierra
    smile_ani(): se encarga de crear la animacion del robot sonriendo
    smile(): aumenta la felicidad en 5 si esta es menor a 100 y llama a la funcion smile_ani
    cry_ani(): se encarga de crear la animacion del robot llorando
    cry(): decrementa la felicidad en 5 si esta es mayor a 0 y llama a la funcion smile_ani
    save(): se encarga de guardar el estado del robot
    '''
    class Robot:
        def __init__(self, ventana, nombre, imagen, contador, anim):
            self.ventana = ventana
            self.nombre = nombre
            self.imagen = imagen
            self.contador = contador
            self.anim = anim

        def hello_ani(self):
            self.anim = True
            canvas2.delete('imgR')
            while self.contador != 12:
                if self.anim == False:
                    break
                nombre = 'Imagenes/wave/wave'+str(self.contador)+'.jpg'
                imgR = ImageTk.PhotoImage(Image.open(nombre).resize((700,400)))
                canvas2.create_image(0,100, image=imgR, anchor=NW, tag='imgR')
                self.contador+=1
                time.sleep(0.15)
                canvas2.delete('imgR')
            self.contador = 1
            canvas2.create_image(0, 100, image=self.imagen, anchor=NW)

        def sayhello(self):
            messagebox.showinfo(title='Nombre:', message='Hola! Mi nombre es ' + str(self.nombre))
            threading.Thread(target=self.hello_ani).start()
        
        def forward_ani(self):
            self.anim = True
            canvas2.delete('imgR')
            while self.contador != 22:
                if self.contador == 21:
                    self.contador = 1
                if self.anim == False:
                    break
                nombre = 'Imagenes/walkF/walkF'+str(self.contador)+'.jpg'
                imgR = ImageTk.PhotoImage(Image.open(nombre).resize((700,400)))
                canvas2.create_image(0, 100, image=imgR, anchor=NW, tag='imgR')
                self.contador+=1
                time.sleep(0.15)
                canvas2.delete('imgR')
            self.contador = 1
            canvas2.create_image(0, 100, image=self.imagen, anchor=NW)

        def forward(self):
            canvas2.delete('imgR')
            self.imagen = ImageTk.PhotoImage(Image.open('Imagenes/defaultF.png').resize((700,400)))
            canvas2.create_image(0,100, image=self.imagen, anchor=NW, tag='imgR')
            threading.Thread(target=self.forward_ani).start()

        def backward_ani(self):
            self.anim = True
            canvas2.delete('imgR')
            while self.contador != 22:
                if self.contador == 21:
                    self.contador = 1
                if self.anim == False:
                    break
                nombre = 'Imagenes/walkB/walkB'+str(self.contador)+'.jpg'
                imgR = ImageTk.PhotoImage(Image.open(nombre).resize((700,400)))
                canvas2.create_image(0, 100, image=imgR, anchor=NW, tag='imgR')
                self.contador+=1
                time.sleep(0.15)
                canvas2.delete('imgR')
            self.contador = 1
            canvas2.create_image(0, 100, image=self.imagen, anchor=NW)

        def backward(self):
            canvas2.delete('imgR')
            self.imagen = ImageTk.PhotoImage(Image.open('Imagenes/defaultB.png').resize((700,400)))
            canvas2.create_image(0,100, image=self.imagen, anchor=NW, tag='imgR')
            threading.Thread(target=self.backward_ani).start()

        def stop(self):
            self.anim = False
        
        def dance_ani(self):
            self.anim = True
            canvas2.delete('imgR')
            while self.contador != 64:
                if self.contador == 63:
                    self.contador = 1
                if self.anim == False:
                    break
                nombre = 'Imagenes/dance/dance ('+str(self.contador)+').jpg'
                imgR = ImageTk.PhotoImage(Image.open(nombre).resize((700,400)))
                canvas2.create_image(0, 100, image=imgR, anchor=NW, tag='imgR')
                self.contador+=1
                time.sleep(0.15)
                canvas2.delete('imgR')
            self.contador = 1
            canvas2.create_image(0, 100, image=self.imagen, anchor=NW)

        def dance(self):
            threading.Thread(target=self.dance_ani).start()

        def music_on(self):
            pygame.mixer.music.load('aespa.mp3')
            pygame.mixer.music.play()
        
        def music_off(self):
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

    '''
    Esta función se encarga de recibir un dato por medio de una entry y devuelve uno de los métodos del objeto robot segun lo que se introdujo en la entry
    Parámetros:
        None
    Retorna:
        No retorna 
    '''        
    def aceptar():
        comando = consola.get()
        if comando == 'sayhello':
            R.sayhello()
        if comando == 'forward':
            R.forward()
        if comando == 'backward':
            R.backward()
        if comando == 'stop':
            R.stop()
        if comando == 'dance':
            R.dance()
        if comando == 'music_on':
            R.music_on()
        if comando == 'music_off':
            R.music_off()

    
    Label0 = Label(canvas, text='Consola de comandos', bg='#A2C4EC', fg='#383A3D', font=('Baskerville Old Face', 10))
    Label0.place(x=20, y=10)
    Label1 = Label(canvas, text='Los comandos disponibles son: ', bg='#A2C4EC', fg='#383A3D', font=('Baskerville Old Face', 10), width=25)
    Label2 = Label(canvas, text='- sayhello\n- forward\n- backward\n- stop\n- dance\n- music_on\n- music_off', bg='#A2C4EC', width=10, justify=LEFT, fg='#383A3D', font=('Baskerville Old Face', 10), anchor='w')
    Label1.place(x=20, y=120)
    Label2.place(x=110, y=150)

    consola = Entry(canvas, bg='#A2C4EC')
    consola.place(x=20, y=35)
    
    btn = Button(canvas, text='Aceptar', bg='#A2C4EC', fg='#383A3D', font=('Baskerville Old Face', 10), command=aceptar)
    btn.place(x=60, y=60)

    imgR = ImageTk.PhotoImage(Image.open('Imagenes/defaultF.png').resize((700,400)))
    canvas2.create_image(0,100, image=imgR, anchor=NW, tag='imgR')
    R = Robot(ventana, 'Linaria', imgR, 1, False)
    ventana.mainloop()

ventana()