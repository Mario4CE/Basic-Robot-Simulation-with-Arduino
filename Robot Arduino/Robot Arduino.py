#Codigos de las imagenes
"""
1 = normal
2 = derecha
3 = derecha 1
4= izquierda
5 = zoom
6 = atras
9 = explo 1
10 = explo 2
11 = explo 3
12 = explo 4
13 = explo 5
14 = explo 6
"""

"""
Bibliotecas usadas
"""
import csv  # Funcion donde se guardara la informacion del robot
import os  # Ubicacio de archivos
from PIL import Image, ImageTk
import time  # Funcion para el tiempo
from tkinter import *  # Interfaz grafica
from tkinter import PhotoImage, messagebox, ttk  # interfaz grafica
import PIL.Image
import pygame  # reproductor de musica

"""	
Global variables
"""
robot_info = [] #Aqui se guardan los datos del robot

"""
Funcion que carga la imagen de fondo
"""
def Fondo(img):  
    ruta = os.path.join("Adicionales",img) 
    imagen = PhotoImage(file=ruta)
    return imagen 

def Imagenes(img,size):
    ruta = None
    if size != None:
        ruta = PIL.Image.open("Adicionales/"+img).resize((size))
    else:
        ruta = PIL.Image.open("Adicionales/"+img)
    imagen = ImageTk.PhotoImage(ruta)
    return imagen              

