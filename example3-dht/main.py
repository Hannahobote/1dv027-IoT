from machine import Pin
import utime as time
from dht import DHT11

# The GPIO number is 13 which is equal to the pin number 17
# pin = Pin(13, Pin.IN)
pin = Pin(13, Pin.IN)
sensor = DHT11(pin)

while True:
    time.sleep(2)
    try:
        t = sensor.temperature
        time.sleep(2)
        h = sensor.humidity
    except:
        print("An exception occurred")  
        continue  
    # print("Measure: {}".format(sensor.measure))
    print("Temperature: {}".format(sensor.temperature()))
    print("Humidity: {}".format(sensor.humidity()))

