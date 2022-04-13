from signal import alarm
import time
import webbrowser

def six_am_routine():
    print(time.strftime("%H:%M:%S"))
    print("It's TIME!!\nGET AFTER IT!!\n")
    # alarm function
    
    # gui function to stop the alarm
    webbrowser.open('https://www.youtube.com/watch?v=9vJRopau0g0&list=PL_6yYTbdnwfmdOf5SSzzljlhZIahw5NUX', new=())


def nighty_night():
    print(time.strftime("%H:%M:%S"))
    print("turn other devices off\n turn on the alarm\nturn off the lights\ntime to sleep\n")
    webbrowser.open('https://www.youtube.com/watch?v=wM5CCu2NH2E&list=PL_6yYTbdnwflAZuIhuM_nIgJPXAePYuth', new=())
      
if __name__ == "__main__":
    while time.strftime("%H:%M:%S") != "06:00:00" or "22:00:00":
      time.sleep(1)
      if time.strftime("%H:%M:%S") == "06:00:00": six_am_routine()		
      if time.strftime("%H:%M:%S") == "22:00:00": nighty_night()
