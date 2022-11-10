from DriverSerial import DriverSerial
from threading import Thread
import threading
import time

class Game:
    def __init__(self,COM,baudrate):
        self.__serial = DriverSerial(COM, baudrate) 
        self.__window = None

      #Funcion principal
    def main(self):
        def readSerial():
            while(True):
                command= self.__serial.read()
                self.__compareSerial(command)

        def sendSerial():
            command= self.__serial.send('hola'.encode())

        def th_receiveData():
            th_time=Thread(target=readSerial, args=())
            th_time.start()

        def th_sendData():
            th_time=Thread(target=sendSerial, args=())
            th_time.start()

        def closeSerial():
            self.__serial.close()

    """
    __compareSerial: Funcion que compara el comando recibido con los comandos que se pueden ejecutar
    """
    def __compareSerial(self, command):
        if(command!=None):
            if(command =='B1\r\n'):
                print("PRESENTACION")
                presentacion()
                
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

        
x = Game("COM5",9600) #Aqui se debe de cambiar dependiendo del puerto que tengas en Aurdino
x.main()