from machine import Pin, TouchPad
led = Pin(2, Pin.Out)
touch = TouchPad (Pin(4))

while True:
    if touch.read()<400
    led.value(not led.value())
    print("Led is turned on" if led.value() else "Led turned off")
    while touch.read()<400:
        pass