from machine import Pin
from time import sleep

p28 = Pin(28, Pin.IN)
p27 = Pin(27, Pin.IN)
l1 = Pin(1, Pin.OUT)
l2 = Pin(2, Pin.OUT)
while True:
  if p28.value() == 1:
    l1.value(1)
  elif p28.value() == 0:
    l1.value(0)
  print(p28.value())
  if p27.value() == 1:  
    l2.value(1)
    sleep(1)
  if p27.value() == 1:
    l2.value(0)
    sleep(1) 