#Codigos de las self.Imagenes
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
from PIL import Image, ImageTk # Libreria para manejar self.Imagenes
import time  # Funcion para el tiempo
from tkinter import *  # Interfaz grafica
from tkinter import PhotoImage, messagebox, ttk  # interfaz grafica
import PIL.Image # Libreria para manejar self.Imagenes
import pygame  # reproductor de musica
from DriverSerial import DriverSerial # Doc .py para manejar el puerto serial
from threading import Thread # Hilos
import threading

"""	
Global variables
"""
robot_info = [] #Aqui se guardan los datos del robot

"""
--> Clase que contiene los metodos para el robot
-> Contiene como metodos o funciones: 
Window: ventana principal
Y tambien todas las ordenes que se le pueden dar al robot, como "presentacion","forward","backward",
"pay_stop" y "explosion"
"""  

class RobotArduino:
    def __init__(self,COM,baudrate):
        self.__serial = DriverSerial(COM, baudrate) 
        self.__window = None

    """
    Funcion que carga la imagen de fondo
    """
    def Fondo(self,img):  
        ruta = os.path.join("Adicionales",img) 
        imagen = PhotoImage(file=ruta)
        return imagen 

    def Imagenes(self,img,size):
        ruta = None
        if size != None:
            ruta = PIL.Image.open("Adicionales/"+img).resize((size))
        imagen = ImageTk.PhotoImage(ruta)
        return imagen             

    """
    leerRobot:Funcion que lee el archivo de texto con las caracteristica del robot
    E:None
    R:None
    S:None
    """
    def leerRobot(self):
        with open("robotInfo.csv",'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                robot_info.append(line)

    """
    Funcion que escribe en el archivo de texto(Actualiza el archivo)
    """
    def escribirR(self):
        with open("robotInfo.csv",'w',newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(robot_info)


        """
        Window: ventana principal
        E: No recibe parametros
        S: No retorna nada
        R: No tiene restricciones
        """	
    def Window(self):

        self.__window = Tk()
        self.__window.title("Robot")
        self.__window.geometry('1200x700+50+0')
        self.__window.resizable(0,0)
        self.__window.configure(background="black")
        self.__window.iconbitmap("Adicionales/robot.ico")

        self.Img = self.Fondo("fondo.png") 
        self.LblFondo = Label(self.__window, image = self.Img).place(x = 0,y = 0)  

        if  robot_info[0][1] == str(1): 

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.__window.update()
            time.sleep(1)

            self.robot1 = self.Imagenes("derecha 1.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.__window.update()
            time.sleep(0.05)
            robot_info[0][1] = 3
            self.escribirR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            time.sleep(0.05)
            robot_info[0][1] = 1
            self.escribirR()

            self.__window.update()
        
        elif int(robot_info[0][1]) == 2: 

            self.robot1 = self.Imagenes("derecha.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.__window.update()
            time.sleep(0.05)  
            robot_info[0][1] = 2
            self.escribirR()

            self.robot1 = self.Imagenes("derecha 1.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.__window.update()
            time.sleep(0.05)
            robot_info[0][1] = 3
            self.escribirR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()

        elif int(robot_info[0][1]) == 3: 

            self.robot1 = self.Imagenes("derecha 1.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.__window.update()
            time.sleep(0.05)
            robot_info[0][1] = 3
            self.escribirR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()
        
        elif int(robot_info[0][1]) == 4:

            self.robot1 = self.Imagenes("izquierda.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.__window.update()
            time.sleep(0.05)
            robot_info[0][1] = 4
            self.escribirR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()

            
        elif int(robot_info[0][1]) == 5:

            self.robot1 = self.Imagenes("zoom.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.__window.update()
            time.sleep(0.5)
            robot_info[0][1] = 5
            self.escribirR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()
        
        elif int(robot_info[0][1]) == 6:

            self.robot1 = self.Imagenes("atras.png",(250,250))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            self.__window.update()
            time.sleep(0.5)
            robot_info[0][1] = 6
            self.escribirR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()
        
        elif int(robot_info[0][1]) == 9:
                
            pygame.mixer.init()
            pygame.mixer.music.load('Adicionales/explosion.mp3')
            pygame.mixer.music.play()

            
            self.robot1 = self.Imagenes("explo 1.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 9
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 2.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 10
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 3.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 11
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 4.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 12
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 5.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 13
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 6.png",(800,700))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 0, y = 0)
            self.__window.update()
            time.sleep(0.5)
            robot_info[0][1] = 14
            self.escribirRR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()
        
        elif int(robot_info[0][1]) == 10:

            self.robot1 = self.Imagenes("explo 2.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 10
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 3.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 11
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 4.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 12
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 5.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 13
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 6.png",(800,700))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 0, y = 0)
            self.__window.update()
            time.sleep(0.5)
            robot_info[0][1] = 14
            self.escribirRR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()

        elif int(robot_info[0][1]) == 11:

            self.robot1 = self.Imagenes("explo 3.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 11
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 4.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 12
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 5.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 13
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 6.png",(800,700))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 0, y = 0)
            self.__window.update()
            time.sleep(0.5)
            robot_info[0][1] = 14
            self.escribirRR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()
        
        elif int(robot_info[0][1]) == 12:

            self.robot1 = self.Imagenes("explo 4.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 12
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 5.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 13
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 6.png",(800,700))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 0, y = 0)
            self.__window.update()
            time.sleep(0.5)
            robot_info[0][1] = 14
            self.escribirRR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()
        
        elif int(robot_info[0][1]) == 13:

            self.robot1 = self.Imagenes("explo 5.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 200, y = 250)
            self.__window.update()
            time.sleep(0.02)
            robot_info[0][1] = 13
            self.escribirRR()

            self.robot1 = self.Imagenes("explo 6.png",(800,700))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 0, y = 0)
            self.__window.update()
            time.sleep(0.5)
            robot_info[0][1] = 14
            self.escribirRR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()
        
        elif int(robot_info[0][1]) == 14:

            self.robot1 = self.Imagenes("explo 6.png",(800,700))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 0, y = 0)
            self.__window.update()
            time.sleep(0.5)
            robot_info[0][1] = 14
            self.escribirRR()

            self.robot1 = self.Imagenes("normal.png",(400,400))
            self.IMG = Label(self.__window, image = self.robot1)
            self.IMG.place(x = 500, y = 250)
            robot_info[0][1] = 1
            self.escribirR()
            self.__window.update()
               
        self.__window.mainloop()

            

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

        self.robot1 = self.Imagenes("normal.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.__window.update()
        time.sleep(0.05)
        self.robot1 = self.Imagenes("derecha.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.__window.update()
        time.sleep(0.05)  
        robot_info[0][1] = 2
        self.escribirRR()

        self.robot1 = self.Imagenes("derecha 1.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.__window.update()
        time.sleep(0.05)
        robot_info[0][1] = 3
        self.escribirRR

        self.robot1 = self.Imagenes("normal.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.__window.update()
        robot_info[0][1] = 1
        self.escribirRR()
        time.sleep(0.05)

        self.Nombre = Label(self.__window, font=("Arial ",20), text="Nombre: " + robot_info[0][0]
            ,height = 1,width = 15,bg = "DeepSkyBlue4",fg = "black",justify = "left",relief = "ridge")
        self.Nombre.place(x = 50, y = 50)

        self.Fecha = Label(self.__window, font=("Arial ",20), text="Fecha de creacion: " + robot_info[0][2]
            ,height = 1,width = 35,bg = "DeepSkyBlue4",fg = "black",justify = "left",relief = "ridge")
        self.Fecha.place(x = 250, y = 50)
        time.sleep(2)
        self.__window.update()

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

        self.robot1 = self.Imagenes("normal.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.__window.update()
        time.sleep(0.05)
        self.robot1 = self.Imagenes("zoom.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.__window.update()
        time.sleep(0.5)
        robot_info[0][1] = 5
        self.escribirRR()

        self.robot1 = self.Imagenes("normal.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.__window.update()
        robot_info[0][1] = 1
        self.escribirRR()

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
        
        self.robot1 = self.Imagenes("normal.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.__window.update()
        time.sleep(1)

        self.robot1 = self.Imagenes("atras.png",(250,250))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.__window.update()
        time.sleep(0.5)
        robot_info[0][1] = 6
        self.escribirRR()

        self.robot1 = self.Imagenes("normal.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 500, y = 250)
        self.__window.update()
        robot_info[0][1] = 1
        self.escribirRR()
    
    def play_stop(self):
        if true:
            pygame.mixer.init()
            pygame.mixer.music.load('Adicionales/Welcome to the Jungle.mp3')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.stop()

    #Funcion adicional solicitada por el profesor
    """
    explocion: Funcion que hace que el robot explote
    E: self
    S: imagen de la explosion
    R: No aplica
    """	

    def explocion(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/explosion sonido.mp3')
        pygame.mixer.music.play()

        
        self.robot1 = self.Imagenes("explo 1.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 200, y = 250)
        self.__window.update()
        time.sleep(0.02)
        robot_info[0][1] = 9
        self.escribirRR()

        self.robot1 = self.Imagenes("explo 2.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 200, y = 250)
        self.__window.update()
        time.sleep(0.02)
        robot_info[0][1] = 10
        self.escribirRR()

        self.robot1 = self.Imagenes("explo 3.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 200, y = 250)
        self.__window.update()
        time.sleep(0.02)
        robot_info[0][1] = 11
        self.escribirRR()

        self.robot1 = self.Imagenes("explo 4.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 200, y = 250)
        self.__window.update()
        time.sleep(0.02)
        robot_info[0][1] = 12
        self.escribirRR()

        self.robot1 = self.Imagenes("explo 5.png",(400,400))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 200, y = 250)
        self.__window.update()
        time.sleep(0.02)
        robot_info[0][1] = 13
        self.escribirRR()

        self.robot1 = self.Imagenes("explo 6.png",(800,700))
        self.IMG = Label(self.__window, image = self.robot1)
        self.IMG.place(x = 0, y = 0)
        self.__window.update()
        time.sleep(0.5)
        robot_info[0][1] = 14
        self.escribirRR()
    
        self.__window.mainloop()
    
            
#Funcion principal
    def readSerial(self):
        while(True):
            command= self.__serial.read()
            self.__compareSerial(command)

    def sendSerial(self):
        command= self.__serial.send('hola'.encode())

    def th_receiveData(self):
        th_time=Thread(target = self.readSerial, args=())
        th_time.start()

    def th_sendData(self):
        th_time=Thread(target = self.sendSerial, args=())
        th_time.start()

    def closeSerial(self):
        self.__serial.close()

    """
    __compareSerial: Funcion que compara el comando recibido con los comandos que se pueden ejecutar
    """
    def __compareSerial(self, command):
        if(command!=None):
            if(command =='B1\r\n'):
                print("PRESENTACION")
                self.presentacion()
                
            elif(command=="B2\r\n"):
                print("BACKWARD")
                self.backward()
                
            elif(command=="B3\r\n"):
                print("FORWARD")
                self.forward()
                
            elif(command=="B4\r\n"):
                print("PLAY|STOP")
                self.play_stop()
                            
            elif(command=="B5\r\n"):
                print("EXPLOSION")
                self.explocion()
            else:
                print(command)

"""	
Parte final del codigo, aqui se implementa las condiciones para abri y cerrar la simulacion, ademas tambien se establece 
                las funciones que se ejecutaran al mismo tiempo que el codigo
"""
x = RobotArduino("COM6",9600) #Se crea un objeto de la clase Robot
x.leerRobot() #Se ejecuta la funcion leerRobot de la clase Robot
x.Window() #Se ejecuta la funcion Window de la clase Robot
x.th_receiveData() #Se ejecuta la funcion th_receiveData de la clase Robot
x.th_sendData() #Se ejecuta la funcion th_sendData de la clase Robot



     


