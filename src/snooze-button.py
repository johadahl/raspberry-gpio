from signal import pause
from time import sleep

import requests
from gpiozero import Button

# from src import settings

# ROOT_URL = settings.HOST_URL
THRESHOLD = 0.6 # seconds
GPIO_PIN = 2

def pressed(btn):
    sleep(3)
    if btn.is_pressed == False:
        print("pressed")
        requests.patch('http://192.168.0.105:5001/v1/alarm/1?snooze=true')

def held(btn):
    print("held")
    requests.patch('http://192.168.0.105:5001/v1/alarm/1?reset=true')

btn = Button(GPIO_PIN)
btn.hold_time = THRESHOLD

btn.when_pressed = pressed
btn.when_held = held
pause()

# while True:
#     time.sleep(0.2)

#     if GPIO.input(gpio_pin) == False: # Listen for the press, the loop until it steps
#         print "Started press"
#         pressed_time=time.time()
#         while GPIO.input(gpio_pin) == False:
#             time.sleep(0.2)

#         pressed_time=time.time()-pressed_time
#         print "Button pressed %d, POSTing to nightlight server" % pressed_time
#         if pressed_time<longpress_threshold:
#             data = dict(light=2, cmd="toggle-with-timer")
#         else:
#             data = dict(light=2, cmd="toggle-keep-on")

#         r = requests.post(url, data=data, allow_redirects=True)
#         print r.content