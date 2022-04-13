import time

def six_am_routine():
    print(time.strftime("%H:%M:%S"))
    print("It's TIME!!")

if __name__ == "__main__":
    while time.strftime("%H:%M:%S") != "12:39:00":
      time.sleep(1)
    else:
        six_am_routine()		
