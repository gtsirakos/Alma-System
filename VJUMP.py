
import threading
from tkinter import Toplevel, Button, Tk, Menu, messagebox
from functools import partial
from tkinter import*
import tkinter.font as TkFont
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from datetime import date
import time
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from reportlab.pdfgen import canvas
import numpy as np
from datetime import date
import time, queue
import serialReading
import functions as serialFunctions


top = Tk()
top.geometry("900x600+500+100")
top.title('ΑΞΙΟΛΟΓΗΣΗ ΚΑΤΑΚΟΡΥΦΩΝ ΑΛΜΑΤΩΝ - Copyright Dimitrios K. Tsirakos 2020')
top.iconbitmap('./1.ico')
logo = "./21.png"
image = tk.PhotoImage(file=logo)
label = tk.Label(image=image).place(x=650, y=20)

logo1 = "./2.png"
image1 = tk.PhotoImage(file=logo1)
label = tk.Label(image=image1).place(x=650, y=100)

t_initial=0
t_impulse=None
t_flight=None
ver_jump=0

serialReading.create_thread()

# DEFS FOR MENU SIMPLE VERTICAL JUMPS
def  data_kouti(surname, name, sclub,sport, ybirth, weight, height,pbjump, email,dokimasia):
                root1 = Tk()
                root1.geometry('500x260+550+200')
                root1.title('ΚΑΤΑΧΩΡΗΣΗ ΔΕΔΟΜΕΝΩΝ ΑΘΛΗΤΩΝ')
                root1.iconbitmap('./1.ico')
                surname = StringVar(root1)
                name = StringVar(root1)
                sclub = StringVar(root1)
                sport = StringVar(root1)
                ybirth = StringVar(root1)
                weight = StringVar(root1)
                height = StringVar(root1)
                pbjump = StringVar(root1)
                email = StringVar(root1)
                a11 = Label(root1, text="ΔΟΚΙΜΑΣΙΑ").place(x=10, y=5)
                a111 = Label(root1, text= dokimasia).place(x=150, y=5)

                a1 = Label(root1, text="ΕΠΩΝΥΜΟ").place(x=10, y=30)
                a2 = Label(root1, text="ΟΝΟΜΑ").place(x=10, y=50)
                a3 = Label(root1, text="ΑΘ. ΣΥΛΛΟΓΟΣ").place(x=10, y=70)
                a4 = Label(root1, text="ΑΓΩΝΙΣΜΑ").place(x=10, y=90)
                a5 = Label(root1, text="ΕΤΟΣ ΓΕΝΝΗΣΗΣ").place(x=10, y=110)
                a6 = Label(root1, text="ΜΑΖΑ - ΒΑΡΟΣ").place(x=10, y=130)
                a61 = Label(root1, text=" (Kgr)").place(x=220, y=130)
                a7 = Label(root1, text="ΥΨΟΣ   ").place(x=10, y=150)
                a71 = Label(root1, text=" (cm)").place(x=220, y=150)
                a8 = Label(root1, text="PB ΚΑΘ.ΑΛΜΑ  ").place(x=10, y=170)
                a81 = Label(root1, text="(cm))").place(x=220, y=170)
                a9 = Label(root1, text="EMAIL").place(x=10, y=190)

                a1 = Entry(root1, width=50, textvariable=surname).place(x=150, y=30)
                a2 = Entry(root1, width=50, textvariable=name).place(x=150, y=50)
                a3 = Entry(root1, width=50, textvariable=sclub).place(x=150, y=70)
                a4 = Entry(root1, width=50, textvariable=sport).place(x=150, y=90)
                a5 = Entry(root1, width=10, textvariable=ybirth).place(x=150, y=110)
                a6 = Entry(root1, width=10, textvariable=weight).place(x=150, y=130)
                a7 = Entry(root1, width=10, textvariable=height).place(x=150, y=150)
                a8 = Entry(root1, width=10, textvariable=pbjump).place(x=150, y=170)
                a9 = Entry(root1, width=50, textvariable=email).place(x=150, y=190)
                # 2. CALLS PERSONAL DATA KATAXORISI ROUTINE
                b1 = Button(root1, text="ΚΑΤΑΧΩΡΗΣΗ ΔΕΔΟΜΕΝΩΝ", command=partial(kataxorisi_data,surname,name,sclub,
                                                                               sport,ybirth,weight,height,pbjump,email,dokimasia),bg='red').place(x=180, y=220)
                exit
                root1.mainloop()

def  data_kouti_drop(surname, name, sclub,sport, ybirth, weight, height,pbjump, email,dokimasia):
                root1 = Tk()
                root1.geometry('500x260+550+200')
                root1.title('ΚΑΤΑΧΩΡΗΣΗ ΔΕΔΟΜΕΝΩΝ ΑΘΛΗΤΩΝ')
                root1.iconbitmap('./1.ico')
                surname = StringVar(root1)
                name = StringVar(root1)
                sclub = StringVar(root1)
                sport = StringVar(root1)
                ybirth = StringVar(root1)
                weight = StringVar(root1)
                height = StringVar(root1)
                pbjump = StringVar(root1)
                email = StringVar(root1)
                a11 = Label(root1, text="ΔΟΚΙΜΑΣΙΑ").place(x=10, y=5)
                a111 = Label(root1, text= dokimasia).place(x=150, y=5)

                a1 = Label(root1, text="ΕΠΩΝΥΜΟ").place(x=10, y=30)
                a2 = Label(root1, text="ΟΝΟΜΑ").place(x=10, y=50)
                a3 = Label(root1, text="ΑΘ. ΣΥΛΛΟΓΟΣ").place(x=10, y=70)
                a4 = Label(root1, text="ΑΓΩΝΙΣΜΑ").place(x=10, y=90)
                a5 = Label(root1, text="ΕΤΟΣ ΓΕΝΝΗΣΗΣ").place(x=10, y=110)
                a6 = Label(root1, text="ΜΑΖΑ - ΒΑΡΟΣ").place(x=10, y=130)
                a61 = Label(root1, text=" (Kgr)").place(x=220, y=130)
                a7 = Label(root1, text="ΥΨΟΣ   ").place(x=10, y=150)
                a71 = Label(root1, text=" (cm)").place(x=220, y=150)
                a8 = Label(root1, text="PB ΚΑΘ.ΑΛΜΑ  ").place(x=10, y=170)
                a81 = Label(root1, text="(cm))").place(x=220, y=170)
                a9 = Label(root1, text="EMAIL").place(x=10, y=190)

                a1 = Entry(root1, width=50, textvariable=surname).place(x=150, y=30)
                a2 = Entry(root1, width=50, textvariable=name).place(x=150, y=50)
                a3 = Entry(root1, width=50, textvariable=sclub).place(x=150, y=70)
                a4 = Entry(root1, width=50, textvariable=sport).place(x=150, y=90)
                a5 = Entry(root1, width=10, textvariable=ybirth).place(x=150, y=110)
                a6 = Entry(root1, width=10, textvariable=weight).place(x=150, y=130)
                a7 = Entry(root1, width=10, textvariable=height).place(x=150, y=150)
                a8 = Entry(root1, width=10, textvariable=pbjump).place(x=150, y=170)
                a9 = Entry(root1, width=50, textvariable=email).place(x=150, y=190)
                # 2. CALLS PERSONAL DATA KATAXORISI ROUTINE
                b1 = Button(root1, text="ΚΑΤΑΧΩΡΗΣΗ ΔΕΔΟΜΕΝΩΝ", command=partial(kataxorisi_data_drop,surname,name,sclub,
                                                                               sport,ybirth,weight,height,pbjump,email,dokimasia),bg='red').place(x=180, y=220)
                exit
                root1.mainloop()

