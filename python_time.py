import time
import webbrowser

def six_am_routine():
    print(time.strftime("%H:%M:%S"))
    print("It's TIME!!\nGET AFTER IT!!\n")
    webbrowser.open('http://net-informations.com', new=())


def nighty_night():
    print(time.strftime("%H:%M:%S"))
    print("turn other devices off\n turn on the alarm\nturn off the lights\ntime to sleep\n")
    webbrowser.open('http://net-informations.com', new=())
      
if __name__ == "__main__":
    while time.strftime("%H:%M:%S") != "13:41:00" or "22:00:00":
      time.sleep(1)
      if time.strftime("%H:%M:%S") == "13:41:00": six_am_routine()		
      if time.strftime("%H:%M:%S") == "22:00:00": nighty_night()
