# import requests
from gpiozero import Button
from datetime import datetime, timedelta
# from src import settings

# root_url = settings.HOST_URL
# button_gpio_pin=18
# longpress_threshold=100 # ms

Button.pressed_time = None

def pressed(btn):
    if btn.pressed_time:
        if btn.pressed_time + timedelta(seconds=0.6) > datetime.now():
            print("pressed twice")
        else:
            print("too slow") # debug
        btn.pressed_time = None
    else:
        print("pressed once")  # debug
        btn.pressed_time = datetime.now()

btn = Button(3)
btn.when_pressed = pressed

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