"""
leerRobot:Funcion que lee el archivo de texto con las caracteristica del robot
E:None
R:None
S:None
"""
def leerRobot():
    with open("robotInfo.csv",'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            robot_info.append(line)

"""
Funcion que escribe en el archivo de texto(Actualiza el archivo)
"""
def escribirR():
    with open("robotInfo.csv",'w',newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(robot_info)

"""
--> Clase que contiene los metodos para el robot
-> Contiene como metodos o funciones: 
Window: ventana principal
Y tambien todas las ordenes que se le pueden dar al robot, como "presentacion","forward","backward",
"pay_stop" y "explosion"
"""  

class Robot:
    def __init__(self,ventana_robot):
        self.ventana_robot = ventana_robot
        self.Window()

    """
    Window: ventana principal
    E: No recibe parametros
    S: No retorna nada
    R: No tiene restricciones
    """	
    def Window(self):
        self.Img = Fondo("fondo.png") 
        self.LblFondo = Label(self.ventana_robot, image = self.Img).place(x = 0,y = 0)

        if  1 == int(robot_info[0][1]): 

            self.robot1 = Imagenes("normal.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()
            time.sleep(1)
            self.robot1 = Imagenes("derecha 1.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()
            time.sleep(0.05)
            self.robot1 = Imagenes("normal.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            time.sleep(0.05)
            self.ventana_robot.update()
        
        elif int(robot_info[0][1]) == 2: 

            self.robot1 = Imagenes("derecha.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()
            time.sleep(0.05)  
            self.robot1 = Imagenes("derecha 1.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()
            time.sleep(0.05)
            self.robot1 = Imagenes("normal.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()

        elif int(robot_info[0][1]) == 3: 

            self.robot1 = Imagenes("derecha 1.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()
            time.sleep(0.05)
            self.robot1 = Imagenes("normal.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()
        
        elif int(robot_info[0][1]) == 4:

            self.robot1 = Imagenes("izquierda.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()
            time.sleep(0.05)
            self.robot1 = Imagenes("normal.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()

              
        elif int(robot_info[0][1]) == 5:

            self.robot1 = Imagenes("zoom.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()
            time.sleep(0.05)
            self.robot1 = Imagenes("normal.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()
        
        elif int(robot_info[0][1]) == 6:

            self.robot1 = Imagenes("atras.png",(250,250))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()
            time.sleep(0.05)
            self.robot1 = Imagenes("normal.png",(400,400))
            self.IMG = Label(self.ventana_robot, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.ventana_robot.update()

    """
    presentacion: Funcion que hace que el robot se presente	
    E: self
    S: Mensaje de presentacion y datos como el nombre y la fecha de su creacion.
    R: No aplica
    """
    def presentacion(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
        pygame.mixer.music.play()

        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("derecha.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.ventana_robot.update()
        time.sleep(0.05)  
        self.robot1 = Imagenes("derecha 1.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.ventana_robot.update()
        time.sleep(0.05)
        robot_info[0][1] = 3
        escribirR
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.ventana_robot.update()
        robot_info[0][1] = 1
        escribirR()
        time.sleep(0.05)

        self.Nombre = Label(self.ventana_robot, font=("Arial ",20), text="Nombre: " + robot_info[0][0]
            ,height = 1,width = 15,bg = "DeepSkyBlue4",fg = "black",justify = "left",relief = "ridge")
        self.Nombre.place(x = 50, y = 50)

        self.Fecha = Label(self.ventana_robot, font=("Arial ",20), text="Fecha de creacion: " + robot_info[0][2]
            ,height = 1,width = 35,bg = "DeepSkyBlue4",fg = "black",justify = "left",relief = "ridge")
        self.Fecha.place(x = 250, y = 50)
        time.sleep(2)
        self.ventana_robot.update()

    """
    forward: Funcion que hace que el robot se mueva hacia adelante
    E: self
    S: Mensaje de movimiento hacia adelante y el movimiento
    R: No aplica
    """
    def forward(self): 

        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
        pygame.mixer.music.play()

        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("zoom.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.ventana_robot.update()
        time.sleep(0.5)
        robot_info[0][1] = 5
        escribirR()
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.ventana_robot.update()
        robot_info[0][1] = 1
        escribirR()

    """
    backward: Funcion que hace que el robot se mueva hacia atras
    E: self
    S: Mensaje de movimiento hacia atras y el movimiento
    R: No aplica
    """
    def backward(self):

        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
        pygame.mixer.music.play()
        
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.ventana_robot.update()
        time.sleep(1)
        self.robot1 = Imagenes("atras.png",(250,250))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.ventana_robot.update()
        time.sleep(0.5)
        robot_info[0][1] = 6
        escribirR()
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.ventana_robot.update()
        robot_info[0][1] = 1
        escribirR()
    
    def play_stop():
        if true:
            pygame.mixer.init()
            pygame.mixer.music.load('Adicionales/Welcome to the Jungle.mp3')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.stop()

    #Funcion definida por el grupo
    """
    explocion: Funcion que hace que el robot explote
    E: self
    S: imagen de la explosion
    R: No aplica
    """	

    def explocion():
        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/explosion.mp3')
        pygame.mixer.music.play()

        
        self.robot1 = Imagenes("explo 1.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 250)
        self.ventana_robot.update()
        time.sleep(0.02)
        robot_info[0][1] = 9
        escribirR()
        self.robot1 = Imagenes("explo 2.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 250)
        self.ventana_robot.update()
        time.sleep(0.02)
        robot_info[0][1] = 10
        escribirR()
        self.robot1 = Imagenes("explo 3.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 250)
        self.ventana_robot.update()
        time.sleep(0.02)
        robot_info[0][1] = 11
        escribirR()
        self.robot1 = Imagenes("explo 4.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 250)
        self.ventana_robot.update()
        time.sleep(0.02)
        robot_info[0][1] = 12
        escribirR()
        self.robot1 = Imagenes("explo 5.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 250)
        self.ventana_robot.update()
        time.sleep(0.02)
        robot_info[0][1] = 13
        escribirR()
        self.robot1 = Imagenes("explo 6.png",(800,700))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 0, y = 0)
        self.ventana_robot.update()
        time.sleep(0.5)
        robot_info[0][1] = 14
        escribirR()

        self.ventana_robot.destroy()

#Parte final del codigo, aqui se implementa las condiciones para abri y cerrar la simulacion, ademas tambien se establece 
                #las funciones que se ejecutaran al mismo tiempo que el codigo

"""
Atributos o funciones en inicializarse al ejecutar el codigo
"""
leerRobot() #Se habre el archivo donde se encuentra la informacion del robot

"""
Funcion que cierra ambas ventanas cuando se cumple cierta condicion
"""
def close (): 
    escribirR() #Antes de cerrar la ventana se escribe en el archivo
    window.destroy() #Se cierra la ventana principal o donde se encuentra el robot  
"""
Lo que se ejecuta apenas se corre el codigo de las clases
"""

#Ventana principal
window = Tk()
window.geometry('1200x700+75+0') #Tamaño de la ventana
window.title("Robot Simulator using Arduiino Software") #Titulo de la ventana
window.iconbitmap('Adicionales/robot.ico') #Añade un icono distinto
window.resizable(False,False) #No permite cambiar el tamaño de la ventana
window_1 = Robot(window)

window.protocol ("WM_DELETE_WINDOW", close) #Funcion que se ejecuta al cerrar la ventana

window.mainloop() 
