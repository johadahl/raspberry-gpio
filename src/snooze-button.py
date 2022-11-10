# import requests
from gpiozero import Button
from datetime import datetime, timedelta
from signal import pause
# from src import settings

# ROOT_URL = settings.HOST_URL
THRESHOLD = 600 #ms
GPIO_PIN = 2

Button.pressed_time = None

def pressed(btn):
    pressed = datetime.now()
    if btn.wait_for_release(timeout=0.6):
        timeout = pressed - datetime.now()
        if btn.wait_for_press(timeout=0.6):
            print("pressed twice")
        else:
            print("pressed once")

btn = Button(GPIO_PIN)
btn.when_pressed = pressed
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