import time
import webbrowser
from tkinter import *
import datetime
from threading import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def six_am_routine():
    print(time.strftime("%H:%M:%S"))
    print("It's TIME!!\nGET AFTER IT!!\n")
    # URL of website
    webbrowser.open('https://www.youtube.com/watch?v=JDJz9JA9qxc&list=PL_6yYTbdnwfmdOf5SSzzljlhZIahw5NUX', new=())

    
def morning_gui():
    pass
    # Morning GUI opens up with the sound of jocko alarm -> Type in I AM AWAKE
    #root = Tk()
    #root.geometry("400x200")
    #Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
    #Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
    #frame = Frame(root)
    #frame.pack()
    
def night_gui():
    pass

def nighty_night():
    print(time.strftime("%H:%M:%S"))
    # gui for nighty night
    
    # Timer to close other applications
    print("turn other devices off\nturn on the alarm\nturn off the lights\ntime to sleep\n")

    # Add delay
    driver = webdriver.Chrome()
    # Play the video for night time
    webbrowser.open('https://www.youtube.com/watch?v=wM5CCu2NH2E&list=PL_6yYTbdnwflAZuIhuM_nIgJPXAePYuth', new=())
    url = "https://www.youtube.com/watch?v=wM5CCu2NH2E&list=PL_6yYTbdnwflAZuIhuM_nIgJPXAePYuth"
    
    # Opening the website
    driver.get(url)
  
    # Wait for 2 hrs
    time.sleep(6000) # Add Delay
    
    # Closes the current window
    driver.close()
      
if __name__ == "__main__":
    while time.strftime("%H:%M:%S") != "06:00:00" or "22:00:00":
      time.sleep(1)
      if time.strftime("%H:%M:%S") == "06:00:00": six_am_routine()		
      if time.strftime("%H:%M:%S") == "23:00:00": nighty_night()
