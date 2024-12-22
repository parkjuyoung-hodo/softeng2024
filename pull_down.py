from gpiozero import LED
from gpiozero import Button
from time import sleep

led= LED(21)
switch =Button(20)
pulldown= LED(16)

while True:
    pulldown.off()
    sleep(0.5)

    if switch.is_pressed:
        led.off()
        print("switch:off")
    else:
        led.on()
        print("switch:on")