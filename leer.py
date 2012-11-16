from arduino import Arduino
import time

b = Arduino('/dev/ttyACM0')
pin1 = 1
pin2 = 2

b.output([])

while (True):
    val = b.analogRead(pin1)
    print val
    time.sleep(0.5)
if val="0":
   	b.setHigh(pin2)
else:
   	b.setLow(pin2)
   	pass