def  data_kouti0(surname, name, sclub,sport, ybirth, weight, height,pbjump, email,dokimasia):
                root1 = Tk()
                root1.geometry('500x260+550+200')
                root1.title('ΚΑΤΑΧΩΡΗΣΗ ΔΕΔΟΜΕΝΩΝ ΑΘΛΗΤΩΝ')
                root1.iconbitmap('./1.ico')
                surname = StringVar(root1)
                name = StringVar(root1)
                sclub = StringVar(root1)
                sport = StringVar(root1)
                ybirth = StringVar(root1)
                weight = StringVar(root1)
                height = StringVar(root1)
                pbjump = StringVar(root1)
                email = StringVar(root1)
                a11 = Label(root1, text="ΔΟΚΙΜΑΣΙΑ").place(x=10, y=5)
                a111 = Label(root1, text= dokimasia).place(x=150, y=5)

                a1 = Label(root1, text="ΕΠΩΝΥΜΟ").place(x=10, y=30)
                a2 = Label(root1, text="ΟΝΟΜΑ").place(x=10, y=50)
                a3 = Label(root1, text="ΑΘ. ΣΥΛΛΟΓΟΣ").place(x=10, y=70)
                a4 = Label(root1, text="ΑΓΩΝΙΣΜΑ").place(x=10, y=90)
                a5 = Label(root1, text="ΕΤΟΣ ΓΕΝΝΗΣΗΣ").place(x=10, y=110)
                a6 = Label(root1, text="ΜΑΖΑ - ΒΑΡΟΣ").place(x=10, y=130)
                a61 = Label(root1, text=" (Kgr)").place(x=220, y=130)
                a7 = Label(root1, text="ΥΨΟΣ   ").place(x=10, y=150)
                a71 = Label(root1, text=" (cm)").place(x=220, y=150)
                a8 = Label(root1, text="PB ΚΑΘ.ΑΛΜΑ  ").place(x=10, y=170)
                a81 = Label(root1, text="(cm))").place(x=220, y=170)
                a9 = Label(root1, text="EMAIL").place(x=10, y=190)

                a1 = Entry(root1, width=50, textvariable=surname).place(x=150, y=30)
                a2 = Entry(root1, width=50, textvariable=name).place(x=150, y=50)
                a3 = Entry(root1, width=50, textvariable=sclub).place(x=150, y=70)
                a4 = Entry(root1, width=50, textvariable=sport).place(x=150, y=90)
                a5 = Entry(root1, width=10, textvariable=ybirth).place(x=150, y=110)
                a6 = Entry(root1, width=10, textvariable=weight).place(x=150, y=130)
                a7 = Entry(root1, width=10, textvariable=height).place(x=150, y=150)
                a8 = Entry(root1, width=10, textvariable=pbjump).place(x=150, y=170)
                a9 = Entry(root1, width=50, textvariable=email).place(x=150, y=190)
                # 2. CALLS PERSONAL DATA KATAXORISI ROUTINE
                b1 = Button(root1, text="ΚΑΤΑΧΩΡΗΣΗ ΔΕΔΟΜΕΝΩΝ", command=partial(kataxorisi_data0,surname,name,sclub,
                                                                               sport,ybirth,weight,height,pbjump,email,dokimasia),bg='red').place(x=180, y=220)
                exit
                root1.mainloop()

# ΡΟΥΤΙΝΕΣ ΜΕ ΠΟΛΛΑΠΛΑ ΑΛΜΑΤΑ ΚΑΙ ΑΘΛΗΤΗ EKTOS APO TO VJ mat
def kataxorisi_data(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia):
                    surname = (surname.get())
                    name = (name.get())
                    sclub = (sclub.get())
                    sport = (sport.get())
                    ybirth = (ybirth.get())
                    weight = (weight.get())
                    height = (height.get())
                    pbjump = (pbjump.get())
                    email = (email.get())
                    jumps=0
                    r1 = Tk()
                    r1.geometry('400x160+550+500')
                    r1.title("ΜΕΤΡΗΣΗ ΑΛΜΑΤΟΣ - V_JUMP CALCULATION")
                    r1.iconbitmap('./1.ico')
                    Label(r1, text="      ΠΑΡΑΚΑΛΩ ΕΤΟΙΜΑΣΤΕΙΤΕ   ", font="arial 14 bold", fg="red").place(x=30, y=40)
                    Label(r1, text="    ΓΙΑ  ΤΑ ΚΑΤΑΚΟΡΥΦΑ ΑΛΜΑΤΑ   ", font="arial 14 bold", fg="red").place(x=35, y=65)
                    Button(r1, text="ΠΑΤΗΣΤΕ ΓΙΑ ΕΝΑΡΞΗ 1",command=partial(time_data,t_initial, t_impulse, t_flight, ver_jump,surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)).place(x=140, y=120)
                    r1.mainloop()

def getImpulse(trials, jumps):
    try:
        return trials[jumps][0]
    except:
        print("Not so many jumps")
def getFlight(trials , jumps):
    try:
        return trials[jumps][1]
    except:
        print("Not so many jumps")
def getJump(trials , jumps):
    try:
        return trials[jumps][2]
    except:
        print("Not so many jumps")

def time_data(t_initial, t_impulse, t_flight, ver_jump,surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia):

    maxJumps = 5
    jumps = 0
    t_initial = None
    t_impulse = None  # This is the variable for the impulse time
    t_flight = None  # This is the variable for the flight time
    trials = []
    r2= Tk()
    r2.iconbitmap('./1.ico')
    r2.geometry('300x200+1100+200')
    r2.title("# ΑΛΜΑΤΟΣ" )

    while True:

        # Xronos antidrasis
        status = serialReading.microbit_touched()
        print(status)
        if status == True:
            if t_impulse is not None:
                t3 = time.monotonic()
                t_flight = t3 - t1
                #print("FINAL FLIGHT TIME", t_flight)  # You should see a reasonable time here.
                #print(jumps + 1, (t_impulse, t_flight))
                #print("-----------------------------------------------")
                jumps = jumps + 1
                label = Label(r2, font = ("Arial", 23, "bold"), text="# ΑΛΜΑΤΟΣ :\n" + "#  JUMP:\n"+str(jumps), bg="grey", fg="white", width = 200, height = 10)
                label.pack()

                # Add jumps to array and check if we completed the jumps
                tfl = (0.5 * t_flight) * (0.5 * t_flight)
                ver_jump = (4.90 * tfl)*100
                trials.append((t_impulse , t_flight, ver_jump))

                if jumps == maxJumps:
                    paroysiasi_results(t_initial, t_impulse, t_flight, ver_jump, surname, name, sclub, sport,
                                        ybirth, weight, height, pbjump, email, dokimasia,trials)
                # If not just reset the jump and add another trial
                t_impulse = None
                t_flight = None
                t_initial = time.monotonic()
            elif t_initial is None:
                t_initial = time.monotonic()
            # Jump point code

        else:
            if (t_initial is not None):
                if (t_impulse is None):
                    # We take the time before subtructing and use it also as starting point for the flight time.
                    t1 = time.monotonic()
                    t_impulse = t1 - t_initial
                    print("FINAL IMPULSE TIME", jumps+1, t_impulse)
                t2 = time.monotonic()
                print('FLIGHT TIME' , t2 - t1)


def  data_kouti3(surname, name, sclub,sport, ybirth, weight, height,pbjump, email,dokimasia):
                root1 = Tk()
                root1.geometry('500x260+600+200')
                root1.title('ΚΑΤΑΧΩΡΗΣΗ ΔΕΔΟΜΕΝΩΝ ΑΘΛΗΤΩΝ')
                root1.iconbitmap('./1.ico')
                surname = StringVar(root1)
                name = StringVar(root1)
                sclub = StringVar(root1)
                sport = StringVar(root1)
                ybirth = StringVar(root1)
                weight = StringVar(root1)
                height = StringVar(root1)
                pbjump = StringVar(root1)
                email = StringVar(root1)
                a11 = Label(root1, text="ΔΟΚΙΜΑΣΙΑ").place(x=10, y=5)
                a111 = Label(root1, text= dokimasia).place(x=150, y=5)

                a1 = Label(root1, text="ΕΠΩΝΥΜΟ").place(x=10, y=30)
                a2 = Label(root1, text="ΟΝΟΜΑ").place(x=10, y=50)
                a3 = Label(root1, text="ΑΘ. ΣΥΛΛΟΓΟΣ").place(x=10, y=70)
                a4 = Label(root1, text="ΑΓΩΝΙΣΜΑ").place(x=10, y=90)
                a5 = Label(root1, text="ΕΤΟΣ ΓΕΝΝΗΣΗΣ").place(x=10, y=110)
                a6 = Label(root1, text="ΜΑΖΑ - ΒΑΡΟΣ").place(x=10, y=130)
                a61 = Label(root1, text=" (Kgr)").place(x=220, y=130)
                a7 = Label(root1, text="ΥΨΟΣ   ").place(x=10, y=150)
                a71 = Label(root1, text=" (cm)").place(x=220, y=150)
                a8 = Label(root1, text="PB ΚΑΘ.ΑΛΜΑ  ").place(x=10, y=170)
                a81 = Label(root1, text="(cm))").place(x=220, y=170)
                a9 = Label(root1, text="EMAIL").place(x=10, y=190)

                a1 = Entry(root1, width=50, textvariable=surname).place(x=150, y=30)
                a2 = Entry(root1, width=50, textvariable=name).place(x=150, y=50)
                a3 = Entry(root1, width=50, textvariable=sclub).place(x=150, y=70)
                a4 = Entry(root1, width=50, textvariable=sport).place(x=150, y=90)
                a5 = Entry(root1, width=10, textvariable=ybirth).place(x=150, y=110)
                a6 = Entry(root1, width=10, textvariable=weight).place(x=150, y=130)
                a7 = Entry(root1, width=10, textvariable=height).place(x=150, y=150)
                a8 = Entry(root1, width=10, textvariable=pbjump).place(x=150, y=170)
                a9 = Entry(root1, width=50, textvariable=email).place(x=150, y=190)
                # 2. CALLS PERSONAL DATA KATAXORISI ROUTINE
                b1 = Button(root1, text="ΚΑΤΑΧΩΡΗΣΗ ΔΕΔΟΜΕΝΩΝ", command=partial(kataxorisi_data3,surname,name,sclub,
                                                                               sport,ybirth,weight,height,pbjump,email,dokimasia),bg='red').place(x=180, y=220)
                exit
                root1.mainloop()


