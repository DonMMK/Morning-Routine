import time
import webbrowser
from tkinter import *
import datetime
from threading import *

def six_am_routine():
    print(time.strftime("%H:%M:%S"))
    print("It's TIME!!\nGET AFTER IT!!\n")
    
    # Morning GUI
    root = Tk()
    root.geometry("400x200")
    Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
    Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
    frame = Frame(root)
    frame.pack()
    
    # Add delay
    webbrowser.open('https://www.youtube.com/watch?v=9vJRopau0g0&list=PL_6yYTbdnwfmdOf5SSzzljlhZIahw5NUX', new=())


def nighty_night():
    print(time.strftime("%H:%M:%S"))
    # gui telling you to stop doing work
    
    # Timer to close other applications
    print("turn other devices off\n turn on the alarm\nturn off the lights\ntime to sleep\n")
    # Add Delay
    webbrowser.open('https://www.youtube.com/watch?v=wM5CCu2NH2E&list=PL_6yYTbdnwflAZuIhuM_nIgJPXAePYuth', new=())
      
if __name__ == "__main__":
    while time.strftime("%H:%M:%S") != "06:00:00" or "22:00:00":
      time.sleep(1)
      if time.strftime("%H:%M:%S") == "06:00:00": six_am_routine()		
      if time.strftime("%H:%M:%S") == "22:00:00": nighty_night()
