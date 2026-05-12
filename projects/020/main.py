print("Project 020 - Countdown Timer")
# This is the file number 20- Countdown Timer

import time

minutes=int(input("Enter minutes: "))
seconds=int(input("Enter seconds: "))

total_seconds=(minutes*60)+seconds

while total_seconds>0:
    minutes=total_seconds//60
    seconds=total_seconds %60

    timer=f"{minutes:02d}:{seconds:02d}"
    print(timer,end="\r")

    time.sleep(1)
    total_seconds-=1

print("time's up!")   