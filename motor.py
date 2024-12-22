from gpiozero import AngularServo
from time import sleep

servo_pin =18

servo = AngularServo(servo_pin,min_angle=0, max_angle=180, min_pulse_width =0.0006, max_pulse_width=0.0024)

while True:
    servo.angle(0)
    sleep(1)

    servo.angle(90)
    sleep(1)

    servo.angle(180)
    sleep(1)