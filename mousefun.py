import random
import time
import pyautogui as pag

# input for timer
runtime=pag.prompt(text='How many minutes do you want to run for?',title='Automouse',default=30)
sleeptime=pag.prompt(text='How many seconds between mouse movements?',title='Automouse',default=1)

# #variables for total time and mouse movement intervals
sleeptime=int(sleeptime)
runtime=float(runtime)
sectime=runtime*60
sectime=int(sectime)
interval=int(sectime/sleeptime)
loop=1

#loop to move mouse until designated time
while True:
    width,height=pag.size()
    x=random.randint(0,width)
    y=random.randint(0,height)
    pag.moveTo(x,y,1.0,pag.easeOutQuad)
    if loop%100==0:
        pag.rightClick()
    
    time.sleep(sleeptime)

    if loop==interval:
        response=pag.confirm(text="It's been about %d minute(s)" %runtime,title="Automouse",buttons=['Keep Going','Stop'])
        if response=='Keep Going':
            loop=0
        else:
            break
    else: loop+=1