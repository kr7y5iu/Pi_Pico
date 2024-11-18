import machine
import time
from machine import Pin
from utime import sleep
trig = Pin(0, Pin.OUT)  
echo = Pin(1, Pin.OUT)  
buzzer = Pin(15, Pin.OUT)
def get_distance(trig, echo):
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()
    while echo.value()==0:
        singal_off=time.ticks_us()
        #print ("here")
    while echo.value()==1:
        singal_on=time.ticks_us()
    time_passed=singal_on-   singal_off
    distance2 = (time_passed * 0.0343) / 2
    return distance2
while True:
    distance = get_distance(trig,echo)
    print("distance:",distance, "CM")
    if distance < 15:
        print("<15")
        buzzer.value(1)
        sleep(1)
        buzzer.value(0)

    elif distance > 15:
          print(">15")
          buzzer.value(1)
          sleep(0.2)
          buzzer.value(0)
          sleep(distance / 160)
    
