import functions
import threading, queue
import time

reading = False
q = []
ser = functions.initializeSerialPort()
continious_reading_thread = None
stop_reading_variable = True
status = None

"""
Create Reading thread function
This function is creating a thread with the
reading function in order to not block the
main thread which is the TK window
"""
def create_thread():
    global stop_reading_variable
    global continious_reading_thread
    stop_reading_variable = False
    continious_reading_thread = threading.Thread(target=start_reading)
    continious_reading_thread.start()

""""
Reading Function
This threads purpose is to create
reading threads that read one value from serial port
and return it inside a queue

We wait for the function to get the value (t.join())
and then we read it.
"""
def start_reading():
    while True:
        global ser
        global q
        global status
        t = threading.Thread(target=functions.readData, args=(
        ser, q))
        t.start()
        t.join()
        status = q.pop()

        if(len(q) == 200):
            q = []

        if stop_reading_variable:
            q = []
            break
"""
Stop reading function
This function is setting
stop_reading_variable to false.
This variable instructs the reading function (start_reading)
to break from the infinite loop and let the thread end
Finally we wait for the thread to finish (continious_reading_thread.join())
before continue.
"""
def stop_reading():
    global stop_reading_variable
    stop_reading_variable = True
    continious_reading_thread.join()
    print('Stopped reading')


"""
We use this variable to get rid of the random None
We store the last not None state and once we get a None 
we sent this one instead. This will replace 

False, None, True 
with 
False, False, True
"""
previous_status = True

"""
THIS FUNCTIONS IS THE MOST IMPORTANT ONE
USING THING AT ANY TIME YOU CAN GET THE STATE
OF THE MAT
"""
def microbit_touched():
    global q
    global previous_status
    global status
    if status == '':
        print(status , previous_status)
        return previous_status
    elif status == '0':
        print(status , True)
        previous_status = True
        return True
    elif status == '1':
        print(status , False)
        previous_status = False
        return False