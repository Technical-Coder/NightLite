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
    return (t2 - t1) * 1000000

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

running = True

try:
    while running == True:
        print(read_resistance()) #debug
        time.sleep(0.5)
        
except KeyboardInterrupt:
    running = False
    
finally:
    print("Cleaning up...")
    GPIO.cleanup()

