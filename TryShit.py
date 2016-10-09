import Tkinter
from Tkinter import tkMessageBox
import serial, time

master = Tkinter.Tk()

class SerialPort():
    def __init__(self):
       self.baud_rate = 115200

    def connect(self):
        #open connection
        self.serialport = serial.Serial("/dev/ttyAMA0", self.baud_rate, timeout=0.5)
    def transmit(self, data):
        self.serialport.write(data + '\r')
class Phone():
    def _init_(self,fona):
        self.fona = serialport.SerialPort()
        self.fona.transmit('AT+CHFA=0')
    def MakeCall(self):
        self.fona.transmit('ATD' + (Entry.get()) + ';')
        tkMessageBox.showinfo("Calling")
    def EndCall(self):
        self.fona.transmit('ATH')
    def CheckMessages(self):
        self.fona.transmit('AT+CPMS?')
    def IncomingCall(self):
        self.fona.transmit('ATA')
        tkMessageBox.showinfo("incoming call")
    def Contacts(self):
        entry.insert(100, "17153098886")
    def delete(self):
        entry.delete(0)

A = Tkinter.Button(master, text="Call", command = self.MakeCall())
A.grid(column=0, row=1)
B = Tkinter.Button(master, text="End", command = self.EndCall())
B.grid(column=1, row=1)
C = Tkinter.Button(master, text="Delete", command = self.delete())
C.grid(column=2, row=1)
D = Tkinter.Button(master, text="Call Me", command = self.Contacts())
D.grid(column=0, row=2)
E = Tkinter.Button(master, text="Messages", command = self.CheckMessages())
E.grid(column=1, row=2)

Entry = Tkinter.Entry(top, width= 15 ,bd=5)
Entry.grid(row=0, columnspan=4, rowspan=1)

master.mainloop()
