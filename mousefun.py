import random
import time as t
import pyautogui as pag

# input for timer
runtime=float(pag.prompt(text='How many minutes do you want to run for?',title='Automouse',default=60))
sleeptime=int(pag.prompt(text='How many seconds between mouse movements?',title='Automouse',default=2))

# #variables for total time and mouse movement intervals
sectime=int(runtime*60)
loop=1

starttime=int(t.time())

#loop to move mouse until designated time
while True:
    width,height=pag.size()
    x=random.randint(0,width)
    y=random.randint(0,height)
    pag.moveTo(x,y,1.0,pag.easeOutQuad)
    if loop%100==0:
        pag.rightClick()
    
    t.sleep(sleeptime)
    currenttime=int(t.time())

    if currenttime-starttime>=sectime:
        response=pag.confirm(text="It's been about %d minute(s)" %runtime,title="Automouse",buttons=['Keep Going','Stop'])
        if response=='Keep Going':
            loop=0
            starttime=int(t.time())
        else:
            break
    else: loop+=1