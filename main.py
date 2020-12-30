try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error: Program must be executed with superuser permissions (sudo)")

import time

GPIO.setmode(GPIO.BCM)

cap = 0.33 #capacitor uf
res = 1000 #resistor ohms

pin1 = 17
pin2 = 22
ledpin = 18

led = GPIO.PWM(ledpin, 500)
led.start(100)

def charge_cycle():
    GPIO.setup(pin1, GPIO.IN)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.output(pin2, False)
    time.sleep(0.05)
    
def charge_reading():
    GPIO.setup(pin2, GPIO.IN)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin1, True)
    time1 = time.time()
    while GPIO.input(pin2) == False:
        ...
    time2 = time.time()
    return (t2 - t1) * 10000

def read():
    charge_cycle()
    ctime = charge_reading()
    charge_cycle()
    return time

def read_resistor():
    n = 20
    tot = 0;
    for i in range(1, n):
        tot = total + read()
    ctime = total/float(n)
    T = ctime * 0.632 * 3.3
    r = (T / C) - res
    return r

def calculate_brightness():
    res_reading = int(read_resistor())
    brightness_set_value = int(res_reading-35)
    if brightness_set_value < 0:
        brightness_set_value = 0
    if brightness_set_value > 100:
        brightness_set_value = 100
    return brightness_set_value

def update_brightness():
    brightness = calculate_brightness()
    GPIO.ChangeDutyCycle(brightness)

running = True

try:
    while running == True:
        update_brightness()
        time.sleep(0.1)
        
except KeyboardInterrupt:
    running = False
    
except:
    print("An error occured.")
    print("The program is being closed to prevent damage to the components.")
    running = False
    
finally:
    print("Cleaning up...")
    GPIO.cleanup()


