import threading
from tkinter import *
import serialReading
import time

window = Tk()
window.geometry("600x600")
text1 = StringVar()
newStatus = False
def print_microbit_touched():
    print(serialReading.microbit_touched())

def show_if_mat_is_pressed():
    while True:
        status = serialReading.microbit_touched()
        global newStatus
        newStatus = status
        if status == True:
            text1.set('Pressed')
        elif status == False:
            text1.set('Not pressed')

x = Label(window, textvariable=text1, font=('Helvatical bold', 20)).place(x=50, y=100)

#Button which creates a thread to start the reading function
button = Button(window, command=serialReading.create_thread , text="Start Read").place(x = 50, y= 400)
#Button that stop the reading function that create the reading threads
button = Button(window, command=serialReading.stop_reading , text="Stop Read").place(x = 250, y= 400)

#Optional in case we want to know
#when mat is pressed without start reading
#serialReading.create_thread()
#t = threading.Thread(target=show_if_mat_is_pressed)
#t.setDaemon(False)
#t.start()

while True:
    print_microbit_touched()

window.mainloop()
