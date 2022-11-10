# Reference: https://pyserial.readthedocs.io/en/latest/shortintro.html
import serial

"""
class DriverSerial: esta clase se encarga de manejar la comunicación serial, comunicacion entre Arduino y Python
metedos:
    __init__(self, port, baudrate): constructor de la clase
    leer_bytes(self): lee el puerto serial
    leer(self): lee el puerto serial
    send(self, data): envia datos al puerto serial
    close(self): cierra el puerto serial
    open(self): abre el puerto serial
"""
class DriverSerial:
    def __init__(self, port, baudrate):
        self.__serial = serial.Serial("COM5",9600)
        #self.__serial = serial.Serial(port,baudrate)
        

    def read_bytes(self): #Funcion encargada de la lectura de el byte proveniente del puerto USB
        if self.__serial.inWaiting() > 0: #Revisa que el puerto este recibiendo datos
            command = self.__serial.readline() #Entonces le asigna ala variable command la lectura del puerto
            #arduino.open()
            #Comparacion de commands para realizar su respectiva funcion
            print(command)
            return command 

    
    def read(self): #Funcion encargada de la lectura de el byte proveniente del puerto USB
        encoding = 'utf-8'
        if self.__serial.inWaiting() > 0 :#Revisa que el puerto este recibiendo datos
            command = self.__serial.readline() #Entonces le asigna a la variable command la lectura del puerto
            command = command.decode(encoding)
            #Comparacion de commands para realizar su respectiva funcion
            print(command)
            return command
    
    def send(self, data): #Funcion encargada de la lectura de el byte proveniente del puerto USB
        self.__serial.write(data)

    
    def close(self):
        self.__serial.close()

    def open(self):
        self.__serial.open()


ser= DriverSerial('COM5',9600)           
while(True):
    ser.read()