# ΡΟΥΤΙΝΕΣ ΜΕ ΠΟΛΛΑΠΛΑ ΑΛΜΑΤΑ ΚΑΙ ΑΘΛΗΤΗ ΠΑΝΩ ΣΤΟ VJ mat
def kataxorisi_data3(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia):
                    surname = (surname.get())
                    name = (name.get())
                    sclub = (sclub.get())
                    sport = (sport.get())
                    ybirth = (ybirth.get())
                    weight = (weight.get())
                    height = (height.get())
                    pbjump = (pbjump.get())
                    email = (email.get())
                    r1 = Tk()
                    r1.geometry('400x160+550+500')
                    r1.title("ΜΕΤΡΗΣΗ ΑΛΜΑΤΟΣ - V_JUMP CALCULATION")
                    r1.iconbitmap('./1.ico')
                    Label(r1, text="  ΠΑΡΑΚΑΛΩ ΑΝΕΒΕΙΤΕ ΣΤΟ VJMAT   ", font="arial 14 bold", fg="red").place(x=30, y=40)
                    Label(r1, text="    ΓΙΑ ΤΑ ΚΑΤΑΚΟΡΥΦΑ ΑΛΜΑΤΑ   ", font="arial 14 bold", fg="red").place(x=35, y=65)
                    Button(r1, text="ΠΑΤΗΣΤΕ ΓΙΑ ΕΝΑΡΞΗ",
                            command=partial(time_data3,t_initial, t_impulse, t_flight, ver_jump,surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)).place(x=140, y=120)
                    r1.mainloop()

def getImpulse(trials, jumps):
    try:
        return trials[jumps][0]
    except:
        print("Not so many jumps")

def getFlight(trials , jumps):
    try:
        return trials[jumps][1]
    except:
        print("Not so many jumps")

def getJump(trials , jumps):
    try:
        return trials[jumps][2]
    except:
        print("Not so many jumps")

def time_data3(t_initial, t_impulse, t_flight, ver_jump,surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia):
        t_initial =  time.monotonic()
        t_impulse = None  # This is the variable for the impulse time
        t_flight = None  # This is the variable for the flight time
        trials = []
        maxJumps = 5
        jumps = 0
        #mdata= np.zeros((maxJumps, 3))
        while True:
            # Xronos antidrasis
            if serialReading.microbit_touched():
                if t_impulse is not None:
                    t3 = time.monotonic()
                    t_flight = t3 - t1
                    print("FINAL φλι TIME", t_flight)
                    jumps = jumps + 1
                    # Add jumps to array and check if we completed the jumps
                    tfl = (0.5 * t_flight) * (0.5 * t_flight)
                    ver_jump = (4.90 * tfl)*100
                    trials.append((t_impulse , t_flight, ver_jump))
                    if jumps == maxJumps:

                        paroysiasi_results(t_initial, t_impulse, t_flight, ver_jump, surname, name, sclub, sport,
                                           ybirth, weight, height, pbjump, email, dokimasia,trials)

                    # If not just reset the jump and add another trial
                    t_impulse = None
                    t_flight = None
                    t_initial = time.monotonic()
                    #elif t_initial is None:
                    #t_initial = time.monotonic()

            # Jump point code
            else:
                #if (t_initial is None):
                    if (t_impulse is None):
                        # We take the time before subtructing and use it also as starting point for the flight time.
                        t1 = time.monotonic()
                        t_impulse = t1 - t_initial
                        print("FINAL IMPULSE TIME", t_impulse)

# ΡΟΥΤΙΝΕΣ DATA RETRIEVE ΑΠΛΩΝ ΜΕΜΟΝΟΜΕΝΩΝ ΑΛΜΑΤΩΝ
def kataxorisi_data0(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia):
                    surname = (surname.get())
                    name = (name.get())
                    sclub = (sclub.get())
                    sport = (sport.get())
                    ybirth = (ybirth.get())
                    weight = (weight.get())
                    height = (height.get())
                    pbjump = (pbjump.get())
                    email = (email.get())
                    print ("Dokimasia" , dokimasia)
                    r1 = Tk()
                    r1.geometry('400x160+600+500')
                    r1.title("ΜΕΤΡΗΣΗ ΑΛΜΑΤΟΣ - V_JUMP CALCULATION")
                    r1.iconbitmap('./1.ico')
                    Label(r1, text="ΠΑΡΑΚΑΛΩ ΑΝΕΒΕΙΤΕ ΣΤΟ ΔΑΠΕΔΟ ", font="arial 14 bold", fg="red").place(x=30, y=40)
                    Label(r1, text=" ΚΑΙ ΕΤΟΙΜΑΣΤΕΙΤΕ ΓΙΑ ΤΟ ΑΛΜΑ ", font="arial 14 bold", fg="red").place(x=35, y=65)
                    Label(r1, text= "#ΑΛΜΑΤΟΣ : 1", font="arial 14 bold", fg="blue").place(x=10, y=10)
                    Button(r1, text="ΜΕΤΡΗΣΗ ΑΛΜΑΤΟΣ",
                            command=partial(time_data0,t_initial, t_impulse, t_flight, ver_jump,surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)).place(x=140, y=120)
                    r1.mainloop()


def time_data0(t_initial, t_impulse, t_flight, ver_jump,surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia):

    t_initial = time.monotonic()
    t_impulse = None  # This is the variable for the impulse time
    t_flight = None  # This is the variable for the flight time
    while True:
            # Xronos antidrasis
            status = serialReading.microbit_touched()
            if status == True:
            #if microbit.pin0.pressed():
                if t_impulse is not None:
                    #serialReading.stop_reading()
                    #  t1=time.monotonic()
                    #  print ("IMPULSE TIME", t1 - t_initial) #You should see the time rising in here

                    # Landing point code
                    t3 = time.monotonic()
                    t_flight = t3 - t1
                    print("FINAL FLIGHT TIME", t_flight)  # You should see a reasonable time here.
                    print("################################################")
                    print ("t_ flight -->", t_flight)
                    print ("t_impulse -->", t_impulse)
                    tfl=(0.5*t_flight)*(0.5*t_flight)
                    ver_jump= (4.90 * tfl)*100
                    paroysiasi_results0(t_initial, t_impulse, t_flight, ver_jump,surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)
                    break

            # Jump point code
            else:
                if (t_impulse is None):
                    # We take the time before subtructing and use it also as starting point for the flight time.
                    t1 = time.monotonic()
                    t_impulse = t1 - t_initial
                    print("FINAL IMPULSE TIME", t_impulse)
                t2 = time.monotonic()
                print("    FLIGHT TIME", t2 - t1)  # You should see the time rising in here

def paroysiasi_results0(t_initial, t_impulse, t_flight, ver_jump, surname, name, sclub, sport, ybirth,
                                       weight, height, pbjump, email,dokimasia):

    top = Tk()
    top.geometry('600x650+100+30')
    top.title('ΠΑΡΟΥΣΙΑΣΗ ΑΠΟΤΕΛΕΣΜΑΤΩΝ')
    top.iconbitmap('./1.ico')
    Label(top, text="ΕΠΩΝΥΜΟ").place(x=10, y=25)
    Label(top, text=surname).place(x=120, y=25)
    Label(top, text="ΟΝΟΜΑ").place(x=10, y=45)
    Label(top, text=name).place(x=120, y=45)
    Label(top, text="ΑΘ. ΣΥΛΛΟΓΟΣ").place(x=10, y=65)
    Label(top, text=sclub).place(x=120, y=65)
    Label(top, text="ΑΓΩΝΙΣΜΑ").place(x=10, y=85)
    Label(top, text=sport).place(x=120, y=85)
    Label(top, text="ΕΤΟΣ ΓΕΝΝΗΣΗΣ").place(x=10, y=105)
    Label(top, text=ybirth).place(x=120, y=105)
    Label(top, text="ΜΑΖΑ - ΒΑΡΟΣ").place(x=10, y=125)
    Label(top, text=weight).place(x=120, y=125)
    Label(top, text="(Kgr)").place(x=220, y=125)
    Label(top, text="ΥΨΟΣ   ").place(x=10, y=145)
    Label(top, text=height).place(x=120, y=145)
    Label(top, text="(cm)").place(x=220, y=145)
    Label(top, text="PB ΚΑΘ.ΑΛΜΑ  ").place(x=10, y=165)
    Label(top, text=pbjump).place(x=120, y=165)
    Label(top, text="(cm)").place(x=220, y=165)
    Label(top, text="EMAIL").place(x=10, y=185)
    Label(top, text=email).place(x=120, y=185)
    dat = date.today()
    Label(top, text="ΗΜΕΡΟΜΗΝΙΑ:     ").place(x=10, y=210)
    Label(top, text=dat).place(x=100, y=210)
    ticks = time.asctime(time.localtime(time.time()))
    Label(top, text="ΩΡΑ ΑΞΙΟΛΟΓΗΣΗΣ:").place(x=180, y=210)
    Label(top, text=ticks).place(x=300, y=210)
    Label(top, text="ΕΙΔΟΣ ΚΑΤΑΚΟΡΥΦΟΥ ΑΛΜΑΤΟΣ: ").place(x=10, y=230)
    Label(top, text=dokimasia).place(x=220, y=230)

    ver_jump = '{:.2f}'.format(ver_jump)
    Label(top, text="ΚΑΤ. ΑΛΜΑ :  ", font="arial 15 bold", fg="black").place(x=70, y=300)
    Label(top, text=ver_jump, font="arial 40 bold", fg="red").place(x=320, y=270)
    Label(top, text="  cm", font="arial 15 bold", fg="red").place(x=460, y=300)

    t_impulse = '{:.3f}'.format(t_impulse)
    Label(top, text="ΧΡΟΝΟΣ ΩΘΗΣΗΣ:", font="arial 15 bold", fg="black").place(x=70, y=350)
    Label(top, text=t_impulse, font="arial 40 bold", fg="blue").place(x=320, y=330)
    Label(top, text="  sec", font="arial 15 bold", fg="blue").place(x=460, y=350)

    t_flight = '{:.3f}'.format(t_flight)
    Label(top, text="ΧΡΟΝΟΣ ΠΤΗΣΗΣ:", font="arial 15 bold", fg="black").place(x=70, y=430)
    Label(top, text=t_flight, font="arial 40 bold", fg="blue").place(x=320, y=400)
    Label(top, text="  sec", font="arial 15 bold", fg="blue").place(x=460, y=420)

    posostopb =  (int(pbjump)/int(float(ver_jump)))
    posostopb = '{:.2f}'.format(posostopb)
    Label(top, text="PB/ΑΛΜΑ: ", font="arial 15 bold", fg="black").place(x=70, y=490)
    Label(top, text= posostopb, font="arial 40 bold", fg="blue").place(x=320, y=470)
    Label(top, text=" %", font="arial 15 bold", fg="blue").place(x=460, y=480)
    Label(top, text="Powered by AISA - 3T / TSIRAKOS K. DIMITRIOS copyright 2020",
                        font="arial 5 bold", fg="black").place(x=10, y=750)
      # 3. CALLS PDF WRITING ROUTINE
    Button(top, text="ΕΞΟΔΟΣ-EXIT", command= top.destroy).place(x=300, y=580)
    Button(top, text="ΕΓΓΡΑΦΗ ΣΕ  PDF", command=pdf_dev0(t_impulse, t_flight, ver_jump, surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)).place(x=150, y=580)

    im2 = Image.open('logo1.png')
    img2 = ImageTk.PhotoImage(im2, master=top)
    label = Label(top, image=img2).place(x=400, y=10)
    im3 = Image.open('2.png')
    img3= ImageTk.PhotoImage(im3, master=top)
    label = Label(top, image=img3).place(x=400, y=100)
    top.mainloop()

