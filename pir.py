from gpiozero import MotionSensor,LED

pir = MotionSensor(18)
led= LED(15)

while True:
    if pir.value == 1:
        led.on()
        print("motion detect")
    else:
        led.off()
        print("no motion")