from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo=20, trigger =21)

while True:
    print('Distnace:',sensor.distance *100)
    time.sleep(1)