def pdf_dev0(t_impulse, t_flight, ver_jump, surname, name, sclub, sport, ybirth, weight, height, pbjump, email, dokimasia):
            print (surname,name)
            a = date.today()
            ticks = time.asctime(time.localtime(time.time()))
            tik = ticks[11:13]
            tik2 = ticks[14:16]
            tik3 = ticks[17:19]
            c = canvas.Canvas(str(surname) + "_" + str(a) + "_"+ str(tik)+str(tik2)+str(tik3)+".pdf")
            c.setFont("Times-Bold", 20)
            c.drawString(30, 830, "____________________________________________________________________________ ")
            c.drawString(30, 800, "ΑΝΑΦΟΡΑ ΑΞΙΟΛΟΓΗΣΗΣ ΚΑΤΑΚΟΡΥΦΟΥ ΑΛΜΑΤΟΣ ")
            c.drawString(30, 790, "____________________________________________________________________________ ")
            c.setFont("Times-Roman", 14)
            c.drawString(30, 750, "ΕΠΩΝΥΜΟ")
            c.drawString(30, 730, "ΟΝΟΜΑ")
            c.drawString(30, 710, "ΑΘΛ. ΣΥΛΛΟΓΟΣ")
            c.drawString(30, 690, "ΑΓΩΝΙΣΜΑ")
            c.drawString(30, 670, "ΕΤΟΣ ΓΕΝΝΗΣΗΣ")
            c.drawString(30, 650, "ΒΑΡΟΣ (Kgr)")
            c.drawString(30, 630, "ΥΨΟΣ ")
            c.drawString(30, 610, "PB ΚΑΤ. ΑΛΜΑ")
            c.drawString(30, 590, "EMAIL")
            c.drawString(30, 570, "ΗΜΕΡ. ΑΞΙΟΛΟΓΗΣΗΣ")
            c.drawString(30, 550, "ΩΡΑ ΑΞΙΟΛΟΓΗΣΗΣ")
            c.setFont("Times-Bold", 14)
            c.drawString(220, 750, str(surname))
            c.drawString(220, 730, str(name))
            c.drawString(220, 710, str(sclub))
            c.drawString(220, 690, str(sport))
            c.drawString(220, 670, str(ybirth))
            c.drawString(220, 650, str(weight))
            c.drawString(220, 630, str(height))
            c.drawString(220, 610, str(pbjump))
            c.drawString(220, 590, str(email))
            c.drawString(220, 570, str(a))
            c.drawString(220, 550, str(ticks))
            c.setFont("Times-Bold", 15)
            c.drawString(30, 520, "____________________________________________________________ ")
            c.setFont("Times-Roman", 16)
            c.drawString(30, 500, ("ΔΟΚΙΜΑΣΙΑ: " + dokimasia))
            c.setFont("Times-Roman", 15)
            c.drawString(30, 440, "ΚΑΤΑΚΟΡΥΦΟ ΑΛΜΑ")
            c.drawString(30, 390, "ΧΡΟΝΟΣ ΩΘΗΣΗΣ")
            c.drawString(30, 340, "ΧΡΟΝΟΣ ΠΤΗΣΗΣ")
            c.drawString(30, 290, "PB/ALMA")
            c.setFont("Times-Bold", 40)
            c.drawString(220, 440, ver_jump + " cm")
            c.drawString(220, 390, t_impulse + " sec")
            c.drawString(220, 340, t_flight + " sec")
            posostopb = (int(pbjump) / int(float(ver_jump)))

            posostopb = '{:.2f}'.format(posostopb)
            c.drawString(220, 290, str(posostopb) + "  %")
            c.setFont("Times-Bold", 15)
            c.drawString(30, 270, "_____________________________________________________________")
            c.setFont("Times-Bold", 6)
            c.drawImage("logo1.png", 420,700, mask='auto')
            c.drawImage("2.png", 420,600, mask='auto')
            c.drawString(30, 30, "Powered by AISA - 3T - TSIRAKOS K. DIMITRIOS copyright 2020")
            c.save()
            return

####
# ΡΟΥΤΙΝΕΣ DATA RETRIEVE ΑΠΛΩΝ ΜΕΜΟΝΟΜΕΝΩΝ ΑΛΜΑΤΩΝ
def kataxorisi_data_drop(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia):
                    surname = (surname.get())
                    name = (name.get())
                    sclub = (sclub.get())
                    sport = (sport.get())
                    ybirth = (ybirth.get())
                    weight = (weight.get())
                    height = (height.get())
                    pbjump = (pbjump.get())
                    email = (email.get())
                    print ("llllllllll " , dokimasia)
                    r1 = Tk()
                    r1.geometry('400x160+600+500')
                    r1.title("ΜΕΤΡΗΣΗ ΑΛΜΑΤΟΣ - V_JUMP CALCULATION")
                    r1.iconbitmap('./1.ico')
                    Label(r1, text="ΠΑΡΑΚΑΛΩ ΑΝΕΒΕΙΤΕ ΣΤΟ BOCK ", font="arial 14 bold", fg="red").place(x=30, y=40)
                    Label(r1, text=" ΚΑΙ ΕΤΟΙΜΑΣΤΕΙΤΕ ΓΙΑ ΤΟ ΑΛΜΑ ", font="arial 14 bold", fg="red").place(x=35, y=65)
                    Button(r1, text="ΜΕΤΡΗΣΗ ΑΛΜΑΤΟΣ",
                            command=partial(time_data_drop,t_initial, t_impulse, t_flight, ver_jump,surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)).place(x=140, y=120)
                    r1.mainloop()

def time_data_drop(t_initial, t_impulse, t_flight, ver_jump,surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia):
    t_initial = None
    t_impulse = None  # This is the variable for the impulse time
    t_flight = None  # This is the variable for the flight time
    trials = []
    maxJumps = 1
    jumps = 0

    while True:
        status = serialReading.microbit_touched()
        if status == True:
        # Xronos antidrasis
        #--------------Change here-----------------
        #if serialReading.microbit_touched():
            if t_impulse is not None:
                t3 = time.monotonic()
                t_flight = t3 - t1
                print("FINAL FLIGHT TIME", t_flight)  # You should see a reasonable time here.
                print(jumps + 1, (t_impulse, t_flight))
                print("################################################")
                tfl=(0.5*t_flight)*(0.5*t_flight)
                ver_jump= (4.90 * tfl)*100
                jumps = jumps + 1
                if jumps == maxJumps: paroysiasi_results_drop(t_initial, t_impulse, t_flight, ver_jump,surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)


                #If not just reset the jump and add another trial
                t_impulse = None
                t_flight = None
                t_initial =  time.monotonic()
            elif t_initial is None:
                t_initial = time.monotonic()

        # Jump point code
        else:
            if(t_initial is not None):
                if (t_impulse is None):
                    # We take the time before subtructing and use it also as starting point for the flight time.
                    t1 = time.monotonic()
                    t_impulse = t1 - t_initial

def paroysiasi_results_drop(t_initial, t_impulse, t_flight, ver_jump, surname, name, sclub, sport, ybirth,
                                       weight, height, pbjump, email,dokimasia):

    top = Tk()
    top.geometry('600x650+100+30')
    top.title('ΠΑΡΟΥΣΙΑΣΗ ΑΠΟΤΕΛΕΣΜΑΤΩΝ')
    top.iconbitmap('./1.ico')
    Label(top, text="ΕΠΩΝΥΜΟ").place(x=10, y=25)
    Label(top, text=surname).place(x=120, y=25)
    Label(top, text="ΟΝΟΜΑ").place(x=10, y=45)
    Label(top, text=name).place(x=120, y=45)
    Label(top, text="ΑΘ. ΣΥΛΛΟΓΟΣ").place(x=10, y=65)
    Label(top, text=sclub).place(x=120, y=65)
    Label(top, text="ΑΓΩΝΙΣΜΑ").place(x=10, y=85)
    Label(top, text=sport).place(x=120, y=85)
    Label(top, text="ΕΤΟΣ ΓΕΝΝΗΣΗΣ").place(x=10, y=105)
    Label(top, text=ybirth).place(x=120, y=105)
    Label(top, text="ΜΑΖΑ - ΒΑΡΟΣ").place(x=10, y=125)
    Label(top, text=weight).place(x=120, y=125)
    Label(top, text="(Kgr)").place(x=220, y=125)
    Label(top, text="ΥΨΟΣ   ").place(x=10, y=145)
    Label(top, text=height).place(x=120, y=145)
    Label(top, text="(cm)").place(x=220, y=145)
    Label(top, text="PB ΚΑΘ.ΑΛΜΑ  ").place(x=10, y=165)
    Label(top, text=pbjump).place(x=120, y=165)
    Label(top, text="(cm)").place(x=220, y=165)
    Label(top, text="EMAIL").place(x=10, y=185)
    Label(top, text=email).place(x=120, y=185)
    dat = date.today()
    Label(top, text="ΗΜΕΡΟΜΗΝΙΑ:     ").place(x=10, y=210)
    Label(top, text=dat).place(x=100, y=210)
    ticks = time.asctime(time.localtime(time.time()))
    Label(top, text="ΩΡΑ ΑΞΙΟΛΟΓΗΣΗΣ:").place(x=180, y=210)
    Label(top, text=ticks).place(x=300, y=210)
    Label(top, text="ΕΙΔΟΣ ΚΑΤΑΚΟΡΥΦΟΥ ΑΛΜΑΤΟΣ: ").place(x=10, y=230)
    Label(top, text=dokimasia).place(x=220, y=230)

    ver_jump = '{:.2f}'.format(ver_jump)
    Label(top, text="ΚΑΤ. ΑΛΜΑ :  ", font="arial 15 bold", fg="black").place(x=70, y=300)
    Label(top, text=ver_jump, font="arial 40 bold", fg="red").place(x=320, y=270)
    Label(top, text="  cm", font="arial 15 bold", fg="red").place(x=460, y=300)

    t_impulse = '{:.3f}'.format(t_impulse)
    Label(top, text="ΧΡΟΝΟΣ ΩΘΗΣΗΣ:", font="arial 15 bold", fg="black").place(x=70, y=350)
    Label(top, text=t_impulse, font="arial 40 bold", fg="blue").place(x=320, y=330)
    Label(top, text="  sec", font="arial 15 bold", fg="blue").place(x=460, y=350)

    t_flight = '{:.3f}'.format(t_flight)
    Label(top, text="ΧΡΟΝΟΣ ΠΤΗΣΗΣ:", font="arial 15 bold", fg="black").place(x=70, y=430)
    Label(top, text=t_flight, font="arial 40 bold", fg="blue").place(x=320, y=400)
    Label(top, text="  sec", font="arial 15 bold", fg="blue").place(x=460, y=420)

    posostopb =  (int(pbjump)/int(float(ver_jump)))
    posostopb = '{:.2f}'.format(posostopb)
    Label(top, text="PB/ΑΛΜΑ: ", font="arial 15 bold", fg="black").place(x=70, y=490)
    Label(top, text= posostopb, font="arial 40 bold", fg="blue").place(x=320, y=470)
    Label(top, text=" %", font="arial 15 bold", fg="blue").place(x=460, y=480)
    Label(top, text="Powered by AISA - 3T / TSIRAKOS K. DIMITRIOS copyright 2020",
                        font="arial 5 bold", fg="black").place(x=10, y=750)
      # 3. CALLS PDF WRITING ROUTINE
    Button(top, text="ΕΞΟΔΟΣ-EXIT", command= top.destroy).place(x=300, y=580)
    Button(top, text="ΕΓΓΡΑΦΗ ΣΕ  PDF", command=pdf_dev_drop(t_impulse, t_flight, ver_jump, surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)).place(x=150, y=580)

    im2 = Image.open('logo1.png')
    img2 = ImageTk.PhotoImage(im2, master=top)
    label = Label(top, image=img2).place(x=400, y=10)
    im3 = Image.open('2.png')
    img3= ImageTk.PhotoImage(im3, master=top)
    label = Label(top, image=img3).place(x=300, y=100)
    top.mainloop()

def pdf_dev_drop(t_impulse, t_flight, ver_jump, surname, name, sclub, sport, ybirth, weight, height, pbjump, email, dokimasia):
            a = date.today()
            ticks = time.asctime(time.localtime(time.time()))
            tik = ticks[11:13]
            tik2 = ticks[14:16]
            tik3 = ticks[17:19]
            c = canvas.Canvas(str(surname) + "_" + str(a) + "_"+ str(tik)+str(tik2)+str(tik3)+".pdf")
            c.setFont("Times-Bold", 20)
            c.drawString(30, 830, "____________________________________________________________________________ ")
            c.drawString(30, 800, "ΑΝΑΦΟΡΑ ΑΞΙΟΛΟΓΗΣΗΣ ΚΑΤΑΚΟΡΥΦΟΥ ΑΛΜΑΤΟΣ ")
            c.drawString(30, 790, "____________________________________________________________________________ ")
            c.setFont("Times-Roman", 14)
            c.drawString(30, 750, "ΕΠΩΝΥΜΟ")
            c.drawString(30, 730, "ΟΝΟΜΑ")
            c.drawString(30, 710, "ΑΘΛ. ΣΥΛΛΟΓΟΣ")
            c.drawString(30, 690, "ΑΓΩΝΙΣΜΑ")
            c.drawString(30, 670, "ΕΤΟΣ ΓΕΝΝΗΣΗΣ")
            c.drawString(30, 650, "ΒΑΡΟΣ (Kgr)")
            c.drawString(30, 630, "ΥΨΟΣ ")
            c.drawString(30, 610, "PB ΚΑΤ. ΑΛΜΑ")
            c.drawString(30, 590, "EMAIL")
            c.drawString(30, 570, "ΗΜΕΡ. ΑΞΙΟΛΟΓΗΣΗΣ")
            c.drawString(30, 550, "ΩΡΑ ΑΞΙΟΛΟΓΗΣΗΣ")
            c.setFont("Times-Bold", 14)
            c.drawString(220, 750, str(surname))
            c.drawString(220, 730, str(name))
            c.drawString(220, 710, str(sclub))
            c.drawString(220, 690, str(sport))
            c.drawString(220, 670, str(ybirth))
            c.drawString(220, 650, str(weight))
            c.drawString(220, 630, str(height))
            c.drawString(220, 610, str(pbjump))
            c.drawString(220, 590, str(email))
            c.drawString(220, 570, str(a))
            c.drawString(220, 550, str(ticks))
            c.setFont("Times-Bold", 15)
            c.drawString(30, 520, "____________________________________________________________ ")
            c.setFont("Times-Roman", 16)
            c.drawString(30, 500, ("ΔΟΚΙΜΑΣΙΑ: " + dokimasia))
            c.setFont("Times-Roman", 15)
            c.drawString(30, 440, "ΚΑΤΑΚΟΡΥΦΟ ΑΛΜΑ")
            c.drawString(30, 390, "ΧΡΟΝΟΣ ΩΘΗΣΗΣ")
            c.drawString(30, 340, "ΧΡΟΝΟΣ ΠΤΗΣΗΣ")
            c.drawString(30, 290, "PB/ALMA")
            c.setFont("Times-Bold", 40)
            c.drawString(220, 440, ver_jump + " cm")
            c.drawString(220, 390, t_impulse + " sec")
            c.drawString(220, 340, t_flight + " sec")
            posostopb = (int(pbjump) / int(float(ver_jump)))

            posostopb = '{:.2f}'.format(posostopb)
            c.drawString(220, 290, str(posostopb) + "  %")
            c.setFont("Times-Bold", 15)
            c.drawString(30, 270, "_____________________________________________________________")
            c.setFont("Times-Bold", 6)
            c.drawImage("logo1.png", 420,700, mask='auto')
            c.drawImage("2.png", 420,600, mask='auto')
            c.drawString(30, 30, "Powered by AISA - 3T - TSIRAKOS K. DIMITRIOS copyright 2020")
            c.save()
            return


