from playsound import playsound

import time

CLEAR ="\033[2J"                                   #to clear the text on screen
Clear_AND_RETURN = "\033[H"                        #to return the cursor to home directory and overwrite the text already there

def alarm(seconds):
    time_elapsed =0


    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed +=1

        time_left = seconds - time_elapsed
        hours_left = time_left // 3600              #to calculate hours in alarm
        minutes_left = time_left //60               #to calculate minutes in alarm
        seconds_left = time_left % 60               #to calculate 

        print(f"{Clear_AND_RETURN} Alarm will ring in : {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")
    
    playsound("alarm.mp3")

hours = int(input("How many hours to wait: "))             #Assuming user will give valid input
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))

Total_seconds = (hours *3600) + (minutes*60) + seconds

alarm (Total_seconds)