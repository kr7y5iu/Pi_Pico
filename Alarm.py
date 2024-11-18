from machine import Pin
import time
from time import sleep
 
pir = Pin(2, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(14, Pin.OUT)
led = Pin(15, Pin.OUT)
n = 0
 
print('Starting up the PIR Module')
time.sleep(1)
print('Ready')

sleep(5)
print ("alarm załączony")
while True:
     if pir.value() == 1:
          n = n+1
          print('Motion Detected ',n)
          l=0
          while l< 5:
              buzzer.value(1)
              led.value(1)
              sleep(0.25)
              buzzer.value(0)
              led.value(0)
              sleep(0.25)
              buzzer.value(1)
              led.value(1)
              sleep(0.25)
              buzzer.value(0)
              led.value(0)
              sleep(0.25)
              l=l+1
          sleep(5)