#1. ΡΟΥΤΙΝΑ  ΠΑΡΟΥΣΙΑΣΗΣ ΠΟΛΛΑΠΛΩΝ ΑΛΜΑΤΩΝ
def paroysiasi_results(t_initial, t_impulse, t_flight, ver_jump, surname, name, sclub, sport, ybirth,
                                       weight, height, pbjump, email,dokimasia,trials):
    import matplotlib, numpy, sys
    matplotlib.use('TkAgg')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure

    top = Tk()
    top.geometry('1100x580+100+100')
    top.title('ΠΑΡΟΥΣΙΑΣΗ ΑΠΟΤΕΛΕΣΜΑΤΩΝ')
    top.iconbitmap('./1.ico')
    Label(top, text="ΕΠΩΝΥΜΟ").place(x=10, y=25)
    Label(top, text=surname).place(x=120, y=25)
    Label(top, text="ΟΝΟΜΑ").place(x=10, y=45)
    Label(top, text=name).place(x=120, y=45)
    Label(top, text="ΑΘ. ΣΥΛΛΟΓΟΣ").place(x=10, y=65)
    Label(top, text=sclub).place(x=120, y=65)
    Label(top, text="ΑΓΩΝΙΣΜΑ").place(x=10, y=85)
    Label(top, text=sport).place(x=120, y=85)
    Label(top, text="ΕΤΟΣ ΓΕΝΝΗΣΗΣ").place(x=10, y=105)
    Label(top, text=ybirth).place(x=120, y=105)
    Label(top, text="ΜΑΖΑ - ΒΑΡΟΣ").place(x=10, y=125)
    Label(top, text=weight).place(x=120, y=125)
    Label(top, text="(Kgr)").place(x=220, y=125)
    Label(top, text="ΥΨΟΣ   ").place(x=10, y=145)
    Label(top, text=height).place(x=120, y=145)
    Label(top, text="(cm)").place(x=220, y=145)
    Label(top, text="PB ΚΑΘ.ΑΛΜΑ  ").place(x=10, y=165)
    Label(top, text=pbjump).place(x=120, y=165)
    Label(top, text="(cm)").place(x=220, y=165)
    Label(top, text="EMAIL").place(x=10, y=185)
    Label(top, text=email).place(x=120, y=185)
    dat = date.today()
    Label(top, text="ΗΜΕΡΟΜΗΝΙΑ:     ").place(x=10, y=210)
    Label(top, text=dat).place(x=100, y=210)
    ticks = time.asctime(time.localtime(time.time()))
    Label(top, text="ΩΡΑ ΑΞΙΟΛΟΓΗΣΗΣ:").place(x=180, y=210)
    Label(top, text=ticks).place(x=300, y=210)
    Label(top, text="ΕΙΔΟΣ ΚΑΤΑΚΟΡΥΦΟΥ ΑΛΜΑΤΟΣ: ").place(x=10, y=250)
    Label(top, text=dokimasia).place(x=220, y=250)

    im2 = Image.open('logo1.png')
    img2 = ImageTk.PhotoImage(im2, master=top)
    label = Label(top, image=img2).place(x=850, y=10)
    im3 = Image.open('2.png')
    img3= ImageTk.PhotoImage(im3, master=top)
    label = Label(top, image=img3).place(x=650, y=10)
    Label(top, text="ΑΠΟΤΕΛΕΣΜΑΤΑ ΠΟΛΛΑΠΛΩΝ ΑΛΜΑΤΩΝ ", font="arial 12 bold",fg="red").place(x=60, y=290)
    Label(top, text="   ΑΛΜΑΤΑ   ", font="arial 10 bold", fg="blue").place(x=20, y=320)
    Label(top, text="   ΕΠΙΔΟΣΗ  ", font="arial 10 bold", fg="blue").place(x=120, y=320)
    Label(top, text=" ΧΡ. ΩΘΗΣΗΣ ", font="arial 10 bold", fg="blue").place(x=220, y=320)
    Label(top, text=" ΧΡ. ΠΤΗΣΗΣ ", font="arial 10 bold", fg="blue").place(x=320, y=320)

    Label(top, text="[1]", font="arial 10 bold", fg="blue").place(x=40, y=350)
    Label(top, text="[2]", font="arial 10 bold", fg="blue").place(x=40, y=380)
    Label(top, text="[3]", font="arial 10 bold", fg="blue").place(x=40, y=410)
    Label(top, text="[4]", font="arial 10 bold", fg="blue").place(x=40, y=440)
    Label(top, text="[5]", font="arial 10 bold", fg="blue").place(x=40, y=470)

    epidosi1 ='{:.2f}'.format(getJump(trials,0))
    Label(top, text=epidosi1 + ' cm',font="arial 12 bold").place(x=130, y=350)
    epidosi2 = '{:.2f}'.format(getJump(trials, 1))
    Label(top, text=epidosi2 + ' cm', font="arial 12 bold").place(x=130, y=380)
    epidosi3 = '{:.2f}'.format(getJump(trials, 2))
    Label(top, text=epidosi3 + ' cm', font="arial 12 bold").place(x=130, y=410)
    epidosi4 = '{:.2f}'.format(getJump(trials, 3))
    Label(top, text=epidosi4 + ' cm', font="arial 12 bold").place(x=130, y=440)
    epidosi5 = '{:.2f}'.format(getJump(trials, 4))
    Label(top, text=epidosi5+ ' cm', font="arial 12 bold").place(x=130, y=470)

    imp1 = '{:.2f}'.format(getImpulse(trials, 0))
    Label(top, text=imp1 + 'sec', font="arial 12 bold").place(x=230, y=350)
    imp2 = '{:.2f}'.format(getImpulse(trials, 1))
    Label(top, text=imp2 + 'sec', font="arial 12 bold").place(x=230, y=380)
    imp3 = '{:.2f}'.format(getImpulse(trials, 2))
    Label(top, text=imp3 + 'sec', font="arial 12 bold").place(x=230, y=410)
    imp4 = '{:.2f}'.format(getImpulse(trials, 3))
    Label(top, text=imp4 + 'sec', font="arial 12 bold").place(x=230, y=440)
    imp5 = '{:.2f}'.format(getImpulse(trials, 4))
    Label(top, text=imp5 + 'sec', font="arial 12 bold").place(x=230, y=470)

    fl1 = '{:.2f}'.format(getFlight(trials, 0))
    Label(top, text=fl1 + 'sec', font="arial 12 bold").place(x=330, y=350)
    fl2 = '{:.2f}'.format(getFlight(trials, 1))
    Label(top, text=fl2 + 'sec', font="arial 12 bold").place(x=330, y=380)
    fl3 = '{:.2f}'.format(getFlight(trials, 2))
    Label(top, text=fl3 + 'sec', font="arial 12 bold").place(x=330, y=410)
    fl4 = '{:.2f}'.format(getFlight(trials, 3))
    Label(top, text=fl4 + 'sec', font="arial 12 bold").place(x=330, y=440)
    fl5 = '{:.2f}'.format(getFlight(trials, 4))
    Label(top, text=fl5 + 'sec', font="arial 12 bold").place(x=330, y=470)

    epidosi_mean =  (getJump(trials,0)+getJump(trials,1)+getJump(trials,2)+getJump(trials,3)+getJump(trials,4))
    epidosi_mean=epidosi_mean/5
    imptime_mean =  (getImpulse(trials,0)+getImpulse(trials,1)+getImpulse(trials,2)+getImpulse(trials,3)+getImpulse(trials,4))
    imptime_mean=imptime_mean/5
    fltime_mean =  (getFlight(trials,0)+getFlight(trials,1)+getFlight(trials,2)+getFlight(trials,3)+getFlight(trials,4))
    fltime_mean =  fltime_mean /5


    data1 = {'ΑΡΙΘΜΟΣ ΑΛΜΑΤΟΣ': ['1','2','3','4','5','M.T'],
         'Κατ. άλματα': [float(epidosi1),float(epidosi2),float(epidosi3),float(epidosi4),float(epidosi5),float(epidosi_mean)]}
    df1 = DataFrame(data1,columns=['ΑΡΙΘΜΟΣ ΑΛΜΑΤΟΣ','Κατ. άλματα'])

    figure1 = plt.Figure(figsize=(5,3), dpi=100)
    ax1 = figure1.add_subplot(111)

    bar1 = FigureCanvasTkAgg(figure1, top)

    bar1.get_tk_widget().pack(side=tk.RIGHT)
    df1 = df1[['ΑΡΙΘΜΟΣ ΑΛΜΑΤΟΣ','Κατ. άλματα']].groupby('ΑΡΙΘΜΟΣ ΑΛΜΑΤΟΣ').sum()
    df1.plot(kind='barh', legend=True, ax=ax1, color="red")
    ax1.set_title('ΕΠΙΔΟΣΕΙΣ ΚΑΤΑΚΟΡΥΦΩΝ ΑΛΜΑΤΩΝ')
    Button(top, text="ΕΞΟΔΟΣ-EXIT", command= top.destroy).place(x=350, y=530)
    # 3. CALLS PDF WRITING ROUTINE
    Button(top, text="ΕΓΓΡΑΦΗ ΣΕ  PDF", command=pdf_dev(t_impulse, t_flight, ver_jump, surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia,trials)).place(x=150, y=530)
    top.mainloop()


def pdf_dev(t_impulse, t_flight, ver_jump, surname, name, sclub, sport, ybirth, weight, height, pbjump, email, dokimasia,trials):
            import matplotlib.pyplot as plt
            from io import BytesIO
            from reportlab.pdfgen import canvas
            from reportlab.graphics import renderPDF
            from svglib.svglib import svg2rlg

            a = date.today()
            ticks = time.asctime(time.localtime(time.time()))
            tik = ticks[11:13]
            tik2 = ticks[14:16]
            tik3 = ticks[17:19]

            c = canvas.Canvas(str(surname) + "_" + str(a) + "_"+ str(tik)+str(tik2)+str(tik3)+".pdf")
            #c.setPageSize((1000,900))
            c.drawImage("logo1.png", 400,700, mask='auto')
            c.drawImage("2.png", 400,600, mask='auto')
            c.setFont("Times-Bold", 5)
            c.setFont("Times-Bold", 20)
            c.drawString(30, 830, "____________________________________________________________________________ ")
            c.drawString(30, 800, "ΑΝΑΦΟΡΑ ΑΞΙΟΛΟΓΗΣΗΣ ΚΑΤΑΚΟΡΥΦΟΥ ΑΛΜΑΤΟΣ ")
            c.drawString(30, 790, "____________________________________________________________________________ ")
            c.setFont("Times-Roman", 14)
            c.drawString(30, 750, "ΕΠΩΝΥΜΟ")
            c.drawString(30, 730, "ΟΝΟΜΑ")
            c.drawString(30, 710, "ΑΘΛ. ΣΥΛΛΟΓΟΣ")
            c.drawString(30, 690, "ΑΓΩΝΙΣΜΑ")
            c.drawString(30, 670, "ΕΤΟΣ ΓΕΝΝΗΣΗΣ")
            c.drawString(30, 650, "ΒΑΡΟΣ (Kgr)")
            c.drawString(30, 630, "ΥΨΟΣ ")
            c.drawString(30, 610, "PB ΚΑΤ. ΑΛΜΑ")
            c.drawString(30, 590, "EMAIL")
            c.drawString(30, 570, "ΗΜΕΡ. ΑΞΙΟΛΟΓΗΣΗΣ")
            c.drawString(30, 550, "ΩΡΑ ΑΞΙΟΛΟΓΗΣΗΣ")
            c.setFont("Times-Bold", 14)
            c.drawString(220, 750, str(surname))
            c.drawString(220, 730, str(name))
            c.drawString(220, 710, str(sclub))
            c.drawString(220, 690, str(sport))
            c.drawString(220, 670, str(ybirth))
            c.drawString(220, 650, str(weight))
            c.drawString(220, 630, str(height))
            c.drawString(220, 610, str(pbjump))
            c.drawString(220, 590, str(email))
            c.drawString(220, 570, str(a))
            c.drawString(220, 550, str(ticks))
            c.setFont("Times-Bold", 15)
            c.drawString(30, 540, "____________________________________________________________________________ ")
            c.setFont("Times-Roman", 14)
            c.drawString(30, 520, ("ΔΟΚΙΜΑΣΙΑ: " + dokimasia))
            c.setFont("Times-Roman", 15)
            c.drawString(55, 490,   "  ΑΠΟΤΕΛΕΣΜΑΤΑ ΠΟΛΛΑΠΛΩΝ ΑΛΜΑΤΩΝ")
            c.setFont("Times-Bold", 12)
            c.drawString(40, 470,   "   ΑΛΜΑΤΑ   ")
            c.drawString(120, 470,  "   ΕΠΙΔΟΣΗ  ")
            c.drawString(210, 470,   " ΧΡ. ΩΘΗΣΗΣ ")
            c.drawString(310, 470,   " ΧΡ. ΠΤΗΣΗΣ ")

            epidosi1 ='{:.2f}'.format(getJump(trials,0))
            epidosi2 = '{:.2f}'.format(getJump(trials, 1))
            epidosi3 = '{:.2f}'.format(getJump(trials, 2))
            epidosi4 = '{:.2f}'.format(getJump(trials, 3))
            epidosi5 = '{:.2f}'.format(getJump(trials, 4))

            epidosi_mean =  (getJump(trials,0)+getJump(trials,1)+getJump(trials,2)+getJump(trials,3)+getJump(trials,4))
            epidosi_mean='{:.2f}'.format(epidosi_mean/5)
            imptime_mean =  (getImpulse(trials,0)+getImpulse(trials,1)+getImpulse(trials,2)+getImpulse(trials,3)+getImpulse(trials,4))
            imptime_mean='{:.2f}'.format(imptime_mean/5)
            fltime_mean =  (getFlight(trials,0)+getFlight(trials,1)+getFlight(trials,2)+getFlight(trials,3)+getFlight(trials,4))
            fltime_mean ='{:.2f}'.format(fltime_mean /5)
            c.setFont("Times-Bold", 12)
            c.drawString(400, 440,   "μ.τ ΑΛΜΑΤΩΝ      :"+ str(epidosi_mean)+ "cm " )
            c.drawString(400, 420,   "μ.τ ΧΡΟΝΟΥ ΩΘΗΣΗΣ:"+ str(imptime_mean)+ "sec" )
            c.drawString(400, 400,   "μ.τ ΧΡΟΝΟΥ ΠΤΗΣΗΣ:"+ str(fltime_mean)+ "sec" )
            c.setFont("Times-Bold", 12)
            imp1 = '{:.2f}'.format(getImpulse(trials, 0))
            imp2 = '{:.2f}'.format(getImpulse(trials, 1))
            imp3 = '{:.2f}'.format(getImpulse(trials, 2))
            imp4 = '{:.2f}'.format(getImpulse(trials, 3))
            imp5 = '{:.2f}'.format(getImpulse(trials, 4))

            fl1 = '{:.2f}'.format(getFlight(trials, 0))
            fl2 = '{:.2f}'.format(getFlight(trials, 1))
            fl3 = '{:.2f}'.format(getFlight(trials, 2))
            fl4 = '{:.2f}'.format(getFlight(trials, 3))
            fl5 = '{:.2f}'.format(getFlight(trials, 4))

            c.setFont("Times-Bold", 14)
            c.drawString(60, 450,   "[1]")
            c.drawString(60, 430,   "[2]")
            c.drawString(60, 410,   "[3]")
            c.drawString(60, 390,   "[4]")
            c.drawString(60, 370,   "[5]")
            c.drawString(130, 450,   epidosi1+" cm")
            c.drawString(130, 430,   epidosi2+" cm")
            c.drawString(130, 410,   epidosi3+" cm")
            c.drawString(130, 390,   epidosi4+" cm")
            c.drawString(130, 370,   epidosi5+" cm")
            c.drawString(220, 450,   imp1+" sec")
            c.drawString(220, 430,   imp2+" sec")
            c.drawString(220, 410,   imp3+" sec")
            c.drawString(220, 390,   imp4+" sec")
            c.drawString(220, 370,   imp5+" sec")
            c.drawString(320, 450,   fl1+" sec")
            c.drawString(320, 430,   fl2+" sec")
            c.drawString(320, 410,   fl3+" sec")
            c.drawString(320, 390,   fl4+" sec")
            c.drawString(320, 370,   fl5+" sec")
            c.setFont("Times-Bold", 15)
            c.drawString(30, 360, "____________________________________________________________________________ ")

            figure1 = plt.figure(figsize=(5,3), dpi=100)
            plt.bar([1,2,3,4,5],[float(epidosi1),float(epidosi2),float(epidosi3),float(epidosi4),float(epidosi5)],color="blue")
            plt.ylabel(" ΚΑΤΑΚΟΡΥΦΟ ΑΛΜΑ")
            plt.xlabel("ΑΡΙΘΜΟΣ ΑΛΜΑΤΟΣ")
            imgdata= BytesIO()
            figure1.savefig(imgdata,format='svg')
            imgdata.seek(0)
            drawing=svg2rlg(imgdata)
            renderPDF.draw(drawing,c,10,85)

            c.setFont("Times-Bold", 7)
            c.drawString(10, 10, "Powered by AISA - 3T - TSIRAKOS K. DIMITRIOS copyright 2020")
            c.showPage()
            c.save()
            return

# APLA KATAKORYFA ALMATA - SYNOLO 6
def aplo_kat_1():
    dokimasia = str("1. ΚΑΤΑΚΟΡΥΦO ΑΛΜΑ ΜΕ ΧΕΡΙΑ")
    print (dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti0(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data0(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return
def aplo_kat_2():
    dokimasia = str("2. ΚΑΤΑΚΟΡΥΦΟ ΑΛΜΑ ΧΩΡΙΣ ΧΕΡΙΑ")
    print (dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti0(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data0(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return
def aplo_kat_3():
    dokimasia = str("3. ΚΑΤΑΚΟΡΥΦΟ ΑΛΜΑ-ΑΡΙΣΤΕΡΟ ΠΟΔΙ")
    print (dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti0(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data0(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return
def aplo_kat_4():
    dokimasia = str("4. ΚΑΤΑΚΟΡΥΦΟ ΑΛΜΑ-ΔΕΞΙ ΠΟΔΙ")
    print (dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti0(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data0(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return

def aplo_kat_5():
    dokimasia = str("5. DROP JUMP ΜΕ ΧΕΡΙΑ - 30 cm")
    print (dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti_drop(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data_drop(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return
def aplo_kat_6():
    dokimasia = str("6. DROP JUMP ΧΩΡΙΣ ΧΕΡΙΑ - 30 cm")
    print (dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti_drop(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data_drop(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return
def aplo_kat_7():
    dokimasia = str("5. DROP JUMP ΜΕ ΧΕΡΙΑ - 50 cm")
    print (dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti_drop(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data_drop(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return
def aplo_kat_8():
    dokimasia = str("6. DROP JUMP ΧΩΡΙΣ ΧΕΡΙΑ - 50 cm")
    print (dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti_drop(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data_drop(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return

# POLLAPLA KATAKORYFA ALMATA - OFF VJUMP SYNOLO 4
def pollaplo_kat_1():
    dokimasia = str("1. ΠΟΛΛΑΠΛΑ ΑΛΜΑΤΑ ΜΕ ΧΕΡΙΑ - OFF VJmat")
    print (dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # gets personal data from data input box
def pollaplo_kat_2():
    dokimasia = str("2. ΚΑΤΑΚΟΡΥΦΑ ΠΟΛΛΑΠΛΑ ΧΩΡΙΣ ΧΕΡΙΑ-OFF VJmat")
    print(dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti(surname, name, sclub, sport, ybirth, weight, height, pbjump, email, dokimasia)  # calls data input box
    kataxorisi_data(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return
def pollaplo_kat_3():
    dokimasia = str("3. ΠΟΛΛΑΠΛΑ ΑΛΜΑΤΑ ΑΡΙΣΤΕΡΟ ΠΟΔΙ - OFF VJmat")
    print(dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti(surname, name, sclub, sport, ybirth, weight, height, pbjump, email, dokimasia)  # calls data input box
    kataxorisi_data(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return
def pollaplo_kat_4():
    dokimasia = str("4. ΠΟΛΛΑΠΛΑ ΑΛΜΑΤΑ ΔΕΞΙ ΠΟΔΙ- OFF VJmat")
    print(dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti(surname, name, sclub, sport, ybirth, weight, height, pbjump, email, dokimasia)  # calls data input box
    kataxorisi_data(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,
                    dokimasia)  # gets personal data from data input box
    return

# POLLAPLA KATAKORYFA ALMATA - ON VJMAT - SYNOLO 4
def pollaplo_kat_on_1():
    dokimasia = str("1. ΚΑΤΑΚΟΡΥΦΑ ΠΟΛΛΑΠΛΑ ΜΕ ΧΕΡΙΑ-ON VJmat")
    print(dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti3(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data3(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # gets personal data from data input box
    return
def pollaplo_kat_on_2():
    dokimasia = str("2. ΚΑΤΑΚΟΡΥΦΑ ΠΟΛΛΑΠΛΑ ΧΩΡΙΣ ΧΕΡΙΑ-ON VJmat")
    print(dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti3(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data3(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # gets personal data from data input box
    return
def pollaplo_kat_on_3():
    dokimasia = str("3. ΚΑΤΑΚΟΡΥΦΑ ΠΟΛΛΑΠΛΑ - ΑΡΙΣΤΕΡΟ ΠΟΔΙ-ON VJmat")
    print(dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti3(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data3(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # gets personal data from data input box
    return
def pollaplo_kat_on_4():
    dokimasia = str("4. ΚΑΤΑΚΟΡΥΦΑ ΠΟΛΛΑΠΛΑ - ΔΕΞΙ ΠΟΔΙ-ON VJmat")
    print(dokimasia)
    surname = None
    name = None
    sclub = None
    sport = None
    ybirth = None
    weight = None
    height = None
    pbjump = None
    email = None
    data_kouti3(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # calls data input box
    kataxorisi_data3(surname, name, sclub, sport, ybirth, weight, height, pbjump, email,dokimasia)  # gets personal data from data input box
    return

menubar = Menu(top)
# MENU APLO ALMA SUBJECT ON MAT


file = Menu(menubar, tearoff=200)
#top.config(bg="grey")
file.add_command(label="1. ΚΑΤΑΚΟΡΥΦO ΑΛΜΑ ΜΕ ΧΕΡΙΑ", command=aplo_kat_1)
file.add_command(label="2. ΚΑΤΑΚΟΡΥΦΟ ΑΛΜΑ ΧΩΡΙΣ ΧΕΡΙΑ",command=aplo_kat_2)
file.add_command(label="3. ΚΑΤΑΚΟΡΥΦΟ ΑΛΜΑ-ΑΡΙΣΤΕΡΟ ΠΟΔΙ", command=aplo_kat_3)
file.add_command(label="4. ΚΑΤΑΚΟΡΥΦΟ ΑΛΜΑ-ΔΕΞΙ ΠΟΔΙ", command=aplo_kat_4)
file.add_command(label="5. DROP JUMP ΜΕ ΧΕΡΙΑ - 30cm ", command=aplo_kat_5)
file.add_command(label="6. DROP JUMP ΧΩΡΙΣ ΧΕΡΙΑ - 30cm ", command=aplo_kat_6)
file.add_command(label="5. DROP JUMP ΜΕ ΧΕΡΙΑ - 50cm ", command=aplo_kat_7)
file.add_command(label="6. DROP JUMP ΧΩΡΙΣ ΧΕΡΙΑ -50cm", command=aplo_kat_8)
file.add_separator()
file.add_separator()
file.add_command(label="ΕΞΟΔΟΣ -EXIT", command=top.quit)
menubar.add_cascade(label="ΑΠΛΑ ΚΑΤΑΚΟΡΥΦΑ ΑΛΜΑΤΑ", menu=file)
edit = Menu(menubar, tearoff=200)

# MENU ΠΟΛΛΑΠΛΑ ALMAΤΑ  SUBJECT ON MAT
file = Menu(menubar, tearoff=200)
file.add_command(label="1. ΠΟΛΛΑΠΛΑ ΑΛΜΑΤΑ ΜΕ ΧΕΡΙΑ - OFF VJmat", command=pollaplo_kat_1)
file.add_command(label="2. ΠΟΛΛΑΠΛΑ ΑΛΜΑΤΑ ΧΩΡΙΣ ΧΕΡΙΑ - OFF VJmat",command=pollaplo_kat_2)
file.add_command(label="3. ΠΟΛΛΑΠΛΑ ΑΛΜΑΤΑ ΑΡΙΣΤΕΡΟ ΠΟΔΙ - OFF VJmat", command=pollaplo_kat_3)
file.add_command(label="4. ΠΟΛΛΑΠΛΑ ΑΛΜΑΤΑ ΔΕΞΙ ΠΟΔΙ- OFF VJmat", command=pollaplo_kat_4)
file.add_separator()
file.add_separator()
file.add_command(label="ΕΞΟΔΟΣ -EXIT", command=top.quit)
menubar.add_cascade(label="ΠΟΛΛΑΠΛΑ ΚΑΤΑΚΟΡΥΦΑ ΑΛΜΑΤΑ OFF VJmat", menu=file)
edit = Menu(menubar, tearoff=200)

# MENU POLLPLA ALMATA SUBJECT OFF MAT
file = Menu(menubar, tearoff=200)
file.add_command(label="1. ΚΑΤΑΚΟΡΥΦΑ ΠΟΛΛΑΠΛΑ ΜΕ ΧΕΡΙΑ-ON VJmat", command=pollaplo_kat_on_1)
file.add_command(label="2. ΚΑΤΑΚΟΡΥΦΑ ΠΟΛΛΑΠΛΑ ΧΩΡΙΣ ΧΕΡΙΑ-ON VJmat",command=pollaplo_kat_on_2)
file.add_command(label="3. ΚΑΤΑΚΟΡΥΦΑ ΠΟΛΛΑΠΛΑ - ΑΡΙΣΤΕΡΟ ΠΟΔΙ-ON VJmat", command=pollaplo_kat_on_3)
file.add_command(label="4. ΚΑΤΑΚΟΡΥΦΑ ΠΟΛΛΑΠΛΑ - ΔΕΞΙ ΠΟΔΙ-ON VJmat", command=pollaplo_kat_on_4)
file.add_separator()
file.add_separator()
file.add_command(label="ΕΞΟΔΟΣ -EXIT", command=top.quit)
menubar.add_cascade(label="ΠΟΛΛΑΠΛΑ ΚΑΤΑΚΟΡΥΦΑ ΑΛΜΑΤΑ ON VJmat", menu=file)
edit = Menu(menubar, tearoff=200)

# ABOUT
file = Menu(menubar)
file.add_command(label="DEVELOPER")
file.add_command(label="ΚΑΝΟΝΕΣ ΧΡΗΣΗΣ")
file.add_command(label="ΕΓΧΕΙΡΙΔΙΟ ΧΡΗΣΗΣ")
file.add_separator()
file.add_separator()
file.add_command(label="ΕΞΟΔΟΣ -EXIT", command=top.quit)
menubar.add_cascade(label="ABOUT", menu=file)
edit = Menu(menubar, tearoff=200)
top.config(menu=menubar)
top.mainloop